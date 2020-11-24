# Problem 1

f = open("data2.txt")
text = f.read()
text = text.split("\n")
for line in text:
    if line.upper() == "LOL":
        print(line)

# Problem 2

def dict_to_str(d):
    """Return a str containing each key and value in the dict d. Keys and values are seperated by a comma. Key-values pairs are seperated by a newline character from each other."""

    string = ""
    for key in d.keys():
        string += f"{key}, {d[key]}\n"

    return string


# Problem 3

def dict_to_str_sorted(d):
    """Return a str containing each key and value in dict d. Keys and values are seperated by a comma. Key-value pairs are seperated by a newline character form each other, and the key in each string must be sorted in ascending order"""
    keys = sorted(d.keys())
    string = ""
    for key in keys:
        string += f"{key}, {d[key]}\n"

    return string


# Problem 4a

f = open("cmudict-0.7b", encoding='latin-1')
d = f.read()
dictionary = {}
d = d.split("\n")
for s in d:
    r = s.split(" ")
    dictionary[r[0]] = r[2:]

# Problem 4b

f = open("cmudict-0.7b.phones", encoding='latin-1')
d = f.read()
phones = {}
d = d.split("\n")
for s in d:
    r = s.split("\t")
    if len(r) > 1:
        phones[r[0]] = r[1]

# Problem 4c
def num_vowels(word):
    """Return the number of vowels in a valid word in the dictionary. Punctuation cannot be included."""
    try:
        syllables = dictionary[word.upper()]
    except KeyError:
        return -1
    vowels = 0
    for s in syllables:
        if phones[s] == "vowel":
            vowels += 1
    return vowels

# Problem 4d

def count_syllables(word):
    """Count the number of syllables in a valid word found in the dictionary. Punctuation can be included but multiple words or invalid words cannot."""
    last = 0
    syllables = 0
    word = word.upper()
    while len(word) > 0:
        try:
            word_phones = dictionary[word]
            break;
        except KeyError:
            word = word[:-1]
    if word == '':
        raise ValueError("The word enter is not in the dictionary.")
    for v in word_phones:
        while len(v)>0:
            try:
                ph = phones[v]
                break
            except KeyError:
                v = v[:-1]
        if len(v) == 0:
            raise ValueError("The word contains an invalid phone.")

        if ph == "vowel":
            if last != 1:
                syllables += 1
                last = 1
        else:
            last = 0
    return syllables

# Problem 5
def FKGL(text):
    """Return the Flesch-Kindcaid Readability Grade Level of a text."""
    text = text.replace("!", ".").replace("?", ".").replace("\"", "")
    sentences = len(text.split('.'))-1
    text = text.split(' ')
    words = len(text)
    syllables = 0
    errors = 0
    for word in text:
        try:
            syllables += count_syllables(word)
        except ValueError:
            errors += 1
            print(f"The word {word} is not in the dictionary.")
    if errors:
        print(f"The text contains {errors} invalid words.")
        
    print(f"words: {words} sentences: {sentences} syllables: {syllables}")
    return 0.39*words/sentences + 11.8*syllables/words - 15.59

praxis = open("praxis.txt").read()
print(FKGL(praxis))
