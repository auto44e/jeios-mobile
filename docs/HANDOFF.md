# Mobile agent handoff

## Contributor guidance refresh — observed 2026-10-19T11:09:52+00:00

Inspected jeios-mobile main at `d790d2f48a9a9f3093f412d9fabed2952974f7c0`. Owner requested additional
guidance for other contributors: expansive risk-based local CI/testing, PR result
data and an easy-to-hard assistance scale adjustable even mid-session. Added
contributor/agent guidance and a PR evidence template; core holds the shared guide.
Easy mode includes setup, plain-language OS/coding explanations and contribution/
decision walkthroughs; hard mode still follows all standards, docs and gates.
Owner clarification: fully guided contributors can work through natural
plain-English conversation without prior code/terminal/Git syntax knowledge.
Added a shared development getting-started guide with conversational and manual
paths, setup/build/test/PR steps and a mobile entry point.
This is documentation only, not new CI enforcement, runtime support or an owner
onboarding requirement. Existing milestone status and owner gates are unchanged.

Local verification on this docs-only patch over the inspected revision:
`python3 tools/validate.py`, `python3 tools/target_plan.py` and
`python3 -m unittest discover -s tests -v` passed (four tests; planning only).
Changed Markdown links and `git diff --check` checked before publication.
No emulator rerun for docs/template changes; no new-head remote CI result claimed
here. Next: review/merge the guidance; implementation priorities remain #52/#53/#54
and mobile #2. CI automation/enforcement remains core #18/#19.

## Current phase refresh — observed 2026-10-19T10:44:37+00:00

Inspected `auto44e/jeios-mobile` main `c7b42cd8a575fafc67c7a8e7742218dee3981e83` and core main
`11a02adf744874328371b7f9f3bc801623995980`. Mobile PRs #8/#9 and core #51 are merged; no open PRs
at initial inspection. MP0 issue #1 is closed/Done. Mobile #2 remains open and
partially implemented (MP1 entry/console/vectors in shared core); MP2/MP3 planned.

Implemented/tested upstream: AMD64 M3 complete; ARM64 early boot and EL1 exception
vectors locally demonstrated in QEMU. Mobile validation is planning-only: observed
remote run 39072964571 passed at the inspected mobile SHA; core run 39237040923
passed at its SHA. Remote ARM boot tests remain absent. No Pixel/mobile UI/Android
runtime support is claimed. `config/core.json` still pins the M1/M2 foundation;
advancing that pin/schema requires separate integration evidence and review.

Next bounded task: core #52 DTB parsing and remote boot CI, followed by MP2/MP3
under mobile #2. Core #53 M4 services/devices and #54 read-only M5a implement the
[shared next phase](https://github.com/auto44e/jeios/blob/main/docs/NEXT_PHASE.md).
Cross-device parity and #7 F2FS qualification remain later tracked work. This is
a documentation/status update; no runtime/configuration or frozen ADR edits.
Earlier evidence and dated decisions below are historical; this block supersedes
their open/closed/current-priority wording.


Local verification for this docs-only refresh: `python3 tools/validate.py`,
`python3 tools/target_plan.py` and `python3 -m unittest discover -s tests -v`
passed (four tests). The planner describes the intentionally unchanged old pin;
it does not negate newer upstream ARM boot evidence. No emulator rerun.
Relative Markdown links and `git diff --check` passed.
Project board verified core #52/#53/#54 and #18/#19 as Todo; mobile #2 as
In Progress. Current overview updated while preserving its earlier history.

## Ecosystem coding-policy refresh — observed 2026-10-17T00:12:28+00:00

Owner direction: 2026-10-16T20:01:26-04:00, reaffirmed
2026-10-16T20:08:52-04:00. Inspected `auto44e/jeios-mobile` branch
`docs/posix-ldap-20261016` at `b2ab0f0a75cc6e8902408eb222474de592adfdc5`.
Core PR #17 and mobile PR #8 were observed open/unmerged. This update extends
PR #8; core #19 is open for policy audit/enforcement alongside CI #18.
No board membership or reviewer assignment is claimed.

Implemented: documentation policy and contributor guidance only; runtime remains
core M1/M2 AMD64 and mobile planning scaffold. Planned: ecosystem-wide NASA/JPL-
inspired rules, risk profiles, baseline audit and staged automated enforcement.
Blocked/unverified: no complete existing-code audit, independent review or NASA
certification; no new analyzer/workflow or native mobile qualification.
Core CODING_STANDARD.md is the shared proposal in PR #17; mobile references it.
Next: core M3a and mobile MP0, with bounded #19/#18 enforcement work alongside.

Validation: `python3 tools/validate.py`, `python3 tools/target_plan.py` and `python3 -m unittest discover -s tests -v` passed (four tests). These validate planning only.
Documentation links, conflict markers and `git diff --check` checked separately
before publication. No emulator rerun for documentation-only edits. New-head
remote CI must be observed separately. Historical evidence below retains its
original revision/time; this entry supersedes earlier current-status wording.

## Current refresh — observed 2026-10-16T23:08:34+00:00

Inspected `auto44e/jeios-mobile` main at `79b3565a3049862c16d4696cd6ada233e03523da`.
Mobile #6 merged 2026-10-15T00:46:30Z.
No open PRs existed in either repository at initial inspection. This update uses
`docs/posix-ldap-20261016` and will be submitted as an unmerged review PR.
Mobile #1-#5 and #7 open; parity #5 carries the new requirements.

Implemented: core M1/M2 AMD64 foundation; mobile planning/manifest scaffold only.
Planned: POSIX.1-2024 and built-in LDAPv3 are now core requirements, owner decision
2026-10-16T19:04:18-04:00. Organizational enrollment remains optional.
Blocked: native POSIX/directory runtime awaits isolation, services, storage,
networking and security prerequisites; mobile also awaits ARM64 qualification.
Next bounded tasks remain core M3a (#2 contracts first) and mobile MP0 (#1).
New standards ADR/qualification planning can proceed without claiming runtime work.

Preserve all historical decisions below, including immutability/off switch,
versioned updates independent of immutability, F2FS selection, crypto relock,
zero trust, customization, Android planning, multitouch and hardware MFA.
Earlier references to then-open PRs or candidate-only LDAP are historical.
Mobile `python3 tools/validate.py`, `python3 tools/target_plan.py` and
`python3 -m unittest discover -s tests -v` passed (four tests).
The pinned core implementation revision remains unchanged.
Relative Markdown targets, whitespace and conflict-marker checks passed.
GitHub CI for the new PR head is separate from local results.
Project board verified: new core #15 and #16 are present as Todo; prior merged
PRs are Done. Refreshed stale core #2-#9 baseline guidance and mobile #5 parity.
No boot behavior changes; no emulator/device tests or POSIX/LDAP runtime tests claimed.


## F2FS approval and agent tasks — 2026-10-14T20:43:47-04:00

Owner approved F2FS as the provisional mobile default, subject to actual JeiOS
qualification. This supersedes earlier candidate-only wording; device support,
feature flags and production readiness are not implied. Btrfs/OpenZFS remain
long-term default targets; ext4 remains the initial core bring-up backend.

Ready-to-start bounded work:
- [Core #13](https://github.com/auto44e/jeios/issues/13): backend contract ADR,
  hosted fake-block-device and conformance harness.
- [Core #14](https://github.com/auto44e/jeios/issues/14): F2FS format/provenance
  review and bounded read-only hosted metadata probe with negative tests.
- [Mobile #7](https://github.com/auto44e/jeios-mobile/issues/7): mobile F2FS
  workload/qualification profile and shared-backend integration plan.

These issues are open/unassigned at creation; no coding agent has been launched
by creating them and project-board membership has not been verified. Hosted
prototypes can proceed independently while runtime integration waits for M3/M4/M5
and relevant mobile execution/driver gates. No writes to real user media.
M3a remains the next core kernel gate; MP0 remains the mobile architecture gate.


## Latest storage decision — 2026-10-14T20:40:22-04:00

Owner selected multiple first-class long-term default backends: Btrfs, OpenZFS
and a suitable mobile filesystem. F2FS is the proposed mobile candidate; suggested
profile assignments remain subject to qualification. Native APIs provide coherent
workflows, with backend-specific capabilities and tested guarantees. Owner-provided
system defaults are supported through explicit interfaces, boot/recovery contracts
and honest experimental profiles. Changing defaults is not an in-place conversion.

Shared STORAGE.md records scope and staged gates. ext4 remains initial bring-up;
core M3a/mobile MP0 remain next. Documentation-only decision; no filesystem,
migration tool or plugin runtime was added. New text checked for whitespace and
conflict markers; no executable tests rerun. No merge performed.


## Latest owner decision — 2026-10-14T20:30:05-04:00

Protected/versioned system deployments are the seamless default, with full
customization and an authorized immutability off switch. OS and built-in-app
forward updates/rollback must remain intuitive and available independently of
write protection. Shared STORAGE.md specifies native lifecycle/schema contracts,
mutable-mode change handling, retained versions, coherent activation and recovery.
Data migration and trust/anti-rollback limits remain explicit; no promise that
arbitrary direct edits or external effects can be automatically reversed.

Planning only; no update manager, filesystem or native app runtime was added.
Core M3a/mobile MP0 remain next; reserve storage/update contracts before M5 format
freeze. Documentation whitespace/conflict-marker checks only; runtime tests
not rerun. Existing PR branches updated; no merge performed.


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


## Historical status — observed 2026-10-14T23:50:13.156Z

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
