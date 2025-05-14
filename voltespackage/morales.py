from faker import Faker
fake = Faker()

def generate_female_name():
    female_first_name = fake.first_name_female()
    return f"Your baby's name: {female_first_name}"

def generate_male_name():
    male_first_name = fake.first_name_male()
    return f"Your baby's name: {male_first_name}"