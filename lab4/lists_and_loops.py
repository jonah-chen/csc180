import numpy as np 

# Problem 1
def list1_starts_with_list2(list1, list2):
    if len(list1) < len(list2):
        return False
    for j in np.arange(len(list2)):
        if list1[j] != list2[j]:
            return False
    return True


# Problem 2
def match_pattern(list1, list2):
    for i in range(len(list1)-len(list2)):
        boolVar = True
        for j in range(len(list2)):
            if list2[j] != list1[j+i]:
                boolVar = False
        if boolVar == True:
            return True
    return False

# Problem 3
def repeats(list0):
    for i in range(len(list0)-1):
        if list0[i] == list0[i+1]:
            return True
    return False

# Problem 4
# a
def print_matrix_dim(M):
    print(f'{len(M)}x{len(M[0])}')

def mult_M_v(M, v):
    D = [0]*len(M)
    for j in np.arange(len(M)):
        for k in np.arange(len(v)):
            D[j] += M[j][k] * v[k]
    return D

def check(D, M, v):
    M = np.array(M)
    v = np.array(v)
    E = M.dot(v)
    D = np.array(D)
    print(E)
    print(D)
    print(f'{E==D}')

#c

# how does this work? ten_zeros1 = [0]*10

def mult_M_N(M,N):
    D = list(np.zeros((len(M), len(N[0],))))
    print(np.array(D))
    for i in np.arange(len(M)):
        for j in np.arange(len(N)):
            for k in np.arange(len(N[0])):
                D[i][k] += M[i][j] * N[j][k]
    return D

def checkC(D,M,N):
    D, M, N = np.array(D), np.array(M), np.array(N)
    E = np.matmul(M,N)
    print(D)
    print(E)
    print(D==E)

if __name__=='__main__':
    M = [[1,2],[3,5]]
    v = [1,2]
    checkC(mult_M_N(M, M), M, M)