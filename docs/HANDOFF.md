# Mobile agent handoff

## Latest compatibility requirement — 2026-10-14T20:15:24-04:00

Owner expects the future AOSP-derived Android layer to carry additional crypto
relock/unlock adaptation for existing apps. Mobile ANDROID.md now specifies
framework/ART/Binder/JNI and native-resource coordination, bounded state saving,
domain teardown/restoration and app-specific qualification. Core ENCRYPTION.md
records host ownership of keys/policy and the compatibility boundary.
No hidden key retention or weaker host policy to keep a foreign app running.
Graceful restoration is a target; unsupported unsaved-state recovery is disclosed.

Planned only; no Android runtime or relock implementation added. Core M3a/mobile
MP0 remain next. No executable tests rerun for these documentation additions.
Changes remain on existing PR branches; no merge performed.


## Latest native-app requirement — 2026-10-14T20:12:45-04:00

Owner requires native JeiOS apps to gracefully handle cryptographic relock/unlock.
The shared ENCRYPTION.md now makes this an SDK/toolkit/application conformance
contract: protected drafts/checkpoints, bounded lifecycle events, OS-enforced
revocation, process reconstruction and fresh authority after unlock. Apps cannot
veto locking, and callback acknowledgement alone does not prove memory cleanup.
Interrupted external operations require reconciliation, not automatic replay.

Planned only; no API/runtime implementation added. Core M3a and mobile MP0 remain
next. Documentation structure/whitespace checked; no executable tests rerun.
This update stays on existing PR branches, with no merge performed.


## Latest requirement — 2026-10-14T20:08:17-04:00

Owner wants ordinary device/session locking to support cryptographic relock:
withdraw protected user-domain keys and plaintext access to regain a defined
pre-first-unlock-like state without reboot. Shared core ENCRYPTION.md specifies
proposed lock profiles, key/lifecycle/DMA cleanup, strong-credential reopening,
background-service exceptions, failure handling and acceptance gates.
This is an ecosystem-wide requirement, including mobile and compatibility apps.
No universal reboot equivalence or implemented encryption is claimed.

Planning only; core M3a and mobile MP0 remain next. Added prose was checked for
whitespace/conflict markers; reference URLs came from retrieved official Apple/AOSP
documentation. No kernel/build/emulator tests were rerun. Existing documentation
PR branches are updated; no merge is performed.


## Latest scope clarification — 2026-10-14T19:59:09-04:00

The approachable-defaults/deep-control philosophy applies to the entire OS and
ecosystem, not just security. DESIGN.md now records it as the overall product
vision across UI, apps, hardware, storage/networking, media, performance/power,
services, identity/sync, updates and developer workflows. Per-area presets and
expert controls are composable; UI detail, functionality, permissions and hardware
support stay distinct. Security is one application of this broader philosophy.
Earlier security-specific notes remain valid within that scope.

Documentation only; core M3a and mobile MP0 remain next. No runtime capabilities
or new test execution are claimed. This updates the existing review branches;
no merge is performed. Added prose checked for whitespace/conflict markers;
no new links or executable changes.


## Latest requirements clarification — 2026-10-14T19:55:55-04:00

Owner requires seamless everyday security plus granular power-user/developer and
company policy control, spanning deliberate permissive experimentation through
highly restricted deployments. The shared zero-trust proposal now distinguishes
UI complexity, security policy and hardware assurance; defines proposed profiles,
scoped exceptions, GUI/CLI/API parity, visible managed policy and honest restoration
limits. Profile names/settings are proposals. No runtime enforcement was added.
M3a and mobile MP0 remain next. This clarification updates existing documentation
PRs (core #12, mobile #6); no merge is performed by this update.

Validation: new Markdown structure, whitespace and conflict-marker checks passed.
No new links were introduced. Build/emulator tests were not rerun for this
documentation-only clarification; prior evidence remains at its recorded commits.


## Current status — observed 2026-10-14T23:50:13.156Z

Inspected main: `55505743500809b5714a725cb23e155a569791b1`. No pre-existing mobile PRs
were returned. Planning/scaffold only; MP0 remains next. No ARM64, Pixel or Android
execution is claimed. This documentation update will have a separate unmerged PR.
Core PR #11 merged 2026-10-13T23:10:59Z at
`e897e02f9038e164efbb590cfc0229e8300bff54`; the pinned implementation dependency is unchanged.

Owner requirement 2026-10-14: ecosystem-wide
[zero trust](https://github.com/auto44e/jeios/blob/docs/zero-trust-status-20261014/docs/ZERO_TRUST.md).
Qualify core enforcement on ARM64 at MP3; apply broker, device, Android and remote
peer rules at MP6/AC/SEC. No implicit trust from pairing, Android UID/root, stock
app status or device branding. Offline revocation and recovery need explicit tests.
This is planned design, not a completed mobile security feature. The core proposal
link targets its companion review branch until merged; then use core main.

## Status refresh and historical records

Owner preference recorded 2026-10-14: retain detailed timestamped history alongside
a clearly labeled current status. Every refresher must record an ISO-8601
observation time with timezone, repository/branch and exact inspected commit,
implemented/tested/planned/blocked states, PR/issue state, evidence and next task.
Separate an event's timestamp from the time it was verified. If an old record has
only a date, preserve that precision; never invent a time. Keep superseded plans
and previous failures as labeled history with links to their replacements.

Current status takes precedence over historical branch names or open/closed
wording. Preserve previous test results at their original commit and environment;
do not present them as rerun or current-head CI. State unverified items explicitly.
Use enough detail for an agent to resume without reconstructing the conversation.

## Historical scaffold checkpoint — 2026-10-13

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
