import numpy as np

# Question 1
def print_matrix(M_lol):
    M_out = np.array(M_lol)
    print(M_out)
    
# Question 2
def get_lead_ind(row):
    for i in range(len(row)):
        if row[i] != 0:
            return i
    return len(row)

# Question 3
def get_row_to_swap(M, start_i):
    '''Returns the index of the row needed to be swapped with row M[start_i]
    '''
    lead_index = get_lead_ind(M[start_i])
    index = start_i
    for i in range(start_i, len(M)):
        if get_lead_ind(M[i]) < lead_index:
            lead_index = get_lead_ind(M[i])
            index = i
    return index

# Question 4
def add_rows_coefs(r1, c1, r2, c2):
    outList = [0] * np.size(r1)
    for i in range(len(r1)):
        outList[i] = (c1 * r1[i]) + (c2 * r2[i])
    return outList

# Question 5
# Come back to this one later!
def eliminate(M_elim, row_to_sub, best_lead_ind):
    N = M_elim
    for i in range(row_to_sub + 1, len(M_elim)):
        for j in range(best_lead_ind, len(M_elim[0])):
            print("i:" + str(i) + "j:" + str(j))
            N[i][j] = M_elim[i][j] - (M_elim[row_to_sub][j] * (float(M_elim[i][best_lead_ind]) / float(M_elim[row_to_sub][best_lead_ind]) ) )
    return N

# Question 6
# def forward_step(M):
    
        
if __name__ == "__main__":
    
    #Define Matrix M
    M = [[5,6,7,8],
         [0,0,1,1],
         [0,0,5,2],
         [0,0,7,0]]
    
    # Test Question 1
    print_matrix(M)
    
    # Test Question 2
    print(get_lead_ind(M[2]))
    
    # Test Question 3
    print(get_row_to_swap(M,3))
    
    # Test Question 4
    print_matrix(add_rows_coefs(M[0],2,M[1],1))
    
    # Test Question 5
    print_matrix(eliminate(M,1,2))

    #Test Question 6
    