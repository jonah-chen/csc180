import numpy as np

# Problem 1:


def power(x, n):
    if n <= 1:
        return x
    return x*power(x, n-1)

# Problem 2:


def interleave(L1, L2):
    if len(L1) == 0:
        return []
    if len(L1) == 1:
        return [L1[0], L2[0]]
    return [L1[0], L2[0]] + interleave(L1[1:], L2[1:])

# Problem 3


def reverse_rec(L, n=0):
    if n >= len(L)//2:
        return
    L[n], L[-n-1] = L[-n-1], L[n]
    reverse_rec(L, n+1)
    return

# Problem 4


def zigzag(L, n=0):
    if (n == 0):
        print(L[len(L)//2], end=" ")
        zigzag(L, n+1)
        return
    print(L[len(L)//2-n], end=" ")
    print(L[len(L)//2+n], end=" ")

    if (n == len(L)//2):
        return
    zigzag(L, n+1)

# Problem 5


def is_balanced(s):
    if s[0] != "(" and s[0] != ")":
        return is_balanced(s[1:])
    if s[0] == ")":
        return False
    if s[0] == "(" and s[-1] == ")":
        return is_balanced(s[1:-1])

if __name__ == "__main__":
    list1 = list(np.arange(101))
    zigzag(list1)
