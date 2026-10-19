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

## Ecosystem coding policy

Apply shared NASA/JPL-inspired risk profiles and JCS rules from the core
[coding-policy proposal](https://github.com/auto44e/jeios/blob/main/docs/CODING_STANDARD.md)
adopted through merged core PR #17. Classify mobile packaging, platform
integration and apps by authority/failure impact. Record rule evidence and
deviations; host validation is not native qualification. Core #19 tracks shared
enforcement. No existing-code conformity or NASA certification is claimed.

## External contributor assistance and evidence

Owner direction 2026-10-19: for contributors other than the owner, follow the
[contributor assistance and local verification guide](https://github.com/auto44e/jeios/blob/main/docs/CONTRIBUTOR_GUIDE.md). Offer a flexible
easy-to-hard assistance scale, adjustable mid-session. Fully guided mode includes
environment setup, high-level coding/OS explanations, and help making contributions
and decisions in plain language. Expert mode minimizes coaching, not obligations.
All levels follow the same guidance, coding standards, docs, tests and owner gates.
Reproduce applicable CI steps locally, add meaningful risk-based failure coverage,
and include exact environment/commands/results/logs and gaps in PRs. Never equate
blocked or skipped tests with success. This additional onboarding policy does not
impose a mode on the owner or waive existing project-wide rules.

At the easiest level, let contributors express goals and revisions in ordinary
conversation; translate that intent into code, tool actions, tests and PRs. Do not
require prior coding syntax or command-line knowledge. Use the
[getting-started guide](https://github.com/auto44e/jeios/blob/main/docs/GETTING_STARTED.md) and adapt detail mid-session. If tools are
unavailable, distinguish proposed help from actions actually performed.
