import numpy as np

print("--SVD--")

A=np.array([[1,2,3],[4,5,6],[7,8,9]])

print("A:",A)

U,D,VT=np.linalg.svd(A)

print(U)

print(D)

print(VT)

print("\n--REMAKE--")

A_R=(U@np.diag(D)@VT)

print(A_R)
