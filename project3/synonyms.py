"""
"""

from math import sqrt

def cosine_similarity(vec1, vec2):
    """Return the cosine similarity of the two words described by the vectors vec1 and vec2 as a float.

    Args:
        vec1 (dictionary): vector representing the first word
        vec2 (dictionary): vector representing the second word
    
    Returns:
        r (float): A floating point number between -1.0 and 1.0. Larger number means more similar.
    """
    dot_product = sum(vec1[key]*vec2.get(key, 0) for key in vec1)
    p1, p2 = 0,0
    for val in vec1.values():
        p1 += val * val
    for val in vec2.values():
        p2 += val * val
    
    return dot_product / sqrt(p1*p2)
    

def build_semantic_descriptors(sentences):
    """Takes list of sentences as argument. Return dictionary that represents the semantic descripter of each word that appears.

    Args:
        sentences (list of list of string): sentences represented as a list of words.

    Returns:
        dictionary of dictionary (string:int): semantic descripter
    """
    d = {}
    for sentence in sentences:
        for i in range(len(sentence)):
            sentence[i] = sentence[i].lower()
        freq = set(sentence)
        for word in freq:
            for other_word in freq:
                if word != other_word:
                    if word in d:
                        if other_word in d[word]:
                            d[word][other_word] += 1
                        else:
                            d[word][other_word] = 1
                    else:
                        d[word] = {other_word:1}
    return d

def build_semantic_descriptors_from_files(filenames):
    """Return the semantic descriptors for all the words in the files with filename filenames

    Args:
        filenames (list of string): elements are paths to indivisual files of text
    """
    d = {}
    for filename in filenames:
        f = open(filename, "r", encoding="latin1").read()

        for p in [",", "-", "--", ":", ";"]:
            f = f.replace(p, " ")
        f = f.split(".")
        f1 = []
        for e in f:
            f1 += e.split("!") 
        f2 = []
        for e in f1:
            f2 += e.split("?") 
        del f, f1
        f = f2

        for i in range(len(f)):
            f[i] = f[i].split()
        
        
        sem_des = build_semantic_descriptors(f)
        for (key, value) in sem_des.items():
            if key in d: # man
                for (k, v) in value.items(): # {i, 3; am,3; a,2, etc}
                    if k in d[key]:
                        d[key][k] += v
                    else:
                        d[key][k] = v
            else:
                d[key] = value   
    return d

 #Subpart d
 
def most_similar_word(word, choices, semantic_descriptors, similarity_fn):
    """Finds the most similar word from the list of choices to the word words

    Args:
        word (string): the word for which a synonum is attempted to be found
        choices (list of string): the available options for the synonym
        semantic_descriptors (dictionary of dictionary): semantic descriptors built from build_semantic_descriptors method
        similarity_fn (float(vec1, vec2, *args)): A function that return a number from the subset (-1,infinity] which higher number means more similar.keys

    Returns:
        string: the best synonym chosen by semantic_descriptors and similarity_fn.
    """
    largest_similarity = -2.0
    vec1 = semantic_descriptors[word]
    for e in choices:
        if e in semantic_descriptors:
            vec2 = semantic_descriptors[e]
            similarity = similarity_fn(vec1, vec2)
        else:
            similarity = -1.0

        if similarity > largest_similarity:
            largest_similarity = similarity
            answer = e

    return answer

#Subpart e

def run_similarity_test(filename, semantic_descriptors, similarity_fn):
    correct = 0
    words = open(filename, "r", encoding="latin1").read().split("\n")
    if words[-1] == "":
        del words[-1]
    for question in words:
        question = question.split()
        if(question and most_similar_word(question[0], question[2:], semantic_descriptors, similarity_fn) == question[1]):
            correct += 1
    return (float) (100.0*correct/len(words))



if __name__ == "__main__":
    sd = build_semantic_descriptors_from_files(["/home/hina/PycharmProjects/esc180/project3/pg7178.txt", "/home/hina/PycharmProjects/esc180/project3/2600-0.txt"])
    print(run_similarity_test("/home/hina/PycharmProjects/esc180/project3/test.txt", sd, cosine_similarity))
