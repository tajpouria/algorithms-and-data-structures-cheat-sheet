
def binary_search(arr, t):
    low, up = 0, len(arr)
    while low < up:
        mid = (low + up) // 2
        if arr[mid] == t:
            return mid
        elif arr[mid] > t:
            up = mid
        else:
            low = mid + 1

    return -1


def lowerbound(arr, t):
    low, up = 0, len(arr)
    while low < up:
        mid = (low + up) // 2
        if arr[mid] >= t:
           up = mid 
        else:
            low = mid + 1

    return low
    
        
def upperbound(arr, t):
    low, up = 0, len(arr)
    while low < up:
        mid = (low + up) // 2
        if arr[mid] > t:
            up = mid
        else:
            low = mid + 1

    return low


def bound_search(arr, t, compare):
    low, up = 0, len(arr)
    while low < up:
        mid = (low + up) // 2
        if compare(arr[mid], t):
            up = mid
        else:
            low = mid + 1
            
    return low

lower = lambda el, t: el >= t
upper = lambda el, t: el > t


arr = [1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 4]

print(binary_search(arr, 2)) # 5
print(lowerbound(arr, 2)) # 4
print(upperbound(arr, 2)) # 7 One index after the last element
print(bound_search(arr, 2, lower)) # 4
print(bound_search(arr, 2, upper)) # 7

