# Fresh-kernel mobile gates

Current shared-core checkpoint: [STATUS.md](https://github.com/auto44e/jeios/blob/main/docs/STATUS.md). Core through #86 includes ARM MMU and returning IRQ proofs; scheduling and MP3 remain ahead. Mobile integration remains planning-only at main d9a5146; core.json stays pinned to 03aa2f3 with arm64_ready=false. Earlier next-task wording below is historical.

Owner-approved [two-phase native shell and selectable shell roadmap](https://github.com/auto44e/jeios/blob/main/docs/SHELLS.md): recovery + original JeiOS sh, included native Bash/Zsh, and bring-your-own shell. PowerShell deferred. Planned, not runtime support.

## Historical ecosystem status — observed 2026-11-01T21:30:30-05:00

Core main `0f702036c52d40d03bb4c8919d0dcae53ba9f2b1`: AMD64 M3 and scoped M4 complete; PR #70
merged. ARM64 MP1 complete (#52); MP2 then MP3 remain. Main CI passed:
https://github.com/auto44e/jeios/actions/runs/41376309893 . M4 qualifies bounded
supervisor/broker/COM2 UART scenarios, not arbitrary hardware, DMA or a release.
Mobile main `f1d9b0d87746e9dc353a2f48e7b9d27e7fe86d07` has passing planning CI:
https://github.com/auto44e/jeios-mobile/actions/runs/39243515951 . Its core pin
remains older M1/M2; upstream progress does not qualify that integration.
No open PRs were observed before this refresh. M4 #53 is now closed as completed;
MP2 (mobile #2) is next execution work; M5a #54 remains planned.

Shell roadmap: SH1 recovery #71, SH2 original native sh #72, included native
Bash/Zsh and custom-shell registration #73; mobile parity #12. PowerShell deferred.
All shell implementation remains planned. Storage, networking, desktop, POSIX
completion, LDAP, encryption, fleet/ISO 27001 features, RISC-V, accelerators and
Android execution remain later gates. Standards adoption is not certification.
This current status supersedes older next-task/status wording below; timestamped
records remain evidence at their original revisions, not new test runs.


No deadlines or implied device support. Dependencies are acceptance boundaries.
Core AMD64 M3 is complete; mobile must qualify equivalent ARM64 state separately.

| Gate | Deliverable | Pass criteria / dependency |
| --- | --- | --- |
| MP0 | Shared-core lock and ARM64 boot/architecture ADR | Exact tool/board/loader contract; core ownership; reviewed failure model |
| MP1 | ARM64 entry, console, boot context and vectors | Real QEMU serial markers; malformed boot input and deliberate exception tests |
| MP2 | MMU, memory, interrupts/timer and kernel scheduling | W^X/guards; register/preemption/accounting/failure tests; depends MP1 |
| MP3 | EL0 processes, rights/handles, IPC and native init | Isolation, checked copy, stale-right rejection, survivor progress; depends core M3 and MP2 |
| MP4 | Pixel 9 hardware feasibility dossier | Boot/recovery/firmware/driver evidence and explicit blockers; research can start alongside MP0 |
| MP5 | Qualified physical native bring-up | Authorized device experiments and read-only-first drivers; MP1-MP4 and recovery plan |
| MP6 | Native mobile services and shell | Input, display, power, storage/network isolation and parity evidence; only tested hardware |
| AC0 | Android dependency and approach ADR | Explicit ABI/runtime/Binder dependency ledger and prototype criteria |
| AC1 | Minimal native/Binder/runtime probes | Exact tested compatibility subset; requires native isolation and relevant services |
| AC2 | Curated Android apps across ISA/device profiles | App/version/ABI matrix and native authority containment, no blanket support |
| SEC | Mobile release qualification | Signed update/recovery, entropy/key isolation, power-loss/thermal and reviewed security evidence |

Current: MP0 complete (mobile #1 closed; PR #9 merged). MP1 entry/console and
EL1 vectors execute in the shared core; DTB parsing remains in core #52, alongside
remote ARM boot CI. MP2 MMU/timer/scheduling then MP3 EL0/IPC parity remain planned
in mobile #2. Core #53 M4 and #54 read-only M5a define the native service phase;
see the shared [phase plan](https://github.com/auto44e/jeios/blob/main/docs/NEXT_PHASE.md).
The old config/core.json pin is not advanced by this docs-only update.
MP4/AC0 research can proceed without claiming physical device or app execution.
Pixel 10 receives a distinct MP4/MP5 record; Pixel 9 success cannot qualify it.

## Cross-cutting zero trust — owner requirement 2026-10-14

Follow the shared core zero-trust proposal linked in HANDOFF.md. MP0 records trust
boundaries; MP3 qualifies process/handle/IPC enforcement; MP6 and AC gates test
native broker permissions and foreign identity mapping; SEC tests enrollment,
revocation, offline policy and recovery. Neither paired peers nor first-party
services gain ambient authority. These are planned acceptance requirements.

## Core POSIX and LDAP requirements — 2026-10-16

The owner requires POSIX.1-2024 compatibility and built-in LDAPv3 directory
integration across desktop and mobile. Shared contracts are in the companion core
[standards proposal](https://github.com/auto44e/jeios/blob/main/docs/STANDARDS.md).
The standards proposal was merged through core PR #17.
Implementation belongs in shared core/runtime services, not a mobile fork.

Qualify POSIX semantics on native ARM64 and LDAP identity mapping under suspend,
network loss, cache expiry, relock and work-profile separation. Enrollment remains
optional and unmanaged local accounts work offline. Expose unsupported operations
honestly; Android support, AD DS/GPO and cloud identity are separate qualifications.
MP0 is complete; full userspace execution waits for MP3 and relevant core M3-M6/SEC gates.
No runtime or conformance claim is added by these requirements.

Track core [#15](https://github.com/auto44e/jeios/issues/15) and
[#16](https://github.com/auto44e/jeios/issues/16) through mobile parity issue #5.

## Ecosystem coding discipline — 2026-10-16

Adopt the shared [coding-policy proposal](https://github.com/auto44e/jeios/blob/main/docs/CODING_STANDARD.md)
(core PR #17, enforcement core #19) across integration, tools, apps and packaging.
Policy is adopted; actual dependencies still require reviewed commit pins.
MP1 completion is next. Future mobile assurance must include native ARM64, device/power
and recovery evidence; current manifest tests cannot establish those properties.
