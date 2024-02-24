# Import the 'random' libary.

import random

# Define Constants
ABC = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',]
ONETWOTHREE = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Define 'rstrings' function, with 'length' as the only positional argument. This means you place a number in between the brackets when running the program, and it loops for that length.

def rstrings(length):
    # Checks the variable contains only digits, if it doesn't it continues, else it returns a 0, which stops errors from occurring.
    if str(length).isdigit():
        # Here we make sure that length is an integer, it could slip through if it's a string with only numbers.
        randomstring = ""
        length = int(length)
        for i in range(length):
            # Each loop decides whether to use a letter or a number, adding it to the 'randomstring' variable, repeating for the length inputted.
            chooser = 0
            chooser = random.choice([1, 2])
            if chooser == 1:
                randomstring = f"{randomstring}{(random.choice(ABC))}"
            else:
                randomstring = f"{randomstring}{(random.choice(ONETWOTHREE))}"
        return randomstring
    else:
        return 0

if __name__ == '__main__':
    print("This is designed to be used as an import\n")
    print("To import use 'from randomString import rstrings\n")
    print("Then usage is rstrings(1) put any number where 1 is.\n")
    # string = rstrings('10')
    # print(string)
