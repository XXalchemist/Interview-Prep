'''
To find the maximum number of repeated character in string.

example : 'abccddec' -> c
'''


def toFindMaxChar(input1):
    
    c_counts = [0]*256  # Number of ascii characters
    checkflag = True
    max_v = -1 # Initialize the max value for comparison
    res = ''
    
    # Loop to assign the frequency of character

    for character in input1:
        c_counts[ord(character)]+=1

    for character in input1:

        if max_v < c_counts[ord(character)]:
            max_v = c_counts[ord(character)]
            res = character

    for count in c_counts:
        if count == max_v:
            checkflag = not checkflag
    
    if checkflag == False:
        return res
    else:
        return -1


print('\nInput : aabccdebb','Output : ',toFindMaxChar('aabccdebb'))

print('\nInput : aabccde','Output : ',toFindMaxChar('aabccde'))

print('\nInput : aaccdede','Output : ',toFindMaxChar('aabccde'))