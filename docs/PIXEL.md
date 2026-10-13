# Pixel feasibility: fresh kernel, not a custom Android ROM

Status: research candidates only. Pixel 9 base (`tokay`) is first; Pixel 10 base
(`frankel`) is second. Pro/XL/Fold variants require separate records. No phone was
unlocked, flashed, relocked or tested. Fresh JeiOS uses no Android lunch product.

## What existing Android material can and cannot establish

Google publishes device codenames and Android boot-image format guidance. Those
help inventory boot packaging but do not prove the bootloader accepts a JeiOS
payload or that peripherals are usable. Android vendor Linux modules are not
binary-compatible with the fresh kernel; userspace HAL blobs also depend on OS,
ABI and device behavior. A proprietary binary is neither source nor an automatic
right to redistribute it. Historical AOSP/vendor build pairings are references,
not a shortcut to a current secure native phone.

## MP4 feasibility record (before touching hardware)

For each exact SKU/firmware: establish owner unlockability, boot chain and image
headers, DTB/DTBO provenance, entry EL/register convention, RAM/reservations,
rollback indexes, firmware dependencies and reliable recovery access. Identify
which steps erase data and what the current anti-rollback policy permits. Do
not offer a generic flash command or relock recipe. Obtain explicit device action
authorization only after a concrete tested plan exists.

Create a driver evidence matrix:

| Area | Required evidence | Go/no-go consequence |
| --- | --- | --- |
| Earliest output | Accessible UART or independently qualified framebuffer/USB diagnostic path | Cannot diagnose native entry reliably without an output plan |
| CPU/MMU/timer/GIC | Documented register/topology/firmware handoff | QEMU constants cannot be reused blindly |
| Storage and boot partitions | Controller, firmware, DMA and recovery behavior | No writable storage before containment and power-loss plan |
| Display/touch | Panel/link/controller initialization, calibration and input reports | No mobile UI claim from kernel entry alone |
| USB/network/radios | Controller/PHY/firmware protocols, interrupts and DMA isolation | Driver boundaries required before untrusted peripherals |
| GPU/NPU | Documented submission/memory/reset model or licensed feasible implementation | Software fallback only where actual display/CPU path works |
| Modem/audio/camera | Transport, firmware/HAL dependencies and isolation | No telephony/emergency/camera claims without physical evidence |
| Power/thermal/charging | PMIC, regulators, battery sensors, thermal shutdown, suspend/wake | Unsupported behavior blocks daily-use, not just battery optimization |
| Keys and boot trust | Secure-world interface, entropy, owner trust keys, update/recovery | Android's existing keystore support is not inherited |

Each row records source/revision/license, known facts, unknowns, attack boundary,
owner, bounded next experiment and test evidence. Do not probe undocumented MMIO
on hardware without a controlled plan. Preserve radio/thermal safety firmware.
When a critical interface is unavailable, mark blocked and continue the virtual
port; do not silently switch the mobile host to Linux to remove the obstacle.
A documented ARM development board may be a secondary engineering platform,
but it does not qualify the requested Pixel target.

## MP5 physical execution sequence

Only after MP1-MP3 and MP4 go/no-go: recovery rehearsal -> native entry diagnostic
-> validated RAM/MMU/timer -> read-only storage -> display/touch -> isolated device
services -> power/thermal -> updates/trust -> full workload matrix. Flashing and
relocking are separately authorized operations. Never relock an unverified image.
Signed packages and factory recovery material remain out of git where terms or
secrets require it. A demo boot is not a safe phone; publish exact support gaps.

Primary references reviewed 2026-10-13:
- https://source.android.com/docs/setup/reference/build-numbers
- https://source.android.com/docs/core/architecture/bootloader/boot-image-header
- https://source.android.com/docs/setup/build/building-pixel-kernels
- https://developers.google.com/android/drivers
