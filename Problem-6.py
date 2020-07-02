'''
Problem 6 : To find if the any elements of each array if added together gives required vale or not.
Function  : SumOfTwo(a,b,v)

'''

'Algorithm-1 using Brute Force'

def SumOfTwo_1(a,b,v):
    for i in a:
        difference = v - i
        for j in b:
            if(j== difference):
                return True
    return False

a = [1,2,2]
b = [10,20,30,40]
v = 42

a_1 = [1,2,3,4]
b_1 = [11,12,3,4]
v_1 = 42

print('Array_1 : ',a," Array_2 : ",b," Value : ",v,"\nOutput : ",SumOfTwo_1(a,b,v))

print('Array_1 : ',a_1," Array_2 : ",b_1," Value : ",v_1,"\nOutput : ",SumOfTwo_1(a_1,b_1,v_1))


'Algorithm-2 using datastructure(set) O(n)'

def SumOfTwo_2(a,b,v):
    differences = set()
    for i in a :
        difference = v - i
        differences.add(difference)
    for j in b:
        if j in differences:
            return True
    return False

print('Array_1 : ',a," Array_2 : ",b," Value : ",v,"\nOutput : ",SumOfTwo_2(a,b,v))

print('Array_1 : ',a_1," Array_2 : ",b_1," Value : ",v_1,"\nOutput : ",SumOfTwo_2(a_1,b_1,v_1))