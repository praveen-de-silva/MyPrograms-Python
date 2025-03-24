def matMult(mat1, mat2):
    '''Multiply two matrices'''
    rows_mat1 = len(mat1)
    cols_mat1 = len(mat1[0])  
    rows_mat2 = len(mat2)
    cols_mat2 = len(mat2[0])  

    # Check if multiplication is possible
    if cols_mat1 != rows_mat2:
        raise ValueError("Matrix multiplication not possible: Columns of first matrix must match rows of second matrix.")

    # Initialize result matrix with zeros
    result = [[0 for _ in range(cols_mat2)] for _ in range(rows_mat1)]

    # Perform multiplication
    for i in range(rows_mat1):
        for j in range(cols_mat2):
            for k in range(cols_mat1):  # Same as rows_mat2
                result[i][j] += mat1[i][k] * mat2[k][j]

    return result


def minor(mat, i_ignore, j_ignore):
    '''find the minor'''
    mat_size = len(mat) # no of rows (or columns)
    new_mat = []

    for i in range(mat_size):
        if i==i_ignore: # iqnore the row
            continue
        
        new_row = []

        for j in range(mat_size):
            if j==j_ignore: # iqnore the column
                continue
            
            new_row.append(mat[i][j])         
        new_mat.append(new_row)
    return new_mat

def coFact(mat, i, j):
    '''find the cofactor'''
    return (-1)**(i+j+2) * det(minor(mat, i, j))

def det(mat):
    '''find the determinent value'''
    mat_size = len(mat)
    
    if mat_size==1:
        return mat[0][0]

    det_val = 0

    for j in range(mat_size):
        det_val += mat[0][j] * coFact(mat, 0, j)

    return det_val
        
def transpose(mat):
    '''find the transpose of the matrix'''
    mat_size = len(mat)
    new_mat = []

    for j in range(mat_size):
        new_row = []
        
        for i in range(mat_size):
            new_row.append(mat[i][j])
        new_mat.append(new_row)
    return new_mat

def matScalDiv(mat, div_val):
    '''scaler division of the matrix'''
    new_mat = mat[:]
    mat_size = len(new_mat)

    for j in range(mat_size):
        for i in range(mat_size):
            if new_mat[i][j]==0:
                new_mat[i][j] = 0 # to avoid printing '0.00' as '-0.00'
            else:
                new_mat[i][j] = new_mat[i][j]/div_val # each value is devided by the determinant
    return new_mat

def adjoint(mat):
    '''find the adjoint of a matrix'''
    mat_size = len(mat)
    new_mat = [] # to contain new rows

    for i in range(mat_size):
        new_row = [] # to contain new values
        
        for j in range(mat_size):
            temp_val = coFact(mat, i, j)
            new_row.append(temp_val)
        new_mat.append(new_row)

    res_mat = transpose(new_mat)
    return res_mat # ADJOINT = TRANSEPOSE( COFACTOR MATRIX )

def inverse(mat):
    '''find the inverse of a matrix'''
    mat_adj = adjoint(mat)
    mat_det = det(mat)
    return matScalDiv(mat_adj, mat_det) # INVERSE = ADJOINT / DETERMINENT

def readData(file_inp_name):
    '''read data and returns the matrices'''
    file_inp = open(file_inp_name, 'r')
    count_matrices = int(file_inp.readline())
    matrices = []

    for _ in range(count_matrices):
        mat_size = int(file_inp.readline())
        mat = []

        for _ in range(mat_size):
            row = list(map(int, file_inp.readline().strip().split(',')))
            mat.append(row)
        matrices.append(mat)
    return matrices   

def makeMatPrint(mat, mat_no):
    '''making a string to present the matrix'''
    mat_str = f'Inverse of Matrix {mat_no}:'

    for row in mat:
        mat_str += '\n' + ' '.join([f'{val:7.2f}' for val in row])   
    return mat_str
    
    
##if __name__=='__main__':
##    matrices = readData('matrix_data.txt') # read the data

##    for i in range(len(matrices)):
##        mat_str = makeMatPrint(matrices[i], i+1)
##        print(mat_str)

    


matA = [
    [16,10,4],
    [10,21,-5],
    [2,-6,-8]
]

matA_inv = inverse(matA)

matB = [
    [1],
    [1],
    [0]
]

result = matMult(matA_inv, matB)

matA_inv_str = makeMatPrint(result, 1)

print(matA_inv_str)




