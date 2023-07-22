import random

# Lists of characters used to generate the password
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
           'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
           'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def ask_about(elements):
    """Ask the user how many letters, numbers, or symbols they want in the password."""
    while True:
        num = input(f"How many {elements} would you like in your password? ")
        if not num.isdigit():
            print("That is not a valid response. Please try again.")
        else:
            return num


def randomly_choose(num, num_of_element):
    """"Randomly choose a specified number of letters, numbers, or symbols from the given list."""
    part_of_password = ""
    for _ in range(num_of_element):
        part_of_password += random.choice(num)
    return part_of_password


def generate_password(lets, nums, syms):
    """"Generate a password by scrambling the letters, numbers, and symbols."""
    unscrambled_password = lets + nums + syms
    scrambled_list = random.sample(unscrambled_password, len(unscrambled_password))
    scrambled_word = ""
    for item in scrambled_list:
        scrambled_word += item
    return scrambled_word

# Ask the user for the number of letters, numbers, and symbols they want in the password
num_of_letters = int(ask_about("letters"))
num_of_numbers = int(ask_about("numbers"))
num_of_symbols = int(ask_about("symbols"))

# Randomly choose the specified number of letters, numbers, and symbols
random_letters = randomly_choose(letters, num_of_letters)
random_numbers = randomly_choose(numbers, num_of_numbers)
random_symbols = randomly_choose(symbols, num_of_symbols)

# Generate the password by scrambling the combination of letters, numbers, and symbols
password = generate_password(random_letters, random_numbers, random_symbols)

# Print the generated password
print(f"Your password is {password}")
