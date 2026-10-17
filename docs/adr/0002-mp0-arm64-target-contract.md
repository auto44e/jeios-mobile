# ADR 0002: Freeze the MP0 ARM64 reproducible-target contract

Date: 2026-10-17. Status: **proposed core ADR** (the one MP0 requires before any
ARM64 code). Scope: MP0 only — the reproducible *target and boot-handoff*
contract. No kernel code accompanies this ADR; it converts the MP0 section of
[ARM64.md](../ARM64.md) into reviewed decisions. Per [ADR 0001](0001-fresh-kernel-mobile.md),
the shared kernel implementation lands in `auto44e/jeios`; this repository locks
the reviewed ARM64 contract revisions only. No Pixel or Android execution is
claimed by MP0.

## Context

JeiOS/x86-64 reached a tested single-CPU userspace boundary (M3a). The mobile
track needs a *second* architecture front, but the owner direction (ADR 0001) is
one maintained C kernel core with shared contracts, **not** a second kernel. MP0
is deliberately the cheapest possible first step: pick an exact, reproducible
virtual ARM64 target and freeze the boot handoff, so that later MP1–MP3 bring-up
(entry/exceptions, protected execution, EL0 processes) has a fixed, documented
ground to stand on. MP0 writes **no executable code** and makes **no** claim that
anything runs yet.

A specific risk shaped this ADR. The peer review of the M3a→ARM64 relationship
found that an ARM64 boot/MMU contract, written carelessly, can **silently
redefine M3a's user-copy ABI** — tagged pointers, privileged-access rules, and
exception syndromes all differ on AArch64. MP0 therefore fixes the *target* and
*handoff* and, for anything that touches the cross-architecture syscall / error /
user-pointer contract, **references a future arch-neutral contract and records an
explicit open item**, rather than inventing an ARM64-specific answer that would
later conflict with tested x86-64 behavior.

## Decision

### D1. Scope and claim

MP0 delivers a **reviewed, reproducible ARM64 target definition and boot-handoff
contract**, plus an explicit list of unsupported states and cross-architecture
open items. It delivers no boot code, no console, no MMU setup — those are MP1+.
The claim is "a pinned, reproducible virtual ARM64 target and a frozen entry
contract, reviewed on paper," never "JeiOS boots on ARM64" and never anything
about Pixel or Android.

### D2. Exact virtual target (reproducible or it does not count)

The MP0 target is a **versioned** QEMU `virt` machine, pinned so a reviewer can
reproduce the **configuration** (not a byte-for-byte execution trace — TCG is not
deterministic without `-icount`, and image reproducibility additionally needs a
deterministic build). Frozen here:

- **Emulator + accelerator:** a specific QEMU release (record the exact
  `qemu-system-aarch64 --version` string when the first config lands; pin the
  versioned machine type `virt-<X.Y>`, never bare `virt`, so the board model can't
  drift) running under **`-accel tcg`** (pinned: KVM/HVF would change the CPU model
  and EL behavior).
- **CPU model:** `cortex-a72`, **one** CPU. No SMP in MP0. Note the architectural
  consequence, recorded honestly: a72 is **ARMv8.0-A**, so it has **no PAN (v8.1),
  no UAO (v8.2), and no MTE (v8.5)**. MP0 therefore does *not* get to lean on those
  privileged-access features; MP3's user-copy model runs without them, which
  mirrors M3a's no-SMAP situation rather than hiding it (see D5). TBI is base
  v8.0 and is present.
- **GIC:** pin the version **explicitly** (e.g. `gic-version=2`) rather than
  "whatever the machine provides"; interrupt *addresses/wiring* are discovered from
  the DTB, but the controller version is part of the frozen programming contract.
- **Memory:** a fixed, modest RAM size (recorded with the config), 4 KiB
  translation granule.
- **Timer:** record `CNTFRQ_EL0` (the architected timer frequency the pinned
  machine presents) so MP2's timer bring-up has a fixed expected value.
- **No optional state / no devices:** optional architectural state is off; no
  DMA-capable device drivers; the only I/O MP0 even names is the PL011 UART, and
  only as "discovered from the DTB," not programmed. (SVE is not even present on
  a72, so "SVE off" is a statement about MP1+ policy on later cores, not this one.)
- **Toolchain:** record the exact `aarch64` cross-compiler and linker versions and
  the build flags when the first artifact lands. Two flags are **mandated now**
  because they mirror M3a invariants and are easy to get wrong: **`-mstrict-align`**
  (with the MMU off at entry, data accesses are Device-nGnRnE and unaligned
  accesses fault) and **`-mgeneral-regs-only`** plus explicit `CPACR_EL1.FPEN`
  handling (compilers emit FP/SIMD for `memcpy`/struct copies; the kernel keeps FP
  trapped, exactly as ADR 0007 D7 does on x86-64).

