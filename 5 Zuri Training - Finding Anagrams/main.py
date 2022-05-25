# Check if two words are anagrams
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagrams(word, anagram):

    if len(word) != len(anagram):
        return False

    for i in word:
        is_found = False
        for j in anagram:
            if i == j:
                is_found = True
        if is_found == False:
            return False

    return True

print(find_anagrams("below", "elbowa"))
print(find_anagrams("below", "elboa"))
print(find_anagrams("below", "elbow"))
