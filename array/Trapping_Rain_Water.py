"""
Input: arr[] = {2, 0, 2}
Output: 2

Input: arr[]   = {3, 0, 2, 0, 4}
Output: 7

Input: arr[] = {0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1}
Output: 6

"""

a = [2,0,2] #2
b = [3,0,2,0,4] #7
c = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1] #6
def rain_water(a):
    water = 0
    for i in range(1,len(a)-1):
        left_max = max(a[0:i+1])
        right_max = max(a[i+1:]) 
        if left_max < right_max:
            print(f"left_max = {left_max} , right_max = {right_max}")
            water += abs(left_max - a[i])
            print("water", water)
        elif left_max > right_max:
            if left_max == a[i]:
                water += abs(left_max - a[i])
            print(f"left_max = {left_max} , right_max = {right_max}")
            water += abs(right_max - a[i])
            print("water", water) 

        

    return water

print(rain_water(a))
print(rain_water(b))
print(rain_water(c))
