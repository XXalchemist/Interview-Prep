'''
Find number of trailing zeroes.
'''

def trailingZeroes(input1):
    count = 0
    i = 5
    while(input1/i >= 1):
        count+=input1/i
        i*=5
    return(int(count))

print('\nInput :  100',' Output : ',trailingZeroes(100))