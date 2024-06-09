# Input: arr[] = {6, -3, -10, 0, 2}
# Output:  180
# Explanation: The subArray is {6, -3, -10}

# Input: arr[] = {-1, -3, -10, 0, 60}
# Output:   60
# Explanation: The subArray is {60}

def Maximum_Product_SubArray(a):
    curr_sum, max_sum = 1, 1
    flag = False 

    for i in range(len(a)):
        if(curr_sum < a[i] or flag):
            flag = True
            curr_sum *= a[i]
            if max_sum < curr_sum:
                max_sum = curr_sum
    return max_sum

a = [6,-3, -10, 0, 2]
print(Maximum_Product_SubArray(a))
a = [-1,-3, -10, 0,60]
print(Maximum_Product_SubArray(a))