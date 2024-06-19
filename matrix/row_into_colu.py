# convert row into column and column into row
# a=[[1,2,3],[4,5,6],[7,8,9]] => a=[[1,4,7],[2,5,8],[3,6,9]]

def conver_row_in_cols(a):
    return [[row[i] for row in a] for i in range(len(a[0]))]

a = [[1,2,3],[4,5,6],[7,8,9]]
print(conver_row_in_cols(a)) 