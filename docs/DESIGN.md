# Fresh-kernel mobile architecture

Status: planning only, 2026-10-13. ADR 0001 records the owner's chosen direction.

## Repository and component ownership

`auto44e/jeios` owns the fresh C kernel, native object/IPC/syscall contracts,
architecture ports and generally reusable drivers/services. `jeios-mobile` owns
mobile integration plans, platform manifests, future packaging, reference mobile
shell policy and hardware/parity qualification. Do not duplicate kernel sources
or modify a dependency checkout invisibly. Propose core changes upstream, then
advance config/core.json to a reviewed commit with evidence. The current pin is
an AMD64 foundation, not ARM64-ready. Cross-repo version changes need integration
tests and explicit compatibility ranges; a moving branch is not a reproducible pin.

Boot chain: platform firmware/loader -> JeiOS ARM64 entry -> MMU/exceptions/timer
and allocator -> native isolated services -> mobile shell/application SDK. Device
services mediate touch, display, sensors, camera, audio, modem and networking.
The future Android compatibility service is a client of native brokers and does
not become the owner of the host OS. Graphics, files, keys and sensors retain the
same host capability checks regardless of the calling application framework.

## Shared core versus mobile policy

Reuse the object model, checked IPC, allocator abstractions, storage semantics,
identity and E2E protocols. Separate platform-dependent MMIO, interrupts, DMA,
cache management and power operations behind explicit contracts. Mobile profiles
select resource budgets and service activation, not weaker permissions. Memory
pressure, thermal limits and battery policy require measured graceful degradation.
Raw device privileges and low-level controls remain possible only through explicit
scoped authorization; near parity does not mean every app gets a block device.

AOSP informs framework design and future compatibility mapping: package identity,
permissions, lifecycle, Binder/AIDL, ART, media/camera integration and testing.
Every borrowed component needs exact provenance and independent license review.
AOSP API behavior is not a hardware driver specification or an entitlement to
Google proprietary services. Original additions use Apache-2.0; Linux/GPL code,
firmware, SDKs and AOSP subprojects retain their own terms.

## Trust and failure model

Keep boot ownership, user identity, device enrollment and app rights separate.
Native phone services and compatibility processes receive minimal grants. Treat
firmware/device DMA and imported runtime parsers as untrusted surfaces requiring
qualified containment. Neither Pixel hardware branding nor AOSP familiarity
proves a driver, keystore or boot trust chain works under JeiOS.

Do not translate Android UID/root assumptions into native ambient authority.
Fatal kernel corruption remains fatal; an app or compatibility-service crash must
be contained. Core process isolation must exist before untrusted runtimes. Thermal
shutdown, modem failure, no entropy and invalid key state need defined outcomes.
A prototype cannot claim safe emergency calling, suspend or recovery without
physical validation. No personal accounts or secrets belong on bring-up images.

## Ownership/lifetime and API decisions before implementation

Specify request ownership, bounded buffers, cancellation completion, generation
revocation and device detach for every broker. A timeout cannot free a buffer
still referenced by DMA. Define lock order and interrupt context; avoid blocking
IPC or allocations in hard IRQ handlers. Only qualified architectures may enable
SIMD, PAC/BTI/MTE or accelerator state; capability detection must include OS context
support. Zero reused pages before cross-principal exposure.

Protocol versions must advertise unavailable capabilities explicitly. Do not
silently route work to another device or cloud to claim local parity. Persistent
formats require interruption/recovery tests. Signing and enrollment keys are
provided outside source control under an owner-managed release process.

## Immediate decision backlog

ARM64 boot entry/EL and DTB contract; core HAL boundary; page-table geometry;
interrupt/FP-state handling; native service ABI; Pixel boot/firmware feasibility;
Android compatibility implementation choice; reproducible toolchain; security and
power budgets. ARM64 proof and Pixel research may proceed independently, but
userspace services depend on core M3 handle/process/IPC boundaries. No milestone
is complete merely because another architecture's tests passed.