These are **initial simplifications for a reproducible bring-up**, explicitly not
permanent mobile limits (SMP/PSCI, SVE, power states, and real devices are later,
separately-gated milestones).

### D3. Boot delivery and entry format

The handoff is **frozen now**, because the loader choice *is* the handoff contract
(a bare ELF via `-kernel` does not guarantee the DTB-in-x0 convention; UEFI entry
would hand off with the MMU **on**). The frozen choice:

- **No firmware. QEMU direct `-kernel`.** No UEFI/EDK2, no U-Boot.
- **Image format: the Linux arm64 `Image` wrapper**, entered via `-kernel`,
  following the documented **Linux arm64 boot protocol**: on entry **`x0` = DTB
  physical address**, `x1=x2=x3=0`, **MMU off**, **D-cache off**, instruction cache
  may be on, and **DAIF masked** (all interrupts masked). The x86 Multiboot2 ELF is
  **not** reused — the ARM64 entry is its own contract.
- **Frozen layout:** load address, alignment, image bounds, and BSS/stack
  placement are fixed in the first config and recorded; the kernel **copies the DTB
  into its own reserved region** before enabling the MMU (it does not assume the
  firmware-placed DTB survives). The DTB's address/size/alignment and the
  "is-copied" decision are part of this frozen handoff.

Verify the exact `x0`/MMU/cache/DAIF state against the pinned QEMU when the first
config lands and record the observed `CurrentEL`/`SCTLR_EL1`/`DAIF` readout as
evidence — the protocol above is the *required* precondition; the first boot
*confirms* QEMU delivers it, and an unsupported deviation fails safely (D4).

### D4. Entry machine state and EL policy

The contract **pins** the entry machine state rather than observing it after the
fact:

- **Starting Exception Level: EL1, and EL1 only.** The machine is pinned
  `virtualization=off,secure=off`, under which QEMU `virt` enters a `-kernel`
  payload at **EL1 (non-secure)**. (An earlier draft said "typically EL2"; that is
  wrong for this configuration and is corrected here.) The kernel runs at EL1; it
  does **not** expect or program EL2/EL3 state. On entry the kernel reads
  **`CurrentEL` and asserts it is EL1**; any other EL (EL0 is impossible as an
  entry, EL2/EL3 would mean the machine was misconfigured) takes the **safe
  diagnostic-halt** path (D-unsupported), never limps on. Supporting an EL2 entry
  would require programming `HCR_EL2` and a drop to EL1 and is explicitly **out of
  scope** — consistent with "EL2/EL3 ownership unsupported."
- **Never assume** firmware granted hypervisor (EL2) or secure-world (EL3) control.
- **Entry MMU/cache/interrupt state is a required precondition, not an
  observation:** MMU off, D-cache off, DAIF masked, per the Linux arm64 boot
  protocol frozen in D3. The kernel's first instructions normalize from exactly
  that state (set up a stack, clear BSS, then bring up the MMU in MP2); it does not
  "record actual state and adapt."
- Unsupported EL/state is an enumerated, documented failure, consistent with the
  M3a discipline of "exact expected behavior, never timeout-or-reset as success."

### D5. Cross-architecture coupling — reference, do not redefine (the key rule)

MP0 **must not** define an ARM64-specific version of the syscall, error, or
user-pointer contract that M3a already fixed for x86-64. Where the two
architectures must eventually agree, MP0 **points at a future arch-neutral
contract** and records an **explicit open item**; it does not pick an answer that
could later conflict with tested x86-64 behavior. That arch-neutral contract (the
syscall operation + status namespace, and the *observable* user-copy semantics)
will live in **`auto44e/jeios`** and, because it touches ADR 0007 territory, is an
**owner-escalated** document — named here so MP3 has a home to reference, not
authored here.

Correcting a characterization an earlier draft got wrong: M3a's user-copy safety
does **not** "rest on the absence of SMAP." It rests on **prevalidation** (canonical
address, in-arena range, per-page present+permission) **plus** an exact-RIP,
not-present-PFEC, active-scope, CR2-in-span exception fixup. No-SMAP is a *stated
limitation* of that model (the fixup covers the approved copy site only), not its
foundation. The ARM64 port must reproduce the *prevalidation + exact-site fixup*
shape; the privileged-access hardware (PAN/UAO, absent on a72) is a separate axis.

The open items MP0 names (resolved in the arch-neutral contract or at the MP3
EL0-boundary gate, **not** in MP0 — with one interim default frozen now):

1. **Tagged user pointers (TBI / MTE).** MTE is absent on a72. TBI0 is a
   `TCR_EL1` field set whenever the MMU is first configured (MP1/MP2), so it cannot
   wait for MP3: **MP0 freezes the interim default `TBI0 = 0`** (top-byte-tagged
   user pointers are therefore faulted/rejected, mirroring ADR 0007 D9's
   reject-noncanonical rule), and MTE off. MP3 may only *relax* this through the
   arch-neutral contract, never silently.
