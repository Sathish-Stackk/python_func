from itertools import permutations

def get_permutations(word):
    return [''.join(p) for p in permutations(word)]

print(get_permutations("ABC"))
