# Input: interval arr[] = { {1, 3}, {2, 4}, {3, 5}, {7, 9} } 
# Output: 
# [5, 7] 
# Explanation: 
# The only interval which doesn’t overlaps with the other intervals is [5, 7].
# Input: interval arr[] = { {1, 3}, {9, 12}, {2, 4}, {6, 8} } 
# Output: 
# [4, 6] 
# [8, 9] 
# Explanation: 
# There are two intervals which don’t overlap with other intervals are [4, 6], [8, 9].


def non_overlapping_intervals(a):
    a.sort(key=lambda x: x[0])
    res = []
    for i in range(len(a)):
        if not res or res[-1][1] <= a[i][0]:
            res.remove(a[i])
        else:
            res[-1][1] = max(res[-1][1], a[i][1])
    return res 

a = [ [ 1, 3 ], [ 2, 4 ],[ 3, 5 ], [ 7, 9 ] ]
print(non_overlapping_intervals(a))