2. **Privileged-access model (PAN / UAO) vs the x86-64 model.** a72 has neither
   PAN nor UAO, so MP3's ARM64 user-copy runs **without** them — honestly the same
   posture as M3a's no-SMAP. Recorded as an open item for the arch-neutral contract
   so that a *later* core with PAN/UAO tightens, rather than diverges from, the
   shared copy semantics.
3. **Exception-syndrome → fixup mapping.** M3a recovers a copy-site fault by
   matching an x86 `#PF` not-present PFEC at an exact RIP. The AArch64 equivalent
   reads **`ESR_EL1`** (DFSC fault status) and **`FAR_EL1`**. The exact-site fixup
   table design is MP3's, but MP0 imposes the enabling **process requirement now**
   (so MP1 doesn't foreclose it): **MP1's vector entry MUST save `ESR_EL1`,
   `FAR_EL1`, `ELR_EL1`, and `SPSR_EL1`** into the trap frame, and any fixup table
   MUST be keyed on the exact faulting PC (`ELR_EL1`), exactly as the x86 fixup is
   keyed on the exact RIP.

The syscall **operation / error namespace** (the `abi_query`/`yield`/`exit` + the
`JE_ABI_*` status values, and the provisional `copy_probe`) is expressed once in
that arch-neutral contract and **referenced** by both ports — MP0 does not
re-number or re-encode it for ARM64, and internal `je_status` numbering never
leaks into it (ADR 0007 D11).

### D6. Required evidence standard (inherited from the x86-64 discipline)

Even though MP0 ships no executable, it fixes the **evidence bar** every later MP
milestone must meet, so the pinned target is useful. For every future executable
change, record the **core commit, config/tool versions, exact command, image
hash, serial log, and exact pass markers**; and **a halted emulator is not success
without markers**. Host fuzzing complements, never replaces, CPU execution. Virtual
-board qualification is kept separate from physical ARM SoCs and from Pixel.

The negative/positive test cases are **milestone-specific**, not all required at
once (an earlier draft listed them as a single block, which conflated MP1–MP3):

- **MP1** (entry + exceptions): bad/overlapping/malformed DTB rejected; a
  deliberate synchronous exception produces the exact expected `ESR` class, not a
  reset or timeout; bounded console output.
- **MP2** (protected execution): stack-guard hit, write-to-code refused,
  execute-from-data refused, correct TLB/cache maintenance on a mapping change,
  timer fires at the recorded `CNTFRQ`, register + architectural return state
  survive preemption.
- **MP3** (EL0 boundary): user/kernel isolation, malformed/interrupted user copies,
  recovery from a user fault with the kernel surviving, and an unrelated kernel
  fault **not** swallowed by copy recovery — the ARM64 mirror of M3a's modes 4/5.

MP0 itself has no runtime markers to produce; its acceptance is the reviewed ADR +
a reproducible, pinned configuration with the unsupported states enumerated.

### D7. Manual-revision pinning before code

Before MP1 writes a single instruction, the relevant **Arm Architecture Reference
Manual** revisions (for the registers, exception model, and translation semantics
MP1–MP3 touch) are pinned and cited. This planning ADR deliberately specifies
**no register values**; it fixes the target and the process, and defers every
concrete register/bitfield to MP1+ against a pinned manual revision.

## Unsupported states (explicit, per MP0's acceptance)

Named unsupported in MP0 (each a later, separate gate, not a limitation to hide):
SMP / multi-core and PSCI; SVE/SME and other optional architectural state; EL3 /
secure world and EL2 / hypervisor ownership; DMA-capable devices and any real
peripheral beyond the DTB-discovered PL011; demand paging, and everything M3a
already excludes. An unsupported entry EL or machine state **fails safely with a
bounded diagnostic**, never silently continues.

## Consequences

- Pinning a *versioned* machine and CPU means a QEMU upgrade is a deliberate,
  recorded contract change, not silent drift — the whole point of a reproducible
  target.
- Deferring the three D5 couplings to an arch-neutral contract (rather than
  answering them in ARM64 terms now) is what prevents MP0 from quietly forking the
  tested M3a user-copy ABI; the cost is that MP3 cannot start its EL0 boundary
  until that arch-neutral contract exists.
- MP0 produces paper only. The first *executable* ARM64 evidence is an MP1
  deliverable in `auto44e/jeios`, against this frozen target.

AI-assisted design (including a peer cross-talk debate on the M3a/ARM64 coupling);
not independent human qualification. The owner is the merge gate; accepting this
ADR authorizes MP1 to begin against the pinned target, nothing more.
