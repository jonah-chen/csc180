import numpy as np

from urllib.request import urlopen
from string import digits
from concurrent.futures import ThreadPoolExecutor

"""PROBLEM 1:
For this question, you will compute word counts in a large corpus of text.  Word frequency lists (a frequency of the word is the ratio of the number of times the word appears to the total number of words in a document) are commonly used in computational linguistics.  You will write a function that finds the 10 most frequently occurring words in a text file, and a program that uses this function to find the 10 most frequently-occurring words in Pride and Prejudice.  For the purposes of this problem, you may assume, if you like, that all words are separated by spaces and that there is no punctuation in the file, and all the words are in lowercase, so that the list of words in the file text.txt is given by"""

text = open("text.txt", encoding="latin-1").read().split()

"""PART A:
First, store the number of times that the word w appears in the text in word_counts[w].  For example, if the word “the” appears in the file 5 times, word_counts["the"] should be 5. 
For example, if the contents of your file are the opening of Notes from the Underground by Fyodor Dostoyevsky, translated by Constance Garnett:

I am a sick man. I am a spiteful man. I am an unattractive man. I believe my liver is diseased. However, I know nothing at all about my disease, and do not know for certain what ails me.

, and you do not process the text in any way other than using read().split(), the list of words will be:

["I", "am", "a", "sick", "man.", "I", "am", "a", "spiteful", "man.", "I", "am","an", "unattractive", "man.", "I", "believe", "my", "liver", "is", "diseased.","However,", "I", "know", "nothing", "at", "all", "about", "my", "disease,", "and","do", "not", "know", "for", "certain", "what", "ails", "me."]

word_counts should then be {"sick": 1, "man.": 3, "at": 1, "what": 1, "nothing": 1, "do": 1, "is": 1, "me.": 1,"I": 5, "ails": 1, "an": 1, "am": 3, "know": 2, "disease,": 1, "not": 1, "liver": 1,"believe": 1, "all": 1, "my": 2, "certain": 1, "However,": 1, "and": 1, "for": 1,"unattractive": 1, "spiteful": 1, "about": 1, "a": 2, "diseased.": 1}

For example, the word "man." (with the period at the end) appears 3 times in the text, so its entry in the dictionary word_counts is 3."""

word_counts = {}
for word in text:
    if word in word_counts.keys():
        word_counts[word] += 1
    else:
        word_counts[word] = 1
        

"""PART B:
Write a function with the signaturetop10(L)that takes in a list L of 100 different integers, and returns a list of the 10 largest integers in L."""

def radix_sort(L, reduced=None, base=10):
    """Performs LSD Radix Sort on the list

    Args:
        L (list of integers): The list to be sorted
        reduced (list of integers, optional): L after iterations are performed. Defaults to None.
        base (integer, optional): The base of LSD Radix sort to perform. Defaults to 10.
    """
    if reduced is None:
        reduced = L
    sort = [[] for _ in range(base)]
    for i in range(len(L)):
        number = reduced[i]%base
        sort[number].append(L[i])
    for i in range(base):
        if len(sort[i]) > 1:
            sort[i] = radix_sort(sort[i], [number//base for number in sort[i]], base)
    
    return sort


def top10(L):
    """Return the top ten largest integers in the list L

    Args:
        L (list): one hundred integers 
    """
    return sorted(L)[:10]

"""Now, obtain the top 10 most-frequent words from the dictionary freq.  To do that, you need to sort the data by the word counts. You cannot sort dictionaries directly, but you can use the following trick:

inv_freq = {6: "the", 12: "a", 1:"hi"} 
print(sorted(inv_freq.items()))

First,  experiment  with  this  code  and  understand  what  it  is  doing,  and  then  apply  the  technique  tofinding the top 10 most frequent words.  Test your function by creating a small text file where you can findthe top n most-frequent words manually, running your code on this file, and comparing the results.  Then, download the text of Pride and Prejudice from http://www.gutenberg.org/files/1342/1342-0.txt and obtain the top 10 most frequent words in Pride and Prejudice."""

def top10words(freq):
    return sorted([(value, key) for key, value in freq.items()])[:-10:-1]

"""Problem 3"""
# digits = frozenset(digits)
# f = urlopen("http://www.cs.toronto.edu/~guerzhoy/180/draft/draft.html")
# page = f.read().decode("utf-8")
# f.close()
# print(page)
dictionary = open("dictionary.txt").read().split()
def search_yahoo(term):
    term = term.replace(" ", "+")
    page = urlopen(f"https://ca.search.yahoo.com/search?p={term}&fr=yfp-t&fp=1&toggle=1&cop=mss&ei=UTF-8").read().decode("utf-8")
    print(page)


def get_yahoo_search_results(term, start=0):
    term = term.replace(" ", "+")
    page = urlopen(f"https://ca.search.yahoo.com/search?p={term}&fr=yfp-t&fp=1&toggle=1&cop=mss&ei=UTF-8").read().decode("utf-8")[start:]
    for num in range(10):
        index = page.find(f"{num} result")
        if index >= 0:
            break
    if index < 0:
        return 0
    num_results = page[index-13:index+1]
    if num_results.find(",") >= 0:
        # print(page[index-13:index+10])
        return int("".join(c for c in num_results if c in digits))
    return get_yahoo_search_results(term, index)

def choose_variant(varients):
    with ThreadPoolExecutor(max_workers=32) as executor:
        results = np.array(list(executor.map(get_yahoo_search_results, varients)))
    print(results)
    return varients[np.argmax(results)]


"""https://ca.search.yahoo.com/search?p=engineering+science&fr=yfp-t&fp=1&toggle=1&cop=mss&ei=UTF-8"""
if __name__ == "__main__":
    print(choose_variant(["top ranked school uoft", "top ranked school waterloo"]))
    # print(top10words(word_counts))
