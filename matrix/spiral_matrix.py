"""
Input:  {{1,    2,   3,   4},
              {5,    6,   7,   8},
             {9,   10,  11,  12},
            {13,  14,  15,  16 }}
Output: 1 2 3 4 8 12 16 15 14 13 9 5 6 7 11 10

Input: { {1,   2,   3,   4,  5,   6},
           {7,   8,   9,  10,  11,  12},
          {13,  14,  15, 16,  17,  18}}


Output: 1 2 3 4 5 6 12 18 17 16 15 14 13 7 8 9 10 11

"""

def spiral_matrix(matrix):
    row,cols = len(matrix) , len(matrix[0])
    top, bottom, left, right = 0, row-1, 0, cols-1
    result = []

    while len(result) < cols*row:
        print('result = ',result)
        for i in range(left, right+1):
            result.append(matrix[top][i])
        top+=1

        for i in range(top, bottom+1):
            result.append(matrix[i][right])
        right-=1

        if top <= bottom:
            for i in range(right, left-1, -1):
                result.append(matrix[bottom][i])
            bottom-=1

        if left <= right:
            for i in range(bottom, top-1, -1):
                result.append(matrix[i][left])
            left+=1
    return result


a = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
print(spiral_matrix(a))
