'Product of array except itself'

'Solution-1 using division'

nums = [1,2,3,4]
n = len(nums)
product = 1
output = [1]*5

for i in range(0,n):
	product=product*nums[i]
for i in range(0,n):
	output[i] = product // nums[i]

print(output)

