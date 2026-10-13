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
| Storage | Provisional ext4, scoped files, raw disk rights and format matrix | Flash/controller availability, mounted-range exclusivity and power-loss tests |
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
