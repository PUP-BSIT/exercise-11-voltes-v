from voltespackage.pineda import pineda_menu
from voltespackage.corpus import plot
from voltespackage.caculitan import tell_joke
from voltespackage.morales import generate_female_name, generate_male_name
from voltespackage.gulles import age_calculator

def main():

    while True:
        print("\n===== VOLTES-V TEAM MODULE =====")
        print("1. PINEDA - Character Analysis")
        print("2. CORPUS - Line Plot")
        print("3. CACULITAN - Random Programming Joke")
        print("4. MORALES - Baby Name Generator")
        print("5. GULLES - Age Calculator")
        print("6. Exit")

        choice = input("\nSelect an option (1-6): ")

        if choice == "6":
            print("Thank you. Goodbye!")
            break

        elif choice == "1":
            pineda_menu()

        elif choice == "2":
            x_input = input("Enter x values (comma-separated): ")
            x = [float(i) for i in x_input.split(",")]

            y_input = input("Enter y values (comma-separated): ")
            y = [float(i) for i in y_input.split(",")]

            if len(x) != len(y):
                print("Error: x and y must have the same length.")
                continue
            plot(x, y)

        elif choice == "3":
            tell_joke()

        elif choice == "4":
            print("Baby Name Generator")
            gender = input("Enter baby gender (male/female): ").strip().lower()

            if gender == "female":
                print(generate_female_name())
            elif gender == "male":
                print(generate_male_name())
            else:
                print("Incorrect input.")

        elif choice == "5":
            print("Age Calculator")
            birthdate = input("Enter your birthdate (YYYY-MM-DD): ").strip()
            try:
                age = age_calculator(birthdate)
                print(f"Your age is: {age} years old.")
            except Exception as e:
                print(f"Error: {e}")
        else:
            print("Invalid option. Please try again.")
            
if __name__ == "__main__":
    main()