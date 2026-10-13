text = input("Enter a word: ").lower()

for i, char in enumerate(text, start=1):
    if char in "aeiou":
        print(f"Vowel '{char}' found at position {i}")
