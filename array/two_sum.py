# Input: arr[] = {0, -1, 2, -3, 1}, x= -2
# Output: Yes
# Explanation: If we calculate the sum of the output,1 + (-3) = -2

# Input: arr[] = {1, -2, 1, 0, 5}, x = 0
# Output: No

def chkPair(a, x):
    for i in range(0,len(a)):
        for j in range(i,len(a)):
            if(a[i]+a[j] == x and i!=j):
                return 1
                break

a1 = [0, -1, 2, -3, 1]
x1 = -2
a2 = [1, -2, 1, 0, 5]
x2 = 0
if chkPair(a2,x2) == 1: 
    print("yes")
else:
    print("no")


