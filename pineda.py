import pandas as pd  


def count_vowels(string):
    vowels = "aeiouAEIOU"
    count = sum(1 for char in string if char in vowels)
    print(f"The string '{string}' contains {count} vowels.")
    return count


def count_consonants(string):
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    count = sum(1 for char in string if char in consonants)
    print(f"The string '{string}' contains {count} consonants.")
    return count


def character_frequency_analysis(text):
    char_list = list(text)
    df = pd.DataFrame(char_list, columns=['Character'])
    
    freq_table = df['Character'].value_counts().reset_index()
    freq_table.columns = ['Character', 'Frequency']
    freq_table['Percentage'] = (freq_table['Frequency'] 
                                / len(text) * 100).round(2)
    
    freq_table = freq_table.sort_values(by='Frequency', ascending=False)
    
    print("\nCharacter Frequency Analysis:")
    print(freq_table.to_string(index=False))
    
    letter_count = sum(1 for char in text if char.isalpha())
    digit_count = sum(1 for char in text if char.isdigit())
    space_count = sum(1 for char in text if char.isspace())
    special_count = len(text) - letter_count - digit_count - space_count
    
    print("\nSummary Statistics:")
    print(f"Total characters: {len(text)}")
    print(f"Letters: {letter_count} ({letter_count/len(text)*100:.2f}%)")
    print(f"Digits: {digit_count} ({digit_count/len(text)*100:.2f}%)")
    print(f"Spaces: {space_count} ({space_count/len(text)*100:.2f}%)")
    print(f"Special characters: {special_count} ({special_count/
          len(text)*100:.2f}%)")
    
    return freq_table


def pineda_menu():
    print("\n----- PINEDA: Character Analysis -----")
    string = input("Enter a string: ")
    
    if not string:
        print("Empty input. Using default text 'Hello, World!'")
        string = "Hello, World!"
    
 
    count_vowels(string)
    count_consonants(string)
    
    
    print("\nWould you like to perform character frequency analysis " \
    "using pandas? (yes/no)")
    freq_choice = input("> ").lower()
    
    if freq_choice == "yes" or freq_choice == "y":
        character_frequency_analysis(string)
        print("Character frequency analysis completed.")