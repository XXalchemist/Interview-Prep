'''
Problem 12 : To find all the duplicates in the given array without using extraspace and in linear time i.e(O(n))
Important : length of input arr (1,length of arr)
'''

def toFindAllDup(arr):
    for i in range(0,len(arr)):
        index = abs(arr[i])-1
        if (arr[index]>0):
            arr[index] = -arr[index]
    print('After applying algorithm : ',arr)
    
    output_arr = []
    for i in range(0,len(arr)):
        if(arr[i] > 0 ):
            output_arr.append(arr[i])
    return(output_arr)    


print('Algo-1\nInput : [2,1,3,4,3,2]','\nOutput : ',toFindAllDup([2,1,3,4,3,2]))
print('*'*30)
print('Input : [2,1,3,4]','\nOutput : ',toFindAllDup([2,1,3,4]))
print('*'*30)
print('Input : [1,1,1,3,3]','\nOutput : ',toFindAllDup([1,1,1,3,3]))
print('*'*30)

def toFindAllDup_2(arr):
    output_arr = []
    for i in range(0,len(arr)):
        index = abs(arr[i])-1
        if (arr[index]<0):
            output_arr.append(index+1)
        arr[index] = -arr[index]
    return output_arr

print('Algo-2\nInput : [2,1,3,4,3,2]','\nOutput : ',toFindAllDup_2([2,1,3,4,3,2]))
print('*'*30)
print('Input : [2,1,3,4]','\nOutput : ',toFindAllDup_2([2,1,3,4]))
print('*'*30)
print('Input : [3,1,1,3,1]','\nOutput : ',toFindAllDup_2([1,1,1,3,3]))