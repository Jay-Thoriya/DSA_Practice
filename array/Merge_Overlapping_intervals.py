'''
Input: Intervals = {{1,3},{2,4},{6,8},{9,10}}
Output: {{1, 4}, {6, 8}, {9, 10}}
Explanation: Given intervals: [1,3],[2,4],[6,8],[9,10], we have only two overlapping intervals here,[1,3] and [2,4]. Therefore we will merge these two and return [1,4],[6,8], [9,10].

Input: Intervals = {{6,8},{1,9},{2,4},{4,7}}
Output: {{1, 9}}

'''

def Merge_overlapping_intervals(a):
    a.sort(key=lambda x: x[0])
    res = []
    for i in range(len(a)):
        if not res or res[-1][1] <= a[i][0]:
            res.append(a[i])
        else:
            res[-1][1] = max(res[-1][1], a[i][1])
    return res 

a = [[1,3],[2,4],[6,8],[9,10]]
print(Merge_overlapping_intervals(a))

a = [[6,8],[1,9],[2,4],[4,7]]
print(Merge_overlapping_intervals(a))
