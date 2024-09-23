def minor(mat, i_ignore, j_ignore):
    mat_size = len(mat)
    new_mat = []

    for i in range(mat_size):
        if i==i_ignore:
            continue
        
        new_row = []

        for j in range(mat_size):
            if j==j_ignore:
                continue
            
            new_row.append(mat[i][j])         
        new_mat.append(new_row)
    return new_mat

def coFact(mat, i, j):
    return (-1)**(i+j+2) * det(minor(mat, i, j))

def det(mat):
    mat_size = len(mat)
    
    if mat_size==1:
        return mat[0][0]

    det_val = 0

    for j in range(mat_size):
        det_val += mat[0][j] * coFact(mat, 0, j)

    return det_val
        
def transpose(mat):
    mat_size = len(mat)
    new_mat = []

    for j in range(mat_size):
        new_row = []
        
        for i in range(mat_size):
            new_row.append(mat[i][j])
        new_mat.append(new_row)
    return new_mat

def matScalDiv(mat, div_val):
    new_mat = mat[:]
    mat_size = len(new_mat)

    for j in range(mat_size):
        for i in range(mat_size):     
            new_mat[i][j] = round(new_mat[i][j]/div_val, 2)
    return new_mat

def adjoint(mat):
    '''find the adjoint of a matrix'''
    mat_size = len(mat)
    new_mat = [] # to contain new rows

    for i in range(mat_size):
        new_row = [] # to contain new values
        
        for j in range(mat_size):
            temp_val = coFact(mat, j, i) # to get the traspose of the cofactor matrix : (i,j) --> (j,i)
            new_row.append(temp_val)
        new_mat.append(new_row)
    return new_mat 

def inverse(mat):
    '''find the inverse of a matrix'''
    mat_adj = adjoint(mat)
    mat_det = det(mat)
    return matScalDiv(mat_adj, mat_det)



matA = [[2,3,4], [4,3,1], [1,2,4]]
matA_inverse = inverse(matA)

print(matA_inverse)
