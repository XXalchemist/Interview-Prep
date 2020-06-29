'Product of array except itself'

'Solution-1 using division'

nums = [1,2,3,4]
n = len(nums)
product = 1
output = [1]*n

for i in range(0,n):
	product=product*nums[i]
for i in range(0,n):
	output[i] = product // nums[i]

print(output)

'''
Solution-2 using extra-space
In this approach we take left and right products of every elements of array and then multiply both array together.

'''

left_products = [1]*5
right_products = [1]*5
output_2 = [1]*n

for i in range(1,n):
	left_products[i] = nums[i-1]*left_products[i-1]
for i in range(n-2,-1,-1):
	right_products[i] = nums[i+1]*right_products[i+1]

for i in range(0,n):
	output_2[i] = left_products[i]*right_products[i]

print(output_2)


'''
Solution-3
Removing extraspace
'''

output_3 = [1]*n
for i in range(1,n):
	output_3[i] = nums[i-1]*output_3[i-1]
r = 1
for i in range(n-1,-1,-1):
	output_3[i] = output_3[i]*r
	r= r*nums[i] 

print(output_3)