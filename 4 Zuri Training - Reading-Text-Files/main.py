# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!")
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

import string

def read_file_content(filename):
    with open(filename) as f:
        lines = f.readlines()
        return lines


def count_words():
    text = read_file_content("./story.txt")
    dict = {}
    for line in text:
        words = line.translate(str.maketrans('', '', string.punctuation)).lower().split()

        for word in words:
            if len(dict) >= 1:
                is_found = False
                for key, value in dict.items():
                    if key == word:
                        value += 1
                        dict[word] = value
                        is_found = True
                        break

                if is_found == False:
                    dict[word] = 1

            else:
                dict[word] = 1

    return dict

print(read_file_content("./story.txt"))
print(count_words())
