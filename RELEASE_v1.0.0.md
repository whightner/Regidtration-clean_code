# Release v1.0.0 — 2026-01-03

## Summary
- **Release**: v1.0.0
- **Date**: 2026-01-03
- **Scope**: Initial educational release implementing input validation, DOB-based age calculation, interactive CLI, tests and documentation.

## Highlights
- Name validation and normalization supporting accents, hyphens and apostrophes.
- Input changed to Date of Birth (DOB) — age computed from DOB.
- Age bounds: minimum 16, maximum 70 (inclusive).
- Interactive CLI (`main.py`) prompting for name and DOB and printing a formatted summary.
- Complete test suite (pytest) + fallback test runner.
- README updated with setup/run instructions.

## Details

### Features
- `features/name_checker.py` — robust name validation & normalization.
- `features/age_checker.py` — DOB parsing, age calculation and bounds enforcement (16–70).
- `main.py` — interactive entrypoint.
- `tests/` — unit tests and test runner (`tests/test.py`).
- `requirements.txt` — dev dependencies (`pytest>=7.0`).

### Tests
- Unit tests: `tests/test_name_checker.py`, `tests/test_age_checker.py`
- Test runner entrypoint: `tests/test.py` (uses `pytest` if available, falls back to `unittest`)

### Documentation
- `README.md` updated (FR/EN) with project structure, validation rules, setup and testing instructions.

## Breaking changes / Important notes
- The application now expects a **date of birth** instead of an age value. Supported formats: `YYYY-MM-DD`, `DD/MM/YYYY`.
- Age validation now enforces a minimum of **16 years** (previously age semantics were different). Inputs outside 16–70 will be rejected.

## Upgrade / Migration
- Update any automated callers to pass DOB instead of age.
- To run locally:
```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt
python3 tests/test.py
python main.py
```

- Example non-interactive run:
```bash
printf "Jean-Luc\n2000-05-20\n" | python3 main.py
```

## Files changed / Added
- Added / updated:
  - `features/name_checker.py`
  - `features/age_checker.py`
  - `main.py`
  - `tests/test_name_checker.py`
  - `tests/test_age_checker.py`
  - `tests/test.py`
  - `requirements.txt`
  - `README.md`

## Contributors
- Project author / community contributors (educational example)

---

## Notes (FR)

### Résumé
- **Version** : v1.0.0
- **Date** : 2026-01-03
- **Portée** : Publication initiale éducative — validation du nom, saisie par date de naissance, calcul d'âge, CLI, tests et documentation.

### Points clés
- Validation/normalisation du nom (accents, traits d'union, apostrophes).
- Saisie passée à la **date de naissance** (DOB → âge calculé).
- Age validé entre **16** et **70** ans inclus.
- CLI interactive : `main.py`.
- Suite de tests complète + runner `tests/test.py`.
- Documentation et instructions d'installation ajoutées.

### Changements importants
- Entrée modifiée : fournir la date de naissance au lieu de l'âge.
- Borne minimale d'âge : 16 ans.

### Exécution
Voir les instructions ci-dessus (venv, installation et exécution des tests/du programme).
