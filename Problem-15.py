'''
Problem 15 : To Find longest word in given dictionary 

example :-
Input : words = ['w','wo','wor','worl','world']
Output : world
'''

def toFindLongest(words):
    words.sort()
    result = ''
    builtWords = set()
    for word in words:
        if ((len(word)==1) or (word[0:len(word)-1] in builtWords)):
            if(len(word) > len(result)):
                result = word
            builtWords.add(word)
    return result
print('Input : [w,wo,wor,worl,world]','\nOutput : ',toFindLongest(['w','wo','wor','worl','world']))
print('_'*35)
print('Input : [a,apple,banana,app,appl,ap,apply]','\nOutput : ',toFindLongest(['a','apple','banana','app','appl','ap','apply']))
print('_'*35)