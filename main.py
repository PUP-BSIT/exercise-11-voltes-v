from pineda import pineda_menu
#from member2 import function_from_member1
#from member3 import function_from_member2
#from member4 import function_from_member3
#from member5 import function_from_member4


def main():

    while True:
        print("\n===== VOLTES-V TEAM MODULE =====")
        print("1. PINEDA - Character Analysis")
        print("2. [MEMBER2 LASTNAME] - [Function Description]")  
        print("3. [MEMBER3 LASTNAME] - [Function Description]")  
        print("4. [MEMBER4 LASTNAME] - [Function Description]")  
        print("5. [MEMBER5 LASTNAME] - [Function Description]")  
        print("6. Exit")
        
        choice = input("\nSelect an option (1-6): ")
        
        if choice == "6":
            print("Thank you. Goodbye!")
            break
            
        elif choice == "1":
            pineda_menu()
        
        elif choice == "2":
            # function_from_member2()
            pass
            
        elif choice == "3":
            # function_from_member3()
            pass
            
        elif choice == "4":
            # function_from_member4()
            pass
            
        elif choice == "5":
            # function_from_member5()
            pass
            
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()