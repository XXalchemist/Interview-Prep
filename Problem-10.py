'Longest Palindromic Substring from the given string s'

def expandFromMiddle(s,left,right):
    if(s == None or left > right):
        return 0
    while(left >=0 and right < len(s) and s[left]==s[right]):
        left = left-1
        right = right+1
    return right-left-1

def longestPalindrome(s):
    if(s == None or len(s) < 1):
        return ""
    start = 0
    end = 0

    for i in range(0,len(s)):
        len1 = expandFromMiddle(s,i,i)
        len2 = expandFromMiddle(s,i,i+1)
        leng = max(len1, len2)
        if(leng > end-start):
            start = i-((leng-1)//2)
            end = i+(leng//2)
    return(s[start:(end+1)])


print('baabad\nOutput : ',longestPalindrome('baabad'))