'''
Convert the given input string into lower case
'''
def toLowerCase(string):
    result = ''
    for i in string:
        result = result + chr(ord(i)+32)
    return result

print('Input: ACD',toLowerCase('ACD'))