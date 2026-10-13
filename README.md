# JeiOS Mobile

Mobile platform planning and integration for the **fresh C JeiOS kernel**.
The same core serves desktop, mobile and other qualified device profiles.
**AOSP is a reference and a future Android application compatibility layer;
it is not the mobile host OS or a replacement Linux kernel.**

Status: architecture/scaffold only. No ARM64 kernel boot, Pixel image, mobile UI
or Android runtime exists here yet. The shared core has an AMD64 M1/M2 prototype.

## Start here

- [Agent handoff](docs/HANDOFF.md) and [AGENTS.md](AGENTS.md)
- [Architecture and ownership](docs/DESIGN.md)
- [ARM64 port contracts](docs/ARM64.md)
- [Pixel feasibility and recovery](docs/PIXEL.md)
- [Android compatibility across the ecosystem](docs/ANDROID.md)
- [Capability parity matrix](docs/PARITY.md)
- [Gated roadmap](docs/ROADMAP.md)
- [Decision: fresh kernel first](docs/adr/0001-fresh-kernel-mobile.md)

First execution target: QEMU ARM64 `virt` (exact version/profile to qualify).
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
