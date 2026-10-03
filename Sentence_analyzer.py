sentence = "Python makes software development simple and powerful"

words = sentence.split()
lengths = [len(word) for word in words]

print("Words:", len(words))
print("Characters:", len(sentence.replace(" ", "")))
print("Shortest Word:", min(words, key=len))
print("Longest Word:", max(words, key=len))
print("Average Word Length:", round(sum(lengths) / len(lengths), 2))
