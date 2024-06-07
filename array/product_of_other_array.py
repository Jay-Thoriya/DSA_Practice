# Input: arr[]  = {10, 3, 5, 6, 2}
# Output: prod[]  = {180, 600, 360, 300, 900}
# 3 * 5 * 6 * 2 product of other array 
# elements except 10 is 180
# 10 * 5 * 6 * 2 product of other array 
# elements except 3 is 600
# 10 * 3 * 6 * 2 product of other array 
# elements except 5 is 360
# 10 * 3 * 5 * 2 product of other array 
# elements except 6 is 300
# 10 * 3 * 6 * 5 product of other array 
# elements except 2 is 900


# Input: arr[]  = {1, 2, 3, 4, 5}
# Output: prod[]  = {120, 60, 40, 30, 24 }
# 2 * 3 * 4 * 5  product of other array 
# elements except 1 is 120
# 1 * 3 * 4 * 5  product of other array 
# elements except 2 is 60
# 1 * 2 * 4 * 5  product of other array 
# elements except 3 is 40
# 1 * 2 * 3 * 5  product of other array 
# elements except 4 is 30
# 1 * 2 * 3 * 4  product of other array 
# elements except 5 is 24


def product_of_other_array(a,n):
    counter = 0
    result = []
    for i in range(n):
        prod = 1
        for j in range(n):
            if(counter != j):
                prod = prod*a[j]
        result.append(prod)
        counter+=1
    return result

a = [10, 3, 5, 6, 2]
n = len(a)
a1 = [1,2,3,4,5]
n1 = len(a1)
print(product_of_other_array(a,n))
print(product_of_other_array(a1,n1))