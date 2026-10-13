# Future Android application layer across JeiOS devices

Status: research plan; no APK execution, ART port, Linux ABI or Android services
implemented. Applies to desktop and mobile, not only Pixel hardware.

## Architecture choice to investigate

Primary direction: an isolated compatibility domain above the native JeiOS kernel,
with narrow native brokers for display, input, files, network, audio, sensors and
keys. Android processes retain distinct host security identities. The compatibility
manager cannot equate Android root, Binder identity or permissions with host-wide
rights. AOSP is a behavioral/source reference after license review.

| Approach | What it entails | Planning disposition |
| --- | --- | --- |
| Rehost selected ART/framework components with native adapters | Port OS abstractions and specified ABI behavior; build a maintained runtime subset | Preferred investigation, not proven feasibility |
| Linux syscall/Android ABI personality | Implement and test a bounded Linux-like ABI on JeiOS plus Binder semantics | Candidate if needed; avoid turning every ioctl into kernel privilege |
| Linux/Android VM guest | Hypervisor/device model and guest maintenance; apps remain guest-bound | Optional future separate experiment, not the chosen mobile kernel or default deliverable |
| Ordinary Android container | Relies on host kernel interfaces/namespaces/drivers | Not a ready-made solution on a fresh non-Linux kernel |

Record results in an ADR after minimal experiments. A full APK needs much more
than a JVM: ART/DEX, bionic/native linker, process/thread/futex/signal semantics,
Binder, framework services, resources/package management and graphics can all
matter. Public API compatibility, native ABI compatibility and application behavior
are separate claims. No general 'all APKs' promise.

## Dependency ledger and staged probes

1. Native kernel prerequisites: stable checked process/memory/IPC ABI, timers,
   synchronization, files, secure entropy and qualified FP/SIMD state on each ISA.
2. Small libc/native probe: loader, TLS, mmap/mprotect, thread/futex/clock behavior,
   descriptor lifetime and cancellation. List actual required syscalls before
   implementation; no universal Linux syscall claim from hello-world.
3. Binder/AIDL probe: typed objects, caller identity, transaction size, one-way
   queues, handle transfer, reference/death lifecycle, nested calls and reentrancy.
   Bound memory and work; malformed transactions cannot corrupt native services.
4. ART/headless DEX probe: runtime memory mappings, GC/thread safepoints, exceptions,
   signals/JIT W^X and stack unwinding. JIT authority is explicit, never global RWX.
5. Framework/package probe: verified package identity, permission and lifecycle
   mapping, activities/services, resource loading and bounded package parsing.
6. Graphics/input/audio probe: compositor surfaces, buffer ownership/fences, touch,
   keyboard, accessibility, media and audio focus. No shared unscoped device FD.
7. Curated app set: pin APK version/license/ABI/features and expected behaviors;
   test denial/revocation, process death, sleep/resume and upgrades across devices.

Order is dependency-driven; some probes iterate. Implement shared functionality
in core/runtime projects where appropriate, with mobile integration tests here.
Do not advertise native Android HAL compatibility until the kernel/ABI assumptions
of each HAL are actually implemented. Vendor components are independently reviewed.

## Security and ecosystem parity

Map permissions per operation, including existing resources after revocation.
Binder caller provenance must survive forwarding; never accept a caller-supplied
UID as proof. App storage remains isolated, scoped file pickers grant limited
access, and account/key brokers never export ordinary hardware private keys.
Imported SELinux userspace does not make native enforcement equivalent; specify
and test every host-side boundary. Android domain failure must preserve native
apps and the recovery UI. Quotas prevent Binder/runtime denial of service.

ARM64-only native libraries do not run directly on AMD64. Either select APKs with
a matching ABI, rebuild with permission, or separately qualify binary translation;
no transparent architecture portability promise. Optional Google Play/GMS,
proprietary DRM, integrity attestation and vendor APIs are independent availability,
licensing and compatibility questions. Do not fabricate successful attestation.

AOSP Cuttlefish can serve as an external behavioral reference lab later; it is
not the JeiOS boot target. Conformance-style tests must name reference versions
and divergence. Upstream Android changes require ongoing maintenance; a one-time
port is not perpetual compatibility. No test runner/certification claims yet.

Primary references reviewed 2026-10-13:
- https://source.android.com/docs/core/architecture
- https://source.android.com/docs/core/architecture/ipc/binder-overview
