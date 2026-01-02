from datetime import date, datetime
import re
from enum import Enum

# CONFIGURATION

MAX_NAME_LENGTH = 120
MAX_ALLOWED_AGE = 50

# SYSTEM STATES

class SystemState(Enum):
    START = 1
    GET_NAME = 2
    GET_DOB = 3
    PROCESS = 4
    END = 5

# NAME VALIDATION TASK

def name_is_valid(name: str) -> bool:

    if not name:
        return False

    if len(name) > MAX_NAME_LENGTH:
        return False

    if not re.fullmatch(r"[A-Za-z ]+", name):
        return False

    words = name.strip().split()

    for word in words:
        if len(word) < 2:
            return False
        if not re.search(r"[aeiouAEIOU]", word):
            return False

  # Suspicious pattern checks
    vowels = sum(1 for c in word.lower() if c in "aeiou")
    consonants = sum(1 for c in word.lower() if c.isalpha() and c not in "aeiou")
    if consonants > vowels * 3:  # too many consonants
       return False
    if len(set(word)) < len(word) // 2:  # too many repeated letters
        return False

    return True

# NAME TASK

def name_task() -> str:
    while True:
        name = input("Enter full name: ").strip()
        if name_is_valid(name):
            return name
        print("Invalid name. Letters only, realistic name required.")

# DATE OF BIRTH TASK

def calculate_age(dob: date) -> int:
    today = date.today()
    age = today.year - dob.year
    if (today.month, today.day) < (dob.month, dob.day):
        age -= 1
    return age

def dob_task() -> date:
    while True:
        dob_input = input("Enter DOB (YYYY-MM-DD): ").strip()
        try:
            dob = datetime.strptime(dob_input, "%Y-%m-%d").date()
            age = calculate_age(dob)

            if 0 < age <= MAX_ALLOWED_AGE:
                return dob

            print(f"Age must be {MAX_ALLOWED_AGE} years or younger.")
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")


# MAIN APPLICATION

def app():
    state = SystemState.START
    name = None
    dob = None
    age = None

    while state != SystemState.END:

        if state == SystemState.START:
            print("=== User Registration System ===")
            state = SystemState.GET_NAME

        elif state == SystemState.GET_NAME:
            name = name_task()
            state = SystemState.GET_DOB

        elif state == SystemState.GET_DOB:
            dob = dob_task()
            state = SystemState.PROCESS

        elif state == SystemState.PROCESS:
            age = calculate_age(dob)
            print("\n Registration Successful")
            print(f"Name : {name}")
            print(f"Age  : {age}")
            state = SystemState.END

# ENTRY POINT

if __name__ == "__main__":
    app()
