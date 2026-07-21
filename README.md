# Horseless Carriage — Evaluation Repo (To-Do List Web App)

This is the fixed state repo for Horseless Carriage's automated team-performance
evaluation harness. It is **not** a real product — it exists solely so the
Horseless Carriage agent team has a real GitHub repo to run a fixed 5-sprint
scenario against, so results are comparable across Horseless Carriage versions
over time.

- Managed by: [CI-Till-Krempel/Horseless-Carriage](https://github.com/CI-Till-Krempel/Horseless-Carriage)
- Scenario: see `eval/scenario/PRODUCT-VISION.md` in the Horseless Carriage repo for the fixed product vision fed to the team every run.
- Each automated eval run creates a fresh branch here (`eval/<version>-run<N>`) rather than touching `main`.
- `main` is kept empty/minimal on purpose — nothing from the eval runs should land here.

See `HORSELESS_CARRIAGE_RELEASE.md`/`SECURITY.md`/`MANUAL.md` in the main repo for
how this fits into the release process.
