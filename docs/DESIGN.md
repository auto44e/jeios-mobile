# Fresh-kernel mobile architecture

## Overall product vision: approachable defaults, deep owner control

Owner clarification: 2026-10-14T19:59:09-04:00. This philosophy governs the
entire JeiOS OS/ecosystem, not only security. Everyday users should have a coherent,
seamless and intuitive experience without needing to understand implementation
details. Power users, developers and organizations should be able to progressively
inspect, customize, automate, replace and administer supported components in depth.

Apply this to installation/onboarding, desktop and mobile interaction, themes and
window management, accessibility, apps and compatibility, files/storage, networking,
identity/sync, privacy/security, hardware/drivers, audio/media, CPU/GPU/NPU resource
policy, power/performance, init/services, updates/recovery and developer tools.
Good defaults must be complete useful workflows, not a deliberately limited edition.
Advanced controls must be discoverable, documented and supported interfaces rather
than requiring undocumented patches for ordinary customization.

Presets are starting points, not rigid user classes or one global slider.
Allow per-area complexity and configuration: expert audio with simple networking,
a custom shell with stock updates, or deep developer tools with hardened security.
Separate presentation detail, functional configuration, administrative authority,
security policy and hardware capability. Changing one must not silently change
the others. Explicit authorized policy changes remain available to owners within
the device/workspace's disclosed management boundaries.

Provide simple task-oriented UI with progressive disclosure, searchable settings,
plain explanations and accessible input. Expose appropriate advanced configuration
through GUI, CLI and documented APIs with equivalent policy enforcement; not every
low-level operation needs a prominent everyday screen. Versioned configuration,
validation, dry runs where useful, export/import, automation and effective-setting
inspection should make complex setups reproducible. Explain dependencies and
tradeoffs instead of silently ignoring unsupported settings.

Support a spectrum from stock, mostly automatic experiences to deeply customized,
experimental ("YOLO"), finely tuned and tightly controlled deployments. These are
composable choices, not a ranking where more restriction or more complexity is
always better. The authorized owner chooses the balance; organizations can define
and disclose policy for the devices/workspaces they manage.

Prefer scoped changes, previews and reversible transactions where feasible.
Clearly identify destructive, irreversible or system-wide effects. Recovery should
offer a known-good usable environment without needlessly discarding customization.
A reset-to-defaults action must identify affected data/settings and cannot promise
to undo prior data loss or compromise. Do not mistake customizability for a promise
that every component is hot-swappable or every hardware feature exists.

Carry coherent concepts, configuration semantics and workflows across desktop,
mobile, IoT and future device types, adapting interaction to screen, input, power
and hardware. Aim for functional parity where practical; publish explicit support
differences and fallbacks. Cloud accounts and vendor services must not be mandatory
merely to access ordinary local use or expert controls.

Acceptance must cover both audiences: ordinary end-to-end tasks with sensible
defaults and little friction, and documented advanced workflows with predictable
results, configuration portability, accessible explanations and tested recovery.
Qualify each subsystem as it is implemented. This is an accepted product direction,
not evidence that any future UI, service, API or parity target already exists.


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
