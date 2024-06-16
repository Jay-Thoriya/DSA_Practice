'''
Given a boolean matrix mat[M][N] of size M X N, modify it such that if a matrix cell mat[i][j] is 1 (or true)
then make all the cells of ith row and jth column as 1.

Input: {{1, 0},
           {0, 0}}
Output: {{1, 1}
              {1, 0}}


Input: {{0, 0, 0},
            {0, 0, 1}}
Output: {{0, 0, 1},
               {1, 1, 1}}
 

Input: {{1, 0, 0, 1},
           {0, 0, 1, 0},
          {0, 0, 0, 0}}
Output: {{1, 1, 1, 1},
               {1, 1, 1, 1},
              {1, 0, 1, 1}}

'''

def modifyMatrix(matrix):
    m, n = len(matrix), len(matrix[0])
    new_matrix = [[0 for column in range(0,n)] for row in range(0,m)]
    for i in range(0,m):
        for j in range(0,n):
            if matrix[i][j] == 1:
                for k in range(n):
                    new_matrix[i][k] = 1
                for k in range(m):
                    new_matrix[k][j] = 1
    return new_matrix

a = [[1,0],[0,0]]
print(modifyMatrix(a))

b = [[0,0,0],[0,0,1]]
print(modifyMatrix(b))

c = [[1,0,0,1],[0,0,1,0],[0,0,0,0]]
print(modifyMatrix(c))