# Fresh-kernel mobile gates

No deadlines or implied device support. Dependencies are acceptance boundaries.
Core AMD64 M3a continues independently; mobile must qualify equivalent ARM64 state.

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

Now: planning scaffold only. Next coding task MP0, then core ARM64 MP1.
MP4/AC0 planning can proceed without claiming emulator or app execution.
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
[standards proposal](https://github.com/auto44e/jeios/blob/docs/posix-ldap-20261016/docs/STANDARDS.md).
The branch link identifies the unmerged proposal; use main after it lands.
Implementation belongs in shared core/runtime services, not a mobile fork.

Qualify POSIX semantics on native ARM64 and LDAP identity mapping under suspend,
network loss, cache expiry, relock and work-profile separation. Enrollment remains
optional and unmanaged local accounts work offline. Expose unsupported operations
honestly; Android support, AD DS/GPO and cloud identity are separate qualifications.
MP0 remains next; execution waits for MP3 and relevant core M3-M6/SEC gates.
No runtime or conformance claim is added by these requirements.

Track core [#15](https://github.com/auto44e/jeios/issues/15) and
[#16](https://github.com/auto44e/jeios/issues/16) through mobile parity issue #5.
