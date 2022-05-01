nums, k = [1, 3, -1, -3, 5, 3, 6, 7, 7], 3

res = []

for i in range(len(nums) - k):
    res.append(max(nums[i:i+k]))

print(res)

