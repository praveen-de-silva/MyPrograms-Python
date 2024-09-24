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
            new_mat[i][j] = round(new_mat[i][j]/div_val, 5)
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



matA = [
    [2, 80, 97, 74, 44, 9, 1, 81, 17, 75],
    [80, 97, 40, 47, 4, 31, 64, 60, 75, 87],
    [44, 26, 65, 47, 39, 72, 32, 50, 21, 53],
    [35, 44, 44, 81, 70, 62, 72, 60, 98, 34],
    [96, 25, 83, 19, 32, 44, 63, 43, 57, 53],
    [89, 40, 70, 71, 7, 26, 60, 85, 62, 93],
    [35, 77, 44, 81, 50, 25, 28, 41, 93, 24],
    [40, 23, 3, 87, 67, 18, 39, 26, 54, 1],
    [39, 80, 78, 76, 26, 57, 12, 10, 85, 73],
    [56, 80, 63, 62, 19, 98, 95, 35, 88, 7]
]
matA_inverse = inverse(matA)

print(matA_inverse)
