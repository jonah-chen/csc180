import numpy as np

def most_productive_elf(toys_produced):
    best_elf, best_n = None, -1
    for (key, value) in toys_produced:
        if value > best_n:
            best_elf, best_n = key, value
    return best_elf


def two_smallest(L):
    sorted(L)
    return [L[1], L[0]]

# O(n log n)


def largest_col_sum(M):
    n = len(M[0])
    _sum = 0

    for i in range(n):
        _sum += M[0][i]

    for i in range(n):
        __sum = 0
        for j in range(len(M)):
            __sum += M[j][i]
        if __sum > _sum:
            _sum = __sum

    return _sum


def filter_out_odds(L):
    if len(L) == 0:
        return []
    if L[0]%2 == 1:
        return filter_out_odds(L[1:])
    return [L[0]] + filter_out_odds(L[1:])


if __name__ == "__name__":
    
