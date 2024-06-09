'''
input: Set : [1, 3], [6, 9]
New Interval : [2, 5]
Output: [1, 5], [6, 9]
Explanation: The correct position to insert a new interval [2, 5] is between the two given intervals.
The resulting set would have been [1, 3], [2, 5], [6, 9], but the intervals [1, 3], [2, 5] are overlapping. So, they are merged in one interval [1, 5].


Input: Set : [1, 2], [3, 5], [6, 7], [8, 10], [12, 16]
New Interval : [4, 9]
Output: [1, 2], [3, 10 ], [12, 16]
Explanation: First the interval is inserted between intervals [3, 5] and [6, 7]. Then overlapping intervals are merged together in one interval

'''

def non_overlapping_intervals(a,n):
    a.append(n)
    a.sort(key=lambda x: x[0])
    res = []
    for i in range(len(a)):
        if not res or res[-1][1] <= a[i][0]:
            res.append(a[i])
        else:
            res[-1][1] = max(res[-1][1], a[i][1])
    return res 


a = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
n = [4, 9]
print(non_overlapping_intervals(a,n))

a = [[1, 3],[6,9]]
n = [2, 5]
print(non_overlapping_intervals(a,n))