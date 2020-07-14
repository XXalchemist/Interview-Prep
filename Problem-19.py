'''
Power of 2
Example :-
Input : 2       Input : 1
Output : True   Output : False
'''

# Algorithm 1 O(logn)

def isPower2(num):
    if num == 2: 
        return True
    else:
        while(num % 2 == 0):
            num /= 2
    return (num==1)

print('_'*35)
print('\nInput : 2',' Output : ',isPower2(2))
print('_'*35)
print('\nInput : 41',' Output : ',isPower2(41))
print('_'*35)

# Algorithm 2 using Bit manipulation -> O(1)

def isPowerOf2(num):
    if num == 0:
        return True
    else:
        return num & -num == num


print('\nInput : 4',' Output : ',isPower2(4))
print('_'*35)
print('\nInput : 100',' Output : ',isPower2(100))
print('_'*35)
