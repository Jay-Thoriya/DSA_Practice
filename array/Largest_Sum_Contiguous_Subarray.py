# Input: arr = {-2,-3,4,-1,-2,1,5,-3}
# Output: 7
# Explanation: The subArray {4,-1, -2, 1, 5} has the largest sum 7.

# Input: arr = {2}
# Output: 2
# Explanation: The subArray {2} has the largest sum 1.


# Input: arr = {5,4,1,7,8}
# Output: 25
# Explanation: The subArray {5,4,1,7,8} has the largest sum 25.

def Largest_Sum_Contiguous_SubArray(a):
    curr_sum, max_sum = 0, 0
    flag = False 

    for i in range(len(a)):
        if(curr_sum < a[i] or flag):
            flag = True
            curr_sum += a[i]
            if max_sum < curr_sum:
                max_sum = curr_sum
    return max_sum

a = [-2,-3,4,-1,-2,1,5,-3]
print(Largest_Sum_Contiguous_SubArray(a))
a =[2]
print(Largest_Sum_Contiguous_SubArray(a))
a=[5,4,1,7,8]
print(Largest_Sum_Contiguous_SubArray(a))