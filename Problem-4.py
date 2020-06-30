'''
To check if the given inputs are anagram or not.

Anagram : Re-arrangement of characters
'''
input_1 = 'CAT'
input_2 = 'ACT'
input_3 = 'CAAT'
input_4 = 'CAD'

def is_anagram(i_1, i_2):
    is_valid_anagram = False
    c_counts = [0]*256
    if(len(i_1) == len(i_2)):
        for i in range(0,len(i_1)):
            c_counts[ord(i_1[i])] = c_counts[ord(i_1[i])]+1
            c_counts[ord(i_2[i])] = c_counts[ord(i_2[i])]-1
        
        is_valid_anagram = True

        for count in c_counts:
            if count != 0:
                is_valid_anagram = False
                break

    
    return(is_valid_anagram)

print('CAT and ACT\n-->',is_anagram(input_1,input_2))


print('\nCAT and CAAT\n-->',is_anagram(input_1,input_3))


print('\nCAT and CAD\n-->',is_anagram(input_1,input_4))



