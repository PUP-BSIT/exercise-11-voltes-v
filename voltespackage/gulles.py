from datetime import datetime

def age_calculator(birthdate: str) -> int:
    birthdate = datetime.strptime(birthdate, "%Y-%m-%d")
    today = datetime.today()
    
    age = today.year - birthdate.year
    if (today.month, today.day) < (birthdate.month, birthdate.day):
        age -= 1
    return age