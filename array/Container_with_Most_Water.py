# Input: array = [1, 5, 4, 3]
# Output: 6
# Explanation : 
# 5 and 3 are distance 2 apart. 
# So the size of the base = 2. 
# Height of container = min(5, 3) = 3. 
# So total area = 3 * 2 = 6

# Input: array = [3, 1, 2, 4, 5]
# Output: 12
# Explanation : 
# 5 and 3 are distance 4 apart. 
# So the size of the base = 4. 
# Height of container = min(5, 3) = 3. 
# So total area = 4 * 3 = 12

def water_container(A , Len):
    area = 0
    for i in range(Len) :
        for j in range(i + 1, Len) :
            area = max(area, min(A[j], A[i]) * (j - i))
    return area

a = [1, 5, 4, 3]
print(water_container(a,len(a)))

a = [3, 1, 2, 4, 5]
print(water_container(a,len(a)))

