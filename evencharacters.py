characters = input("enter your characters: ")

for character in characters:
    index = characters.index(character)
    if index%2:
        print(character)
    else:
        pass