# Embedded Control & Verification — recorded demonstration

This additive public presentation reuses genuine recorded host PLC/C execution and verified evidence. It does not compile or execute uploaded code, trigger Jenkins, connect to the local computer, or call models.

## Run locally

From this directory: `streamlit run streamlit_app.py`.

## Community Cloud deployment

Repository: `SrinivasReddyMudem/engineering-portfolio`

Branch: `feature/control-verification-streamlit`

Entrypoint: `showcases/control-verification/streamlit_app.py`

Suggested subdomain: `embedded-control-verification` (availability must be confirmed during deployment).

Choose Python 3.12. No secrets or system packages are required. Dependencies are declared alongside the entrypoint. Keep the existing AI Agents deployment unchanged.

## Integrity and scope

The application checks every packaged asset against the retained manifest before rendering. Standalone HTML, CSS and JavaScript are bundled inside Streamlit's supported iframe. Only packaged, reviewed JavaScript executes in the viewer's browser; no user-entered code is accepted. Source snapshots and test results are recorded evidence, not live cloud builds.

Operating replay: overspeed/fault-latch/reset/restart. Verification replay: real defect/recovery build/test/signature events; its operational trace separately covers encoder timeout. No hardware validation, certified safety or ARM secure boot is claimed.
