A = [[2,0,-1], [1,3,-2]]
B = [[0,-1,1,0], [2,3,-1,4], [-3,0,-2,1]]
def mul_matrix(A,B):
    C = [[0 for i in range(len(B[0]))] for i in range(len(A))]
    for i in range(len(A)):
        for j in range(len(B[0])):
                for k in range(len(B)):
                    C[i][j] += A[i][k] + B[k][j]
                    
    return C
print(mul_matrix(A,B))