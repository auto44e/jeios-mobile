# Mobile agent handoff

2026-10-13. Repository: auto44e/jeios-mobile. Owner selected the fresh JeiOS C
kernel for mobile, explicitly superseding the AOSP/Linux host proposal. AOSP is
reference material and a future Android app layer across the ecosystem.

Implemented: original architecture/ARM64/Pixel/Android/parity planning, core pin,
manifest inspector/validator, negative schema tests and CI definition. No ARM64
kernel source, emulator boot, Pixel image, hardware drivers, UI or Android runtime
is implemented in this scaffold. No AOSP/vendor code or binary imported.

Shared core pin: 03aa2f380d8e49262abd1720a3b8db37517cbb31, AMD64 foundation only.
First execution target: QEMU ARM64 virt after MP0. Pixel 9 tokay first physical
candidate; Pixel 10 frankel needs independent evidence. No Android lunch target.
Cuttlefish can be a future reference lab, never the selected native boot target.

Next task MP0: core ARM64 ADR with exact toolchain/versioned board, loader/EL/DTB,
MMU/vector/interrupt/state contracts and code ownership. Pass before MP1 code.
Core M3a continues; MP3 depends on equivalent tested native isolation. MP4 Pixel
research and AC0 Android dependency mapping are bounded planning workstreams.

Validation performed locally: `python3 tools/validate.py`,
`python3 tools/target_plan.py`, `python3 -m unittest discover -s tests -v` and
Python syntax checks. These test planning artifacts only. Remote CI is separate;
no runtime/hardware success should be inferred. No physical device action occurred.

Use one shared ecosystem project for core and mobile issues. Keep future commits
reviewable and update status only from evidence. Initial repo created via authorized
browser UI. Source population uses GitHub connector; no new credentials are needed.
Open ADRs and all blocking prerequisites are in ROADMAP.md and component docs.
