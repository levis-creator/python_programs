character = input("Enter your character: ")
n = int(input("Enter the number of character you want to remove: "))


def remove_chars(character, n):
    sliced = slice(-n)
    print(character[sliced])


remove_chars(character=character, n=n)
