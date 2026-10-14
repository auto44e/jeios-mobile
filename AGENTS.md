# Agent instructions: JeiOS Mobile

Read README.md and docs/HANDOFF.md, DESIGN.md, ARM64.md, ANDROID.md and ROADMAP.md.
The owner explicitly chose the fresh C JeiOS kernel for mobile on 2026-10-13.
This supersedes the earlier AOSP/Linux bring-up proposal in core PR #11 history.
Do not switch to an Android/Linux host, GSI, custom ROM or Linux VM guest as a
substitute for delivering the native port without a new owner decision.

Kernel code belongs in auto44e/jeios; submit shared ARM64/driver changes there.
This repository owns mobile integration, target metadata, packaging and parity
qualification. Pin reviewed core commits and never fork another kernel copy.
C11 core plus necessary architecture assembly; future imported Android components
retain their upstream languages and licenses after provenance review.

Work one gate at a time. Separate implemented/tested/planned/blocked. Fail closed
on unsupported hardware or guarantees. Do not invent drivers, ABI support, lunch
products, cryptography, compatibility certification or successful boot evidence.
No actual device unlock, flash, wipe, relock or key provisioning is authorized by
this planning task. Keep private keys/blobs/build outputs out of git.

Run validation and meaningful tests. Update handoff, roadmap and references with
exact commands/evidence and next bounded task. New boot code requires emulator
execution and failure tests; host config tests cannot qualify it. Use small
reviewable branches/PRs. Do not merge or assign reviewers unless requested.

Initial original scaffold may be committed to the newly created main. Subsequent
implementation uses reviewable PRs. Follow core AGENTS.md for changes there.

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
