import numpy as np
from scipy.sparse import csr_matrix

rows = 10
columns = 490
sparse_matrix = np.zeros((rows, columns))

for i in range(rows):
    for j in range(columns):
        if i == j:
            sparse_matrix[i][j] = 1

sparse_matrix_csr = csr_matrix(sparse_matrix)

def sparse_matrix_size(matrix):
    return matrix.nbytes

def csr_matrix_size(csr):
    data_size = csr.data.nbytes
    indices_size = csr.indices.nbytes
    indptr_size = csr.indptr.nbytes
    return data_size + indices_size + indptr_size

sparse_size = sparse_matrix_size(sparse_matrix)
csr_size = csr_matrix_size(sparse_matrix_csr)
diff = sparse_size - csr_size
diff_percentage = round(100*diff/sparse_size,2)

print(f"Sparse matrix size: {sparse_size} bytes")
print(f"CSR matrix size: {csr_size} bytes")
print(f"Saving: {diff_percentage} %")