# Input: arr[] = {5, 6, 1, 2, 3, 4}
# Output: 1
# Explanation: 1 is the minimum element present in the array.

# Input: arr[] = {1, 2, 3, 4}
# Output: 1


# Input: arr[] = {2, 1}
# Output: 1

#there are two ways to do this

#first way using sorted methods 
def minValue_using_sort(arr):
    arr.sort()
    return arr[0]

#second way without using sorted methods
def minValue_using_without_sort(arr):
    minVal = arr[0]
    for i in range(len(arr)):
        if arr[i] < minVal:
            minVal = arr[i]
    return minVal

arr = [1, 2, 3, 4]
print(minValue_using_sort(arr))
print(minValue_using_without_sort(arr))

arr = [5, 6, 1, 2, 3, 4]
print(minValue_using_sort(arr))
print(minValue_using_without_sort(arr))

arr = [2,1]
print(minValue_using_sort(arr))
print(minValue_using_without_sort(arr))