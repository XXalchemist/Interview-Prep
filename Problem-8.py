'''
Problem-8 : First Duplicate in the given array.
'''

"Algorithm-1 using brute force O(n2)"

i_1 = [1,2,3,2,3,4]
i_2 = [1,2,3,4]
i_3 = [1,2,3,4,3,4]
i_4 = [1,2,3,3]

def findDuplicate_1(inp):
    min_index = len(inp)-1
    for i in range(0,len(inp)):
        for j in range(i+1,len(inp)):
            if (inp[i]==inp[j]):
                min_index = min(min_index, j)
    if min_index == len(inp)-1: return (-1)
    else: return inp[min_index]

print('Input : ',i_1,"\nOutput : ",findDuplicate_1(i_1))
print('Input : ',i_2,"\nOutput : ",findDuplicate_1(i_2))
print('Input : ',i_3,"\nOutput : ",findDuplicate_1(i_3))

"Algorithm-2 using extraspace set O(n)"

def findDuplicate_2(inp):
    lookup = set()
    a = 0
    for i in inp:
        if i not in lookup:
            lookup.add(i)
            a = a+1
            if(a==len(inp)):
                return -1
        else:
            return i

print('-'*30)
print('Input : ',i_1,"\nOutput : ",findDuplicate_2(i_1))
print('Input : ',i_2,"\nOutput : ",findDuplicate_2(i_2))
print('Input : ',i_3,"\nOutput : ",findDuplicate_2(i_3))
print('Input : ',i_4,"\nOutput : ",findDuplicate_2(i_4))

'Algorithm-3 without set O(n)'

def findDuplicateOptimal(a):
    for i in range(0,len(a)):
        if(a[ abs(a[i]) -1 ] < 0):
            return abs(a[i])
        else:
            a[ abs(a[i]) -1 ] = -a[ abs(a[i]) -1 ] 
    return -1



print('-'*30)
print('Algo rep : ',i_1,"\nOutput : ",findDuplicateOptimal(i_1))
print('Algo rep : ',i_2,"\nOutput : ",findDuplicateOptimal(i_2))
print('Algo rep : ',i_3,"\nOutput : ",findDuplicateOptimal(i_3))
print('Algo rep : ',i_4,"\nOutput : ",findDuplicateOptimal(i_4))