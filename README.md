# JeiOS Mobile

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


New contributor? Start with the [development getting-started guide](https://github.com/auto44e/jeios/blob/main/docs/GETTING_STARTED.md),
including a plain-English conversational path with an agent.

Mobile platform planning and integration for the **fresh C JeiOS kernel**.
The same core serves desktop, mobile and other qualified device profiles.
**AOSP is a reference and a future Android application compatibility layer;
it is not the mobile host OS or a replacement Linux kernel.**

Status: mobile integration scaffold; MP0 contract accepted. Current shared core
has completed scoped AMD64 M4 and QEMU ARM64 MP1 including validated DTB
parsing and remote boot CI. MP2/MP3 remain. No Pixel image, mobile UI or Android runtime exists. The
`config/core.json` pin still identifies the older M1/M2 baseline and is unchanged;
upstream progress is not qualification of that pinned integration.

## Start here

- [Agent handoff](docs/HANDOFF.md) and [AGENTS.md](AGENTS.md)
- [Architecture and ownership](docs/DESIGN.md)
- [ARM64 port contracts](docs/ARM64.md)
- [Pixel feasibility and recovery](docs/PIXEL.md)
- [Android compatibility across the ecosystem](docs/ANDROID.md)
- [Capability parity matrix](docs/PARITY.md)
- [Gated roadmap](docs/ROADMAP.md)
- [Decision: fresh kernel first](docs/adr/0001-fresh-kernel-mobile.md)

Qualified early-boot target in shared core: QEMU `virt-8.2` / `cortex-a72`,
as specified in ADR 0002. Full ARM execution remains MP2/MP3 work.
First physical candidate: Pixel 9 `tokay`; Pixel 10 `frankel` follows independent
feasibility review. Neither is supported or flashable. No Android `lunch` target
is currently applicable to the fresh-kernel build.

```sh
python3 tools/validate.py
python3 tools/target_plan.py
python3 -m unittest discover -s tests -v
```

These check planning configuration and documentation, not kernel execution.
See [config/core.json](config/core.json) for the pinned shared-core reference.
There is deliberately no second copy of the kernel source in this repository.
Original files use Apache-2.0; dependencies retain their own licenses.
