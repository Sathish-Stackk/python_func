sentence = "Python programming improves problem solving skills"
words = sentence.split()

longest = ""

for word in words:
    if len(word) > len(longest):
        longest = word

print("Longest Word:", longest)
print("Length:", len(longest))
