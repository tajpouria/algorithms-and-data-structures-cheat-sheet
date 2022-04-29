from random import randint

li =  [randint(0, 100) for i in range(0, 100)]
li = sorted(li)

tari = randint(0, len(li))
tar = li[tari]

print(f"Q: What is the index of {tar}?")

def binary_search(arr, t):
	l, r = 0, len(arr) - 1

	while l < r:
		mi = (r + l) // 2
		mid = arr[mi]
		if mid == t: return mi
		if t > mid: l = mi + 1 
		else: r = mi + -1

	return -1	

print(binary_search(li, tar))

print(f"Correct answer: {tari}")

