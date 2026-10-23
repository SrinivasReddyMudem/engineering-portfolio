# Agent Application: Automated Test Evidence

**441 tests passed** in the recorded local offline run.

| Scope | Passed | What this measures |
| --- | --- | --- |
| SDK agent tests | 363 | Structured schemas, targeted domain validators, skill-loading and mocked-provider behaviour |
| Engineering calculator tests | 78 | Behaviour and boundaries of the existing calculator tools |
| Total | 441 | The two stated offline suites; no duplicate counting |

## What ran

The original Domain-Specific AI Agents application's `tests/` and `sdk_agents/tests/` suites ran locally. The optional response-copy browser test was excluded. Pytest 8.4.2 was loaded in a temporary tools directory; original project dependencies were not modified. The run reported two collection warnings for Pydantic models named like test classes; these were not failed tests.

## What did not run

No live model inference, provider-quality benchmark, browser walkthrough, Jenkins job or hosted CI ran as part of this count. Model calls in the tests are mocked, and external network connections were blocked. This number does not mean every generated answer is correct, every standard is covered, or the application is certified.

## Traceability

Baseline source commit: `83df8ff8feaefee32a42b9b6c76f1ff3c84d4e63`. Source/test/knowledge-file fingerprints were captured and checked unchanged during the run. This identifies the tested working files without claiming the baseline commit alone proves a clean checkout.

Original retained JUnit SHA-256: `7eda8db8be96205e87a4ca319d9bbf5b108011174400598a737a662890b7243d`.

[Inspect the recorded JUnit results](../evidence/agent-tests.junit.xml) · [Explore the AI Agents case study](engineering-analysis.md) · [Back to profile](../README.md)

## Public export

The linked JUnit copy removes machine hostname and file attributes. Test identities and outcomes are unchanged. Original and public-file hashes have separate meanings. [Export details](../evidence/public-export.json).
