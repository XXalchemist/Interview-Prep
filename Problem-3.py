'Problem-3 To find maximum sub array'

'''
Kadanne's Algorithm
'''
nums = [-2,2,5,-11,6]

max_sum = nums[0]
curr_sum = max_sum

for i in range(1,len(nums)):
    curr_sum = max(nums[i]+curr_sum, nums[i])
    max_sum = max(curr_sum, max_sum)
print(max_sum)
