# Ecosystem capability parity

Owner goal: near 1:1 functionality across device types within reason. Share rights,
data formats, service contracts and outcomes; adapt UI, scheduling and hardware
paths. A phone does not become a desktop by silently weakening its security.
All capabilities below are planned in mobile; do not confuse a spec with support.

| Area | Shared contract | Mobile qualification / explicit exception |
| --- | --- | --- |
| Identity/family/multi-user | Local-only login, independent principals, explicit sharing and recovery | Lock/background key residency, memory budgets and phone session UI |
| E2E/PQ sync and nearby sharing | Same recipients, epochs, revocation, consent and conflicts | Radio/power budgets; never silently downgrade crypto |
| Domains/fleets | Mixed Windows/macOS/Linux interoperability and policy inspection | Native mobile policy adapters, offline behavior and managed-device trust |
| Input/customization | Multitouch touchscreens/trackpads, accessibility, good defaults and deep configuration | Touch targets, rotation, external input/display support; no gesture-only recovery |
| MFA | Hardware keys, verified factors, backup/recovery | USB/NFC drivers and secure UI; preboot qualification separate |
| Storage | Shared backends; ext4 initial bring-up, Btrfs/OpenZFS long-term targets, F2FS provisional mobile default | F2FS qualification (#7), controller availability, scoped raw access and power-loss tests |
| GPU/NPU/media | Open standards, conservative configurable offload, CPU fallback, media integration goals | Driver/thermal/SDK feasibility; no universal accelerator or BRAW availability |
| Init/services | Configurable lifecycle, bounded restart and explainable effective policy | Suspend/wake and battery-aware service admission |
| Android apps | Common optional compatibility layer and security semantics | ABI/features per app; same layer applies to desktop and qualified IoT profiles |
| Updates/privacy | Owner trust, recoverable updates, minimal local diagnostics | Pixel boot/firmware and irreversible rollback constraints |

At runtime expose capability ID/version, supported operations, limits, reason for
unavailability, security prerequisites and local/remote execution location. Remote
offload needs an explicit grant and is never disguised as local capability.
Interoperability tests cover native-native, native-mobile and Android-adapted
clients, including negative permission, recovery and offline cases. Unsupported
functions remain discoverable with clear explanation rather than disappearing
behind UI complexity presets.

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
