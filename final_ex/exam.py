# ESC180 Final Examination, Fall 2020
#
# Aids allowed: the ESC180 website, a Python IDE. You must *not* use any other
# notes or internet website. You may must not communicate about the exam except
# to ask questions on Piazza.
#
# You may ask questions on the course Piazza. Please make your question private
# if it must disclose part of the solution. Otherwise, please make it public.
# Please check Piazza occasionally in case there are announcements or
# clarifications.
#
# You have 2.5 hours to work on the exam, and 30 minutes to submit it. You may
# keep writing the exam during the submission window, but it is your
# responsibility to make sure that the exam is submitted before the submission
# window closes. Late submissions will only be accepted from students who
# have been preapproved for a time extension through accessibility services.
#
# To be eligible to receive partial credit, you must submit a file which does
# not produce an error when read into Python. Any code that you know produces
# errors must be commented out. By themselves, comments/docstrings will not
# earn any points. However, they may help TAs in deciding how to award
# partial credit.
#
# Unless otherwise specified, you may import math and numpy, but not other
# modules.
#
import numpy as np
################################################################################

#    Problem 1 (25 pts)
#
#    Up to 5 points will be awarded for making progress toward a correct
#    solution.
#
#    Assume you are given a list of filenames of text files. Assume
#    that the text files only contain the punctuation
#    [".", ",", "!", "?", "-"].
#    The files may also contain the newline character "\n".
#
#    For each file, there is a word that occurs in that file the most often --
#    the most frequent word. We want to find the word that is the most frequent
#    word in the most files.
#    Write a function that takes in a list of file names, and returns the word
#    that is the most frequent word in the most files. You can assume that there
#    are no ties: each file has one word that is the most frequent, and there
#    is one word that is the most frequent word in the most files.
#    For example, the function might be called as follows:
#
#    most_common_frequent_word(["diseases/" + filenames[0],
#                                "diseases/" + filenames[1],
#                                "diseases/" + filenames[2])
#    If the most frequent word in filesnames[0] is "a", the most frequent word in
#    filenames[1] is "the", and the most frequent word in filenames[2] is
#    "the", most_common_frequent_word should return "the"                               .
#    A non-word, such as "<a", would be considered a valid word for the files
#    given to you.
#
#    The words "Dog" and "dog" should be considered to be the same when computing
#    the frequency of words. The words "dogs" and "dog" should be considered
#    to be different.
#
#    You are encouraged to use helper functions.
#
#    For this problem, you may *not* import any Python modules.

def most_common_frequent_word(files):
    """Returns the most frequent word in the most files from the list "files" assuming there are no ties.

    Args:
        files (list): list of file paths
    """
    return most_common(map(most_common_word, files))
        

def most_common_word(_file):
    f = open(_file)
    text = f.read()
    f.close()
    z = text.replace(".", " ").replace(",", " ").replace("!", " ").replace("?", " ").replace("-", " ").replace("\n", " ").lower()
    words = z.split()
    return most_common(words)
    

def most_common(words):
    occurence_list = {}
    for word in words:
        if word in occurence_list:
            occurence_list[word] += 1
        else:
            occurence_list[word] = 1
    common = sorted([(occurence, word) for (word, occurence) in occurence_list.items()])[::-1]
    return common[0][1]



################################################################################

#    Problem 2 (20 pts)
#
#    This problem will be auto-graded.
#
#
#    Recall that links in an html file are given in the format
#    <a href = "http://engsci.utoronto.ca">EngSci homepage</a>
#    Write a function that takes in the text of an html file, and returns a dictionary
#    whose keys are the link texts (e.g. "EngSci homepage") and whose values are
#    the corresponding URLs (e.g., "http://engsci.utoronto.ca"). You can assume
#    that link texts do not repeat.
#    Sample call:
#     get_links('<a href = "http://engsci.utoronto.ca">EngSci homepage</a>')
#    should return {"EngSci homepage": "http://engsci.utoronto.ca"}


def get_links(html_text):
    dic = {}
    while 1:
        v_start = html_text.find("<a href = \"") + 11
        if v_start == 10:
            return dic
        v_end = html_text.find("\">", v_start)
        k_start = v_end + 2
        k_end = html_text.find("</a>", k_start)
        dic[html_text[k_start:k_end]] = html_text[v_start:v_end]
        html_text = html_text[k_end:]

###############################################################################

#   Problem 3 (10 pts)
#
#    Without using for-loops or while-loops, write  function for which
#    the tight asymptotic bound on the runtime complexity is O((n^2)*log(n)).
#    You may create helper functions, as long as they also do not use while-
#    and for-loops.
#    Justify your answer in a comment. The signature of the function must be

