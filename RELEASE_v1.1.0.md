# Release v1.1.0 — 2026-01-03

## Summary
- **Release**: v1.1.0  
- **Date**: 2026-01-03  
- **Scope**: Améliorations UX et contrôle du flux dans l'entrée interactive (`main.py`).

## Changes (FR)
- Ajout d'une option "continuer / quitter" après chaque affichage du résumé : l'utilisateur peut appuyer sur Entrée pour continuer ou taper `q` pour quitter.
- Limitation des tentatives : 3 essais max pour chaque saisie incorrecte (nom et date de naissance). Le programme se ferme si les tentatives sont épuisées.
- Gestion d'erreurs plus explicite et codes de sortie non-zéro en cas d'annulation ou d'échec.
- Suppression du fichier superflu `main3.py` (cleanup).

## Changes (EN)
- Added "continue / quit" prompt after each summary display: Enter to continue, `q` to quit.
- Input attempts limited to three (3) per field (name and DOB); program exits when attempts are exhausted.
- Clearer error messages and non-zero exit codes on cancellation/failure.

## Impact / Notes
- Comportement interactif amélioré ; les scripts non-interactifs restent utilisables (stdin piping) mais l'UX interactive est maintenant guidée.
- Validations existantes (NameChecker, AgeChecker) inchangées. Age bounds: 16–70.

## How to run
```bash
# run interactively
python3 main.py

# run non-interactive example
printf "Jean-Luc\n2000-05-20\n" | python3 main.py

# run tests (venv recommended)
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt
python3 tests/test.py
```

## Files modified / added
- Modified: `main.py`
- Added: `RELEASE_v1.1.0.md`
- Removed: `main3.py`

## Migration
- Aucun changement API — simplement tester l'UX interactive si vous l'utilisez manuellement.

## Contributors
- Project author / contributors

---
(End of release notes)

```//
filepath: /home/alex/development/Regidtration-clean_code/RELEASE_v1.1.0.md
```
# Release v1.1.0 — 2026-01-03

## Summary
- **Release**: v1.1.0  
- **Date**: 2026-01-03  
- **Scope**: Améliorations UX et contrôle du flux dans l'entrée interactive (`main.py`).

## Changes (FR)
- Ajout d'une option "continuer / quitter" après chaque affichage du résumé : l'utilisateur peut appuyer sur Entrée pour continuer ou taper `q` pour quitter.
- Limitation des tentatives : 3 essais max pour chaque saisie incorrecte (nom et date de naissance). Le programme se ferme si les tentatives sont épuisées.
- Gestion d'erreurs plus explicite et codes de sortie non-zéro en cas d'annulation ou d'échec.
- Suppression du fichier superflu `main3.py` (cleanup).

## Changes (EN)
- Added "continue / quit" prompt after each summary display: Enter to continue, `q` to quit.
- Input attempts limited to three (3) per field (name and DOB); program exits when attempts are exhausted.
- Clearer error messages and non-zero exit codes on cancellation/failure.
- Removed unnecessary file `main3.py`.

## Impact / Notes
- Comportement interactif amélioré ; les scripts non-interactifs restent utilisables (stdin piping) mais l'UX interactive est maintenant guidée.
- Validations existantes (NameChecker, AgeChecker) inchangées. Age bounds: 16–70.

## How to run
```bash
# run interactively
python3 main.py

# run non-interactive example
printf "Jean-Luc\n2000-05-20\n" | python3 main.py

# run tests (venv recommended)
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt
python3 tests/test.py
```

## Files modified / added
- Modified: `main.py`
- Added: `RELEASE_v1.1.0.md`
- Removed: `main3.py`

## Migration
- Aucun changement API — simplement tester l'UX interactive si vous l'utilisez manuellement.

## Contributors
- Project author / contributors

---
(End of release notes)