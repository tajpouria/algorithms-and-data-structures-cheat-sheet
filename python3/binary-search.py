from random import randint

arr = [randint(1, 100) for i in range(100)]
sarr = sorted(arr)

rand_idx = randint(1, 100)
tar = sarr[rand_idx]

print(f"Question What is that index of the {tar}? Answer: {rand_idx}")

def binary_search(ar, tar):
    def _binary_search(ar, t, x, y):
        if x >= y: return -1
        mi = (x + y)//2
        mid = ar[mi]
        if mid == t: return mi
        if t > mid :
            return _binary_search(ar, t, mi+1, y)
        return _binary_search(ar, t, x, mi-1)
    
    return _binary_search(ar, tar, 0, len(ar))

# print(binary_search(sarr, tar))
print(binary_search(sarr, -1))


