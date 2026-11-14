# Xcode workspace for jeios-mobile

Open `JeiOSMobile.xcodeproj` on a Mac with Xcode (Xcode 15 or later recommended).
Choose a shared scheme and use **Product > Build / Command-B**. These are external
build targets, not macOS/iOS app targets. Run, Archive and XCTest are not configured;
there is no automatic simulator, signing, flashing or kernel debugger attachment.
Use the report navigator for command output and the existing CLI/QEMU workflows
for execution/debugging. Scheme names: validate, test, plan.

Install Python 3 and ensure `python3` is on PATH. Schemes run the existing
validator, unittest suite or target planner; none boot or package a device.

The wrapper adds standard Homebrew/Docker CLI locations to PATH because GUI Xcode
may not inherit your terminal environment. Missing dependencies fail visibly.
Paths are relative to the checkout, including locations containing spaces.

The navigator lists tracked source/docs/configuration as normal groups. After
adding/removing files run `python3 tools/generate_xcode.py`, then commit the project
changes. No generated build products or per-user Xcode settings belong in git.
No native compile target is added: navigation/editing is supported, but accurate
compiler-driven indexing/completion is not promised for external Linux builds.

Validation on the authoring Linux host covers plist/XML structure, stable target
IDs, scheme references and task commands. Xcode opening, `xcodebuild -list` and
Command-B on Intel/Apple Silicon Macs still need real Mac validation. On a Mac:

```sh
plutil -lint *.xcodeproj/project.pbxproj
xcodebuild -list -project JeiOSMobile.xcodeproj
```

The projects are developer convenience tooling, not OS/platform qualification.
