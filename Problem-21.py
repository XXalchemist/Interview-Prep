'''
Number Series Question

W.A.P to find the nth number in the given series :-

1, 1, 2, 3, 4, 9, 8, 28, .....

Solution :- Through observation we find number at even position have geometric series (a*2)
            and number at odd position have geometric series (b*3). We use this to write the 
            program.
'''

# Algorithm  1 using for loop O(n)

def toFindNth(n): 
    for i in range(1,n+1):
        if(i%2 != 0):
            if i == 1:
                a = 1
            else:
                a = a*2
        else:
            if i == 2:
                b = 1
            else:
                b = b*3
    
    if(n%2 == 0):
        print('Number at {} position in the given series is {}'.format(n,b))
    else:
        print('Number at {} position in the given series is {}'.format(n,a))
    return False

print("_"*70)
print('Given Series : 1, 1, 2, 3, 4, 9, 8, 28, ..... ')
n = int(input('Enter the position of which in the series you want the value : '))

toFindNth(n)
print("_"*70)