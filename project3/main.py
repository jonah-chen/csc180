import numpy as np
from time import perf_counter

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
    
    return dot_product / np.sqrt(p1*p2)
    

def build_semantic_descriptors(sentences):
    """Takes list of sentences as argument. Return dictionary that represents the semantic descripter of each word that appears.

    Args:
        sentences (list of list of string): sentences represented as a list of words.

    Returns:
        dictionary of dictionary (string:int): semantic descripter
    """
    print(len(sentences))
    start = perf_counter()
    d = {}
    for sentence in sentences:
        #print(sentence)
        for word in sentence:

            for other_word in sentence:
                if other_word != word:
                    if word in d:
                        if other_word in d[word]:
                            d[word][other_word] += 1
                        else:
                            d[word][other_word] = 1
                    else:
                        d[word] = {}
                        d[word][other_word] = 1

    end = perf_counter()

    print(f"{(end-start)*1e6}")
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
            f.replace(p, "")
        f = f.split(".")
        print(f[0])

        for i in range(len(f)):
            f[i] = f[i].split(" ")
        print(f[0])

        sem_des = build_semantic_descriptors(f)
        for (key, value) in sem_des.items():
            if key in d: # man
                for (k, v) in value.items(): # {i, 3; am,3; a,2, etc}
                    if k in d[key]:
                        d[key] += v
                    else:
                        d[key] = v
            else:
                d[key] = value                
    return d

    

if __name__ == "__main__":
    pass