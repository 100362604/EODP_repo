#toa_out = np.zeros(toa.shape)

#for ialt in range(toa.shape[0]):
#    toa_out[ialt, :] = (toa[ialt, :] - eq_add) / eq_mult

#return toa_out

import numpy as np

#Operaciones con las filas
matrix = np.zeros((5,10))
matrix2 = np.zeros((5,10))
vec1 = np.ones(10)
vec2 = np.array(range(10))

print(matrix)
print(matrix.shape[0])
print(matrix.shape[1])
print(vec1)
print(vec2)

for i in range(matrix.shape[0]):
    matrix2[i,:] = matrix[i,:] + vec1 + vec2

print(matrix2)

#Operaciones con las filas
matrix3 = np.zeros((5,10))
vec3 = np.ones(5)
vec4 = np.array(range(5))

for j in range(matrix.shape[1]):
    matrix3[:,j] = matrix[:,j] + vec3 + vec4

print(matrix3)


