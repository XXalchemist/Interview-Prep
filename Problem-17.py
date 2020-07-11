'''
Valid Perfect Square 

Example :
Input : 14        Input : 16
Output : False    Output : True
'''

#Algorithm-1 O(logn) using Binary Search

def isValidPerSquare(num):
    
    if num == 1:
        return True 
    left = 2
    right = num//2  # as 16//2 = 8 which is still < 4 

    while(left <= right):
        mid = (left + right)//2
        if mid ** 2 == num:
            return True
        elif mid ** 2 > num:
            right = mid - 1
        else: 
            left = mid + 1
    return False

print('Input : 16','\nOutput : ',isValidPerSquare(16))
print('-'*35)
print('Input : 18','\nOutput : ',isValidPerSquare(18))
print('-'*35)

# Newton's Method to calculate closest perfect square
def isValidPerSquareNewtonsmethod(num):
    result = num
        # stop while until < or ==
    while result * result > num:
        result = (result + num // result) // 2

    return result * result == num
print('Input : 25','\nOutput : ',isValidPerSquareNewtonsmethod(25))
print('-'*35)
print('Input : 50','\nOutput : ',isValidPerSquareNewtonsmethod(50))
print('-'*35)


