'''
Convert Roman Number to Integer Number
eg. 
Input : XI Output : 11
Input : IX Output : 9
'''

# Algorithm 1 O(n)

def romanToInt(num):
    dictionary = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    prev = 0
    curr = 0
    total = 0
    for i in range(len(num)):
        curr = dictionary[num[i]]
        if curr > prev:
            total += total + curr - 2*prev
        else:
            total += curr
        prev = curr
    return total

print('_'*13,'Testing','_'*13)
print('\nInput : XI ','\nOutput : ',romanToInt('XI'))
print('_'*35)
print('\nInput : IX \nOutput : {}'.format(romanToInt('IX')))
print('_'*35)