def log(n, nr):
    if nr == 0:
        return
    x = 1
    del x
    return log(n, nr//2)

def lin(n, nr):
    if nr == 0:
        return
    log(n, n)
    return lin(n, nr-1)

def quad(n, nr):
    if nr == 0:
        return
    lin(n, n)
    return quad(n, nr-1)

def f(n):
    """This method executes in O(n^2 log n) time"""
    return quad(n, n)
    



###############################################################################

# The first function `log(n,nr)` execute a O(1) operation of assigning and deleting a variable x O(log(nr)) times 
# as nr gets integer divided by 2 each time until it reachese the base case of nr=0.
# Thus, this function's runtime complexity is O(log(nr))
# 
# The second function `lin(n,nr)` executes `log(n=n,nr=n)` every time it is called; thus taking O(log n) time. 
# Since 1 is subtracted from nr each time until reaching the base case of nr=0, this function is called nr times before it returns.
# Thus, each execution of this function is O(nr log(n)) runtime complexity.
# 
# Similarly, the third function `quad(n,nr)` executes `lin(n=n,nr=n)` every time it is called. 
# Similar to the second function, this function is also called nr times; hence, its runtime complexity is O(nr*n log(n))
# 
# f(n) calls quad(n=n,nr=n); thus, its runtime complexity is O(n^2 log(n))  



###############################################################################
#  Problem 4 (15 pts)
#
#  This problem will be auto-graded.
#
#
#  It is possible to combine the numbers 1, 5, 6, 7 with arithemtic operations
#  to get 21 as follows: 6/(1-5/7).
#
#  Write a function that takes in a list of three numbers and a target number, and
#  returns a string that contains an expression that uses all the numbers
#  in the list once, and results in the target. Assume that the task is possible
#  without using parentheses.
#
#  For example, get_target_noparens([3, 1, 2], 7) can return "2*3+1" or "1+2*3"
#  (either output would be fine).
#
#

def get_target_noparens(nums, target):
    ops = ["+", "-", "*", "/"]
    for i in range(3):
        for j in range(3):
            if i != j:
                for op1 in ops:
                    for op2 in ops:
                        k = list(range(3))
                        k.remove(i)
                        k.remove(j)
                        k = k[0]
                        op = f"{nums[i]}{op1}{nums[j]}{op2}{nums[k]}"
                        try:
                            if eval(op) == target:
                                return op                
                        except ZeroDivisionError:
                            pass


################################################################################
#  Problem 5 (15 pts)
#
#  Up to 3 pts will be awarded for making progress toward a solution.
#
#  Now, write the function get_target which returns a string that contains an
#  expression that uses all the numbers in the list once, and results in the
#  target. The expression can contain parentheses. Assume that the task is
#  possible.
#  For example, get_target([1, 5, 6, 7], 21) can return "6/(1-5/7)"

def get_permutations(nums):
    """Generates all permutations of three numbers"""
    if len(nums) == 0:
        return []
    if len(nums) == 1:
        return [nums[0]]
    perms = []
    for i in range(len(nums)):
        # return a any of these as first element + the others
        others = get_permutations(nums[:i]+nums[i+1:])
        for o in others:
            try:
                p = [nums[i]] + o
            except TypeError:
                p = [nums[i]] + [o]
            perms.append(p)
    return perms

operations = []
def get_operations(n, start_str = ""):
    """Generates all possible operations that can be used"""
    global operations
    if n == 0:
        operations.append(start_str)
        return
    for letter in "+-*/":
        get_operations(n-1, start_str+letter)


def get_target(nums, target):
    global operations

    if len(nums) <= 1:
        return nums[0]

    numbers = len(nums)
    permutations = get_permutations(nums)
    operations = []
    get_operations(len(nums)-1)
    asdfg = 0
    while 1:
        for p in permutations:
            for op in operations:
                s = ""
                asdf = asdfg
                if asdf%2==0:
                    s += "("
                asdf//=2
                s += str(p[0])
                for i in range(1, numbers):
                    if asdf%2==0:
                        s += ")"
                    asdf//=2
                    s += f"{op[i-1]}"
                    if asdf%2==0:
                        s += "("
                    asdf//=2
                    s += f"{p[i]}"
                if asdf%2==0:
                    s+= ")"
                    asdf//=2
                try:
                    if eval(s) == target:
                        return s
                except ZeroDivisionError:
                    pass
                except SyntaxError:
                    pass
        asdfg += 1



################################################################################

if __name__ == "__main__":
    # print(get_permutations([1,2,3,4]))
    get_operations(10)
    # print(operations)
    print(get_target([3, 1, 2, 5], 7))
    print(get_target([1, 5, 6, 7], 21))
