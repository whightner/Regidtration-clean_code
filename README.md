# Clean Code Practice – Python User Info

*An educational Python project to practice Clean Code principles.*

<p align="left">
  <img src="https://img.shields.io/badge/version-1.0.0-blue" alt="version" />
  <img src="https://img.shields.io/badge/python-%3E%3D3.10-3776AB?logo=python&logoColor=white" alt="python" />
  <img src="https://img.shields.io/badge/license-MIT-green" alt="license" />
  <img src="https://img.shields.io/badge/status-educational-success" alt="status" />
</p>

- **Version**: 1.0.0  
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
- Demande son **âge** (valide, maximum 70 ans)
- Calcule sa **date de naissance**
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
- Validation de l’âge (entier positif ≤ 70)
- Calcul automatique de l’année de naissance
- Affichage clair et formaté des résultats

---

### Structure du projet
```text
clean-code-python/
│
├── main.py
├── utils.py
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
- **Âge** :  
  - nombre entier  
  - compris entre 0 et 70 inclus  

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
- Asks for their **age** (valid, maximum 70)
- Calculates the **birth year**
- Displays:
  - user's **name**
  - **age**
  - **birth year**

The main goal is to **apply Python Clean Code principles**.

---

### Features
- Name validation (non-empty, alphabetic)
- Age validation (positive integer ≤ 70)
- Automatic birth year calculation
- Clear and formatted output

---

### Project Structure
```text
clean-code-python/
│
├── main.py
├── utils.py
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
- **Age**:
  - integer
  - between 0 and 70 inclusive

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

---

### Educational Goal
Perfect for:
- Python beginners
- Clean Code practice
- Learning small project structure
- User input validation
