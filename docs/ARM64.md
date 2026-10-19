# ARM64 port: first executable workstream

Status refreshed 2026-10-19: MP0 accepted in ADR 0002 (PR #9 merged); shared core
MP1 entry/console and EL1 exception vectors are implemented and locally QEMU-tested.
Bounded DTB parsing and remote ARM boot CI remain (core #52). MP2/MP3 remain
planned. The sections below state gate requirements, not blanket completion.
Shared implementation belongs in auto44e/jeios; config/core.json remains the
older integration pin pending a separately reviewed update.

## MP0: reproducible target contract

Select an exact QEMU release/versioned `virt` machine, AArch64 CPU model, GIC
version, memory size and boot delivery method. QEMU `virt` supplies a useful
virtual platform including PL011 and interrupt facilities; discover addresses
and interrupt routing from its validated DTB rather than assuming Pixel matches.
Record compiler/linker versions and flags. Proposed first profile: one CPU,
4 KiB pages, no SVE/SME/advanced optional state and no DMA-capable device drivers.
Those are initial simplifications, not permanent mobile limits.

Choose an entry format supported by the selected loader: ELF via a qualified
loader or a minimal ARM64 image wrapper with documented entry/DTB convention.
Do not pass the existing x86 Multiboot2 ELF to an ARM emulator and call it a port.
Freeze load address, alignment, BSS/stack placement, image bounds and handoff
registers. Record actual starting EL, MMU/cache state and interrupt masking.
Handle supported EL1/EL2 entry explicitly; unsupported EL/state must fail safely.
Never assume firmware granted hypervisor/secure-world control.

## MP1: early boot and exceptions

Add architecture assembly entry, known stack, BSS clearing and a bounded polling
console. Parse a bounded copied boot context: RAM, reserved ranges, kernel image,
DTB and init image reservations. Reject malformed DTB structure/string offsets,
overflows and overlapping/unsupported regions. Bound node depth and property
counts. Trusted bootloader output is still parsed defensively.

Install aligned VBAR vectors and specify complete saved-state layout, SPSR/ELR,
ESR/FAR diagnostics and SP selection. Unknown kernel exceptions halt with bounded
redacted diagnostics. Declare vector stack/alignment and reentrancy assumptions;
no allocating fault handler. Test deliberate synchronous exception and compare
exact expected class/status to observed behavior, not timeout or reset.

## MP2: protected execution and scheduling

Specify MAIR/TCR/TTBR/SCTLR setup, physical address width, virtual layout and valid
memory types. Map code RX, rodata R, data/stacks RW and execute-never as applicable;
include guard pages and a no-executable-writable-alias invariant. Device MMIO is
not normal cacheable RAM. Define barriers, cache maintenance and TLB invalidation
for mapping changes, executable publication and future CPU sharing. Document
address-space ID lifecycle rather than recycling ASIDs without invalidation.

Bring up the qualified GIC and architected timer with exact source/frequency,
acknowledge/end-of-interrupt and spurious interrupt behavior. Core allocator and
scheduler hooks must preserve ownership and IRQ context rules. Prove all general
register state and architectural return state survive preemption. FP/SIMD either
remains trapped/disabled for all tasks or gains full eager context management;
mobile/ART dependencies do not justify unsaved state. SMP/PSCI, SVE and power
states are later independent gates with topology and lifetime tests.

## MP3: EL0/native process boundary

Port the core M3 address-space, syscall, user-copy and fault-containment contracts.
Establish two actual EL0 processes with private memory and kernel stacks. Test
illegal access, malformed pointers, interrupted copies, stale handles and survivor
progress. User faults terminate the offending domain; unknown kernel faults do
not get swallowed by broad copy recovery. Qualify native process/handle/IPC tests
on ARM64, not just AMD64. No Android runtime before this gate.

## Required evidence

For every executable change record core commit, config/tool versions, command,
image hash, serial log and exact pass markers. Test bad boot context, low memory,
allocation rollback, stack guard, write-to-code, execute-from-data, timer state,
user/kernel isolation and recovery from user faults. A halted emulator is not
success without markers. Host fuzzing complements, never replaces CPU execution.
Separate virtual board qualification from physical ARM SoCs and from Pixel.

Reference: https://www.qemu.org/docs/master/system/arm/virt.html . Before coding,
pin relevant Arm architecture manual revisions for registers, exceptions and
translation semantics; this planning document does not specify register values.
