def count_vowels(text):
    vowels = "aeiou"
    return sum(1 for char in text.lower() if char in vowels)

word = input("Enter text: ")
print("Vowels:", count_vowels(word))
