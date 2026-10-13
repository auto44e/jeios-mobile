# ADR 0001: Fresh JeiOS kernel on mobile

Date: 2026-10-13. Status: accepted owner direction.

The owner explicitly selected the fresh JeiOS kernel for the mobile scaffold,
with AOSP as a reference and future Android app layer throughout the ecosystem.
The preceding AOSP/Linux host proposal is superseded, not an alternate default.

One maintained C kernel core, shared architecture contracts and native service
APIs are the base. Bring up ARM64 in QEMU before Pixel hardware. Mobile adapts
presentation, power and device services without changing identity or security
semantics. Android compatibility is a separately bounded subsystem for desktop
and mobile; ordinary Android containers do not remove Linux kernel dependencies.

Consequences: Pixel vendor Linux modules cannot be loaded into this kernel;
Android framework, ART/bionic, Binder and HAL expectations need real compatibility
work. Pixel support can be blocked by undocumented hardware/firmware. A native
phone is a long-term target, not an AOSP rebuild or a currently usable image.
No schedule, universal APK compatibility or platform certification is promised.
