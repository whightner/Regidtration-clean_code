# Release v1.0.1 — 2026-01-03

## Summary
- **Release**: v1.0.1
- **Date**: 2026-01-03
- **Scope**: Patch release — repository cleanup and minor fixes.

## Highlights
- Removed unnecessary file `main3.py` (cleanup).
- Bumped patch version to v1.0.1 and tagged the release.
- No functional changes to features, tests or public API — this is a maintenance release.

## Details
- Cleanup: removed stray/unused file `main3.py` from the repository.
- Tests: unchanged; full test suite still passes (see `tests/`).
- Docs: README and release notes updated in prior release; no additional doc changes in this patch.

## Notes
- This is a patch release: consumers should not expect behavioral changes.
- Recommended: pull the latest tag and run the test suite locally to verify your environment:

```bash
git fetch --tags
git checkout refs/tags/v1.0.1
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt
python3 tests/test.py
```

## Files changed / removed in this release
- Removed: `main3.py`

---

Merci — release patch prête. Souhaitez-vous que je crée aussi une `CHANGELOG.md` centralisant les releases ?
