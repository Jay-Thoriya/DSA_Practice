# Input: arr[] = {0, -1, 2, -3, 1}
# Output: (0 -1 1), (2 -3 1)
# Explanation: The triplets with zero sum are 0 + -1 + 1 = 0 and 2 + -3 + 1 = 0  

# Input: arr[] = {1, -2, 1, 0, 5}
# Output: 1 -2  1
# Explanation: The triplets with zero sum is 1 + -2 + 1 = 0  

def triple_sum_zero(arr):
    arr.sort()
    for i in range(len(arr)-2):
        left = i+1
        right = len(arr)-1
        while left < right:
            if arr[i] + arr[left] + arr[right] == 0:
                print([arr[i],arr[left],arr[right]])
                right -=1
                left +=1
            elif arr[i] + arr[left] + arr[right] < 0:
                left +=1
            elif arr[i] + arr[left] + arr[right] > 0:
                right -=1

a = [0, -1, 2, -3, 1]
triple_sum_zero(a)
a = [1, -2, 1, 0, 5]
triple_sum_zero(a)