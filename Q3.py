#Given an array nums of n integers where nums[i] is in the range [1, n],
#return an array of all the integers in the range [1, n] that do not appear in nums
n = 5
nums = [1, 2, 4, 5]

ans = []

for i in range(1, n + 1):
    if i not in nums:
        ans.append(i)

print(ans)