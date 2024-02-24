import random
ABC = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',]
ONETWOTHREE = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

def rstrings(length):
    if str(length).isdigit():
        randomstring = ""
        for i in range(length):
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
    print("This is designed to be used as an import\n\n")
    print("To import use 'from randomString import rstrings'")
    print("Then usage is rstrings(1) put any number where 1 is.")
    