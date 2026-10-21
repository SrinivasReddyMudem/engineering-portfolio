# Embedded Build Reliability - Detecting a Defect That Compilation Missed

A deliberately introduced queue-adapter defect falsely reported success when the queue was full. Automated behavioral tests detected it. Controlled recovery restored all 10 passing test executions without changing their assertions.

<img src="../assets/project-reliability.svg" alt="Embedded Build Reliability: recorded baseline, injected defect and verified recovery" width="1120" class="project-card">

<img src="../assets/technologies-reliability.svg" alt="Technologies used: Jenkins, Docker, Git, Python, CMake/GCC, Zephyr RTOS, Twister/Ztest" width="1120" class="technology-row">

## Recorded Jenkins verification

<img src="../assets/jenkins-verification.svg" alt="Recorded Jenkins verification: baseline 10/10 passed; injected defect 7 passed and 3 failed; recovery 10/10 passed. Recorded results, not live status." width="1120" class="project-card">

Each recorded Jenkins run contained 10 test executions across two queue configurations. The deliberately defective revision produced three failed executions; recovery restored all 10 passing executions without changing the assertions.

## My engineering contribution

I integrated Zephyr Twister/Ztest verification into an isolated Jenkins/Docker workflow, retained source-linked verification artifacts and implemented deterministic reporting to compare the baseline, injected defect and recovery.

**Professional capability:** Embedded debugging, reproducible CI/CD verification, fault isolation and reviewable technical decisions.

Official project: **Embedded CI/CD Reliability Platform**. Implementation repository: `embedded-cicd-reliability-platform` (private).

## Technologies & Tools

**Embedded execution:** `C` · `Zephyr RTOS` · `Twister/Ztest`

**CI & isolation:** `Jenkins` · `Docker` · `Git`

**Build toolchain:** `CMake` · `GCC`

**Evidence reporting:** `Python`

CMake configures the Zephyr application build and GCC compiles the native target. Twister/Ztest executes the queue checks. Jenkins orchestrates isolated verification, Docker bounds the execution environment, and Python produces source-linked reports.

## Failure mechanism

**Expected: `-ENOMSG` (`-42` in this environment) → Actual: `0` (false success).**

The queue rejected the message, but the adapter hid the error. A caller could therefore incorrectly believe the message had been accepted. The controlled mutation compiled successfully; this was a behavior failure, not a build or infrastructure failure.

For the four-message burst, a two-message queue should accept two messages and reject two. A four-message queue should accept all four. Synchronization prevents the consumer from draining the queue during that burst.

Three assertions detected the defect: one burst-behavior check for capacity 2, and two explicit full-queue error checks, one for each capacity. Capacity 4's four-message burst still passed; its separate full-queue check failed.

## Technical evidence

[Inspect recorded source revisions, counts and assertion evidence](../evidence/recorded-recovery-summary.json).

The following identities refer to retained recorded executions. This page does not rerun Jenkins. The image above is evidence-derived artwork, not a screenshot or live pipeline status.

| Recorded execution | Full source revision | Executed | Passed | Failed |
| --- | --- | --- | --- | --- |
| Original Green | `7c8505541580c93697dfbcec09662b89e0edffa2` | 10 | 10 | 0 |
| Deliberate Red | `2988a4d50901ce0b640e94f5b5b08e366615ebce` | 10 | 7 | 3 |
| Recovery | `1f343d0d212e9140665b6f7213ba2acb7475b318` | 10 | 10 | 0 |

| Failed check in Red | Queue capacity | Source location | Expected | Actual |
| --- | --- | --- | --- | --- |
| Burst error propagation | 2 messages | `main.c:67` | `-42` | `0` |
| Explicit full-queue adapter result | 2 messages | `main.c:98` | `-42` | `0` |
| Explicit full-queue adapter result | 4 messages | `main.c:98` | `-42` | `0` |

### Recorded Jenkins versus live local demonstration

The Green/Red/Recovery results above come from recorded Jenkins executions. The local showcase separately supports a bounded adapter experiment through the existing Docker/Twister runner. It is not a newly triggered Jenkins build, and its editor accepts approved variants rather than arbitrary code.

This is a controlled regression experiment, not an independently discovered production defect or automatic diagnosis of arbitrary firmware. The Zephyr queue workload is separate from the ISO-TP communication workload. The public evidence is a curated summary; raw Jenkins archives and implementation source remain private.

## Why the result is trustworthy

**The same assertions were used throughout. Recovery restored correct adapter behavior rather than changing the tests to obtain a passing result.** Source/configuration identities and retained integrity checks support comparison across equivalent execution scopes.

[Inspect evidence analysis →](engineering-analysis.md) | [Request live local demo ↗](https://www.linkedin.com/in/srinivas-reddy-mudem-400181152/) | [← Back to profile](../README.md)
