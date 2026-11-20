# Control software: operation, defect detection and recovery

By Srinivas Reddy Mudem.

## Scope

Recorded local compiled PLC/C execution with simulated encoder inputs and modeled drive output. This page does not execute C remotely. No physical hardware validation, safety certification, or ARM secure boot claim. Independent educational design, not TK Elevator’s controller architecture.

## Engineering contribution

Integrated PLC sequencing, embedded C speed supervision, deterministic inputs, automated tests, host-side signature verification and traceable evidence.

## Component responsibilities

PLC: Start/Stop/Reset sequencing and controller acknowledgment. C: speed calculation, fault supervision, drive request. Encoder: simulated shaft pulses directly to C. Drive: visualization of C output.

## Operating walkthrough

### 1 · Start is requested

The operator presses Start. The PLC passes the request to the C controller, which enables the drive request and waits for speed feedback.

The system is starting; normal running has not been confirmed yet.

Observed: state=STARTING; fault=NONE; speed=0.0 rpm; drive_request=True; simulated_ms=100; comparison_passed=True.

### 2 · Normal operation is confirmed

The encoder input represents 300 rpm. C checks the measured speed and confirms Running to the PLC.

The speed is below the 600 rpm demonstration limit, so the drive request remains ON.

Observed: state=RUNNING; fault=NONE; speed=300.0 rpm; drive_request=True; simulated_ms=200; comparison_passed=True.

### 3 · Excessive speed triggers protection

The simulated encoder now represents 900 rpm. C detects overspeed, latches a fault and switches the drive request OFF.

Protection worked: the software requested a stop. Physical braking is not modeled.

Observed: state=FAULT; fault=OVERSPEED; speed=900.0 rpm; drive_request=False; simulated_ms=300; comparison_passed=True.

### 4 · The input is restored—but the drive stays off

A valid stationary encoder sample is supplied. The immediate overspeed condition is gone, but the recorded fault is still latched.

Removing the cause must not automatically restart the drive.

Observed: state=FAULT; fault=OVERSPEED; speed=0.0 rpm; drive_request=False; simulated_ms=400; comparison_passed=True.

### 5 · A premature restart is blocked

Start is requested again without resetting the fault. The PLC/C interaction keeps the drive request OFF.

The operator must deliberately clear the fault before requesting a new start.

Observed: state=FAULT; fault=OVERSPEED; speed=0.0 rpm; drive_request=False; simulated_ms=500; comparison_passed=True.

### 6 · Reset clears the fault

With valid stationary feedback, Reset returns the controller to Ready. The drive request remains OFF.

Reset clears the fault; it is not a command to start moving.

Observed: state=READY; fault=NONE; speed=0.0 rpm; drive_request=False; simulated_ms=600; comparison_passed=True.

### 7 · A separate Start begins recovery

The operator makes a fresh Start request. The controller enables the drive request and waits for new speed feedback.

Recovery follows an explicit Reset → Start sequence.

Observed: state=STARTING; fault=NONE; speed=0.0 rpm; drive_request=True; simulated_ms=700; comparison_passed=True.

### 8 · Normal running is restored

Fresh encoder feedback again represents 300 rpm. The controller confirms Running and the drive request stays ON.

Next: inspect the code defect below and see whether automated verification catches it.

Observed: state=RUNNING; fault=NONE; speed=300.0 rpm; drive_request=True; simulated_ms=800; comparison_passed=True.

## Deliberate source change

Working: `return measured > limit;`

Defect: `return (measured > limit) && false;`

The defect always suppresses overspeed detection while remaining buildable.

## Recorded verification

Local automated verification, not live Jenkins. MatIEC, CMake, GCC/Ninja, C assertions, PLC checks, CTest and Cppcheck actually executed. Fault-handling execution in the verification run covers encoder timeout/restart; the separate operating recording covers overspeed.

### BEHAVIORAL_FAIL

Run: 5bf702dd8bea4e7bbe113f25ba99707f. Behavioral counts: {'executed': 45, 'passed': 41, 'failed': 4}. Source base: aa76470b3a7df1a36b23494740870ed969700139; local modifications present, identified by source-file digests. Report-file SHA-256: cc0c53c57032b80f1f5023eb535108512b955490094d291d743d7f1461dd9b41.

Failed: SPEED-05-overspeed-detected at test_drive.c:22; expected=3, actual=0.

Failed: SPEED-06-fault-disables-drive at test_drive.c:23; expected=0, actual=1.

Failed: SPEED-07-exact-scaled-comparison at test_drive.c:24; expected=1, actual=0.

Failed: FAULT-01-overspeed-before-stop at test_drive.c:29; expected=3, actual=0.

### PASS

Run: ee4976b5d4ae457384af57bf8ab76cae. Behavioral counts: {'executed': 45, 'passed': 45, 'failed': 0}. Source base: aa76470b3a7df1a36b23494740870ed969700139; local modifications present, identified by source-file digests. Report-file SHA-256: eceef190ab035229b96e58dd7361b5e336dc004158a7ba49ce022f6e6035579e.

Test sources and PLC sequence hashes match between defect and recovery. Four failed assertions reject the defective revision; repair restores 45/45 checks.

## Fault-code definitions

From drive_controller.h: NO_FAULT=0; STARTUP_TIMEOUT=1; ENCODER_TIMEOUT=2; OVERSPEED=3. These are fault reasons, not overall controller states.

## Evidence

Operating evidence: evidence.json

Verification evidence: verification-evidence.json

Fault-code provenance: fault-definitions.json

## Inspection limits

This text version exposes the story and verified facts to tools that do not execute JavaScript. It does not reproduce visual motion. Assess animation and layout using the interactive page in a browser.
