'''
Problem 7 : Sorted square array
'''
"Algorithm-1 using sort method O(nlogn)"

nums  = [-6,-5,-4,1,3,5]
n = len(nums)
output_arr = []

def sort_square_arr(nums,n):
    for i in nums:
        output_arr.append(i*i)
    
    output_arr.sort()
    return output_arr

print('Input : ', nums,"\nOutput: ",sort_square_arr(nums,n))

"Algorithm-2 using two pointers O(n)"

def sort_square_arr_optimal(nums,n):
    left = 0
    right = n-1
    output = [0]*n
    for i in range(n-1,-1,-1):
        if abs(nums[left]) > nums[right]:
            output[i] = nums[left]*nums[left]
            left = left+1
        else:
            output[i] = nums[right]*nums[right]
            right = right-1
    return output
print('-'*30)
print('Input : ', nums,"\nOutput: ",sort_square_arr_optimal(nums,n))
