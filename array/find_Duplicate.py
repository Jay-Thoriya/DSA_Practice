# Input: n=7 , array[]={1, 2, 3, 6, 3, 6, 1}
# Output: 1, 3, 6
# Explanation: The numbers 1 , 3 and 6 appears more than once in the array.


# Input : n = 5 and array[] = {1, 2, 3, 4 ,3}
# Output: 3
# Explanation: The number 3 appears more than once in the array.

def find_Duplicate(a,n):
    Duplicate = [] 
    for i in range(n):
        for j in range(i+1,n):
            if a[i] == a[j]:
                if(a[i] not in Duplicate):
                    Duplicate.append(a[i])
    return Duplicate

a = [1, 2, 3, 6, 3, 6, 1]
n = 7
a1 = [1, 2, 3, 4 ,3]
n1 = 5
print(find_Duplicate(a1,n1))            
