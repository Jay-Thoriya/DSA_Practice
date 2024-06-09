'''
Input : arr[] = {7, 3, 2, 4, 9, 12, 56} , m = 3 
Output: Minimum Difference is 2 
Explanation:
We have seven packets of chocolates and we need to pick three packets for 3 students 
If we pick 2, 3 and 4, we get the minimum difference between maximum and minimum packet sizes.

Input : arr[] = {3, 4, 1, 9, 56, 7, 9, 12} , m = 5 
Output: Minimum Difference is 6 


Input : arr[] = {12, 4, 7, 9, 2, 23, 25, 41, 30, 40, 28, 42, 30, 44, 48, 43, 50} , m = 7 
Output: Minimum Difference is 10 

'''

def chocolate_intervals(a,m):
    a.sort()
    min_val = a[-1]
    for i in range(len(a)-m+1):
        elements = a[i:i+m]
        max_ele = max(elements)
        min_ele = min(elements)

        if(min_val > max_ele - min_ele):
            min_val = 0
            min_val = max_ele - min_ele
    return min_val

a = [7, 3, 2, 4, 9, 12, 56]
m = 3
print(chocolate_intervals(a,m))

a = [3, 4, 1, 9, 56, 7, 9, 12]
m = 5
print(chocolate_intervals(a,m))

a = [12, 4, 7, 9, 2, 23, 25, 41, 30, 40, 28, 42, 30, 44, 48, 43, 50]
m = 7
print(chocolate_intervals(a,m))