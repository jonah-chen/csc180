import numpy as np

# Part 1
def sum_nums(L):
    s = 0
    for num in L:
        s += num

    return s

def count_evens(L):
    '''returns the number of even integers in the list L (A List of Integers)
    '''
    c = 0
    for num in L:
        if num % 2 == 0:
            c += 1

    return c

# Part 2
def list_to_str(lis):
    '''Without using str() with arguments that are lists (using it with arguments that are not lists is fine),
    write a function with the signature list_to_str(lis) which returns the string representation of the list lis.
     You may assume lis only contains integers.
     '''
    s = ''
    for num in lis:
        s = f'{s}, {num}'

    return f'[{s[1:]}]'

# Part 3
def list_are_the_same(list1, list2):
    '''Without using the == operator to compare lists
    returns True iff list1 and list2 contain the same elements in the same order
    '''
    if len(list1) != len(list2):
        return False
    for i in np.arange(len(list1)):
        if list1[i] == list2[i]:
            return False
    return True

# Part 4
def simplify_fraction(n, m):
    '''prints the simplified version of the fraction n/m
    '''
    for i in np.arange(2, np.min([n, m])//2):
        if n % i == 0 and m % i == 0:
            simplify_fraction(n//i, m//i)
            return
    print(f'{n}/{m}')

# Part 5
def dig():
    res1 = 0
    res2 = 0
    dig1 = 0
    dig2 = 0
    iter = 0
    while True:
        iter += 1
        if iter % 2 == 0:
            res1 -= 4 / (iter * 2 - 1)
        else:
            res1 += 4 / (iter * 2 - 1)
        res2 += np.power(iter, -4.0)

        while int(res1*np.power(10,dig1)) == int(np.pi*np.power(10,dig1)):
            dig1+=1
            print(f'leibniz predicted pie to {dig1-1} decimal places in {iter} iterations\n{res1}\n')
        while int(np.power(90 * res2, 0.25)*np.power(10,dig2)) == int(np.pi*np.power(10,dig2)):
            dig2+=1
            print(f'riemann predicted pie to {dig2 - 1} decimal places in {iter} iterations\n{np.power(90 * res2, 0.25)}\n')

        if iter%500000==0:
            print(f'{iter/1000000}M iterations have been executed. leibniz is wrong by {np.abs(res1-np.pi)}; riemann is wrong by {np.abs(np.power(90 * res2, 0.25)-np.pi)}')

# Part 6
def euclid(n, m): # m > n
    r = m % n
    if r == 0:
        return n
    return euclid(r, n)

if __name__=='__main__':
    print(euclid(10,75))