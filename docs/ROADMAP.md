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
