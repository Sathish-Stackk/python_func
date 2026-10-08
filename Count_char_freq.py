def character_frequency(text):
    frequency = {}

    for char in text:
        if char != " ":
            frequency[char] = frequency.get(char, 0) + 1

    return frequency


text = input("Enter text: ")
print(character_frequency(text))
