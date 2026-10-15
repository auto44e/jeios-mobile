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

## Cryptographic relock: compatibility-layer responsibility

Owner clarification: 2026-10-14T20:15:24-04:00. The future AOSP-derived Android
compatibility layer must perform more lifecycle and recovery work than the native
SDK because existing Android apps are not written for JeiOS cryptographic relock.
This applies across desktop/mobile and all qualified host architectures. It is a
planned integration obligation, not a claim that Android runtime support exists.

The host owns lock policy, credential authentication, key eviction and final
enforcement. The compatibility manager adapts foreign lifecycle semantics; it
cannot veto relock, keep a hidden copy of user keys, or weaken host protection
to preserve app compatibility. Android callbacks alone do not establish cleanup.

### Required integration responsibilities

- Map Android users/profiles and app identities to native protected domains and
  scoped broker authority. Map credential-gated and intentionally boot-available
  data explicitly; do not automatically classify every Android background service
  as an exception. Prevent weaker storage classes from silently receiving protected
  content. Document unavoidable shared-runtime isolation limits.
- Coordinate framework/ART services, app lifecycle, task scheduling, Binder
  transactions, native/JNI processes and file/storage operations during relock.
  Attempt bounded graceful state saving where supported, then enforce cancellation
  or termination at the host deadline. Cover runtime/framework caches, app heaps,
  JIT/native allocations and shared buffers, not only app-private files.
- Revoke broker resources for graphics, audio, camera, sensors, clipboard, input,
  network and keystore operations. Quiesce DMA through native device brokers.
  Protect snapshots, recents thumbnails, notifications and compatibility logs.
  Stop domain-specific framework services or the entire compatibility domain when
  shared plaintext cannot be safely separated.
- Prefer application-supported persistence and framework task reconstruction.
  Investigate encrypted process/domain checkpointing only as a separately reviewed
  option with complete key, pointer, resource and restart contracts. Do not assume
  a saved heap can safely resume across runtime versions, devices or policy changes.
  Suspending a whole runtime while retaining plaintext does not meet relock.
- After host-authorized unlock, reconstruct the runtime/app task state, validate
  saved data, reopen storage and reacquire current native permissions and handles.
  Treat Binder objects, descriptors, GPU contexts and sockets as resources requiring
  explicit reconstruction or failure handling; never restore stale authority.
- Reconcile interrupted writes and external operations. Do not blindly replay
  messages, purchases, authentication requests or other side effects. Handle
  expired sessions and jobs visibly. Keep lock preparation bounded even if a
  foreign app crashes or ignores lifecycle callbacks.

### Compatibility and user experience

Aim for seamless task return without requiring changes to every Android app.
However, the layer cannot reconstruct unsaved state that an app never persisted
unless a separately qualified checkpoint mechanism preserves it. It cannot make
an arbitrary external operation replay-safe. Publish per-app/version/runtime
behavior: transparent restoration, restart with durable state, limited recovery
or unsupported. Clearly disclose work that may be lost before relying on that
profile; never promise universal seamless restoration from framework hooks alone.

Background exceptions for calls, alarms, notifications or playback must use
explicitly scoped data/services and host policy. Their presence means that data
is outside the relocked domain's coverage. An incompatible app does not silently
change the device's lock policy; offer a visible owner-authorized exception where
allowed, or stop the app/decline the unsupported feature.

### Planning and qualification gates

AC0 must include the relock dependency ledger and trust-boundary design before
choosing runtime architecture. AC1 tests lifecycle/resource probes; AC2 qualifies
real app/version combinations. Native M3 isolation, storage and device lifecycle,
and the cryptographic prerequisites remain mandatory dependencies.

Test Java and JNI/native apps, multiple profiles, shared framework services,
in-flight/nested Binder calls, foreground/background tasks, large dirty heaps,
low storage, malformed checkpoints, repeated relock, process death, network loss,
suspend/resume and GPU/device work. Verify host survivor progress, no accessible
protected keys/plaintext after completed relock, no authority revival and no
duplicate external side effects on unlock. Record exact builds and platforms.
Native implementation belongs in shared core/runtime components; this repository
owns Android integration planning and compatibility qualification.
