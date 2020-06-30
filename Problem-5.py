'''
Valid Paranthesis

example - 
() -> True
([]) -> True
([)] -> False
([{}]) -> True
[ -> False

'''

input_1 = '()'
input_2 = '([{}])'
input_3 = '('

def is_valid(inp):
    is_empty = False
    stack = []
    if len(inp)%2 == 0:
        for i in range(0,len(inp)):
            if(inp[i] == '(' or inp[i] == '[' or inp[i] == '{'):
                stack.append(inp[i])

            elif(inp[i] == ')' and not empty(stack) and stack[len(stack)-1] == '('):
                stack.pop()

            elif(inp[i] == ']' and not empty(stack) and stack[len(stack)-1] == '{'):
                stack.pop()
            
            elif(inp[i] == '}' and not empty(stack) and stack[len(stack)-1] == '{'):
                stack.pop()
    
        if(empty(stack)):
            is_empty = empty(stack)
    
    return(is_empty) 

def empty(stack):
    if stack == []:
        return True
    else:
        return False       

print(input_1,' -> ',is_valid(input_1)) 
print(input_2,' -> ',is_valid(input_2)) 
print(input_3,' -> ',is_valid(input_3))        