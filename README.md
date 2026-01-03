# Clean Code Practice – Python User Info

*An educational Python project to practice Clean Code principles.*

<p align="left">
  <img src="https://img.shields.io/badge/version-1.1.0-blue" alt="version" />
  <img src="https://img.shields.io/badge/python-%3E%3D3.10-3776AB?logo=python&logoColor=white" alt="python" />
  <img src="https://img.shields.io/badge/license-MIT-green" alt="license" />
  <img src="https://img.shields.io/badge/status-educational-success" alt="status" />
</p>

- **Version**: 1.1.0  
- **Status**: Educational / Learning Project  
- **License**: MIT  
- **Python Version**: >= 3.10  
- **Author**: Community / Educational Example  
- **Last Update**: 2026

---

🌍 **Language / Langue**  
- 🇫🇷 [Français](#français)  
- 🇬🇧 [English](#english)

---

## Français

### Description
Ce projet est un **exercice simple de pratique du Clean Code en Python**.  
Il consiste à écrire un programme qui :

- Demande le **nom** de l’utilisateur (valide)
- Demande sa **date de naissance** (valide)
- Calcule automatiquement son **âge**
- Affiche :
  - son **nom**
  - son **âge**
  - son **année de naissance**

L’objectif principal est de **respecter les bonnes pratiques Python** :
- fonctions courtes et claires
- noms explicites
- validation des entrées
- séparation des responsabilités
- code lisible et testable

---

### Fonctionnalités
- Validation du nom (non vide, alphabétique)
- Validation de la date de naissance (format attendu : YYYY-MM-DD ou DD/MM/YYYY)
- Calcul automatique de l'âge (doit être entre 16 et 70 ans inclus)
- Affichage clair et formaté des résultats

---

### Structure du projet
```text
clean-code-python/
│
├── main.py
├── features/
│   ├── name_checker.py
│   └── age_checker.py
├── tests/
│   ├── test.py
│   ├── test_name_checker.py
│   └── test_age_checker.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

### Exemple de sortie
```text
Nom : Alex
Âge : 25 ans
Année de naissance : 1999
```

---

### Règles de validation
- **Nom** :  
  - non vide  
  - uniquement des lettres  
- **Date de naissance** :  
  - format `YYYY-MM-DD` ou `DD/MM/YYYY`  
  - l'âge calculé doit être compris entre 16 et 70 ans inclus  

---

### Bonnes pratiques appliquées
- Respect du **PEP 8**
- Fonctions documentées avec **docstrings**
- Une responsabilité par fonction
- Pas de logique complexe dans `main`
- Gestion des erreurs utilisateur

---

### Exemple de docstring Python
```python
def calculate_birth_year(age: int, current_year: int) -> int:
    """
    Calculate the birth year based on the user's age.

    :param age: User's age
    :param current_year: Current year
    :return: Estimated birth year
    """
```

---

### Exécution
```bash
python main.py
```

### Setup et tests

Pour installer les dépendances de développement et exécuter les tests :

```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt
python3 tests/test.py
```

Si vous ne souhaitez pas utiliser un environnement virtuel :

```bash
python3 -m pip install --user -r requirements.txt
python3 tests/test.py
```

---

### Objectif pédagogique
Ce projet est idéal pour :
- débutants en Python
- pratiquer le **Clean Code**
- apprendre à structurer un petit programme
- comprendre la validation des entrées utilisateur

---

## English

### Description
This project is a **simple Clean Code practice exercise in Python**.  
The program:

- Asks the user for their **name** (valid)
- Asks for their **date of birth** (valid)
- Calculates the user's **age** from the provided DOB
- Displays:
  - user's **name**
  - **age**
  - **birth year**

The main goal is to **apply Python Clean Code principles**.

---

### Features
- Name validation (non-empty, alphabetic)
- Date of birth validation (formats: `YYYY-MM-DD` or `DD/MM/YYYY`)
- Automatic age calculation (must be between 16 and 70 years inclusive)
- Clear and formatted output

---

### Project Structure
```text
clean-code-python/
│
├── main.py
├── features/
│   ├── name_checker.py
│   └── age_checker.py
├── tests/
│   ├── test.py
│   ├── test_name_checker.py
│   └── test_age_checker.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

### Sample Output
```text
Name: Alex
Age: 25 years
Birth year: 1999
```

---

### Validation Rules
- **Name**:
  - must not be empty
  - letters only
- **Date of birth**:
  - must be provided in `YYYY-MM-DD` or `DD/MM/YYYY` format
  - computed age must be between 16 and 70 inclusive

---

### Clean Code Practices
- PEP 8 compliant
- Functions documented with **docstrings**
- Single Responsibility Principle
- No business logic in `main`
- User input validation

---

### Python Docstring Example
```python
def calculate_birth_year(age: int, current_year: int) -> int:
    """
    Calculate the birth year based on the user's age.

    :param age: User's age
    :param current_year: Current year
    :return: Estimated birth year
    """
```

---

### Run the Program
```bash
python main.py
```

### Setup and tests

To install development dependencies and run the test suite:

```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt
python3 tests/test.py
```

If you prefer not to use a virtual environment:

```bash
python3 -m pip install --user -r requirements.txt
python3 tests/test.py
```

---

### Educational Goal
Perfect for:
- Python beginners
- Clean Code practice
- Learning small project structure
- User input validation
