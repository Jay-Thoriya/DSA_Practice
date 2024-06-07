# Input  : arr[] = {5, 6, 7, 8, 9, 10, 1, 2, 3}, key = 3
# Output : Found at index 8


# Input  : arr[] = {5, 6, 7, 8, 9, 10, 1, 2, 3}, key = 30
# Output : Not found

# Input : arr[] = {30, 40, 50, 10, 20}, key = 10   
# Output : Found at index 3

#there are two ways to do this

#first way using methods 

def search_element(arr, key):
    try :
        return arr[key] 
    except :
        return 'NOT Founded'

#second way without using methods

def search_element_by_key(arr, key):
    for i in range(len(arr)):
        if i == key:
            return arr[key]
    return 'NOT Founded'


arr = [5, 6, 7, 8, 9, 10, 1, 2, 3]
key = 3

print(search_element(arr, key))
print(search_element_by_key(arr, key))

arr = [5, 6, 7, 8, 9, 10, 1, 2, 3]
key = 10
print(search_element(arr, key))
print(search_element_by_key(arr, key))