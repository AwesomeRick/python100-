nums = [0,6,0,6,8,7,4,2,0,2]
length = len(nums)
for i in range(length):
    if nums[i] == 0:
        del nums[i]
        nums.append(0)
print(nums)