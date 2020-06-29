'Problem -2 First Non Repeating character'



s =  'aaabcccdeef'


n =  len(s)

'Solution-1'

def fnrc(s,n):
    for i in range(0,n):
        seenDuplicate = False
        for j in range(0,n):
            if(s[i] == s[j] and (i!=j)):
                seenDuplicate = True
                break;
        if(not seenDuplicate):
            return s[i]
    return '-'

sol = fnrc(s,n)
print(sol)


'Solution-2 using hashmap'

def fnrc2(s,n):
    c_counts = dict() 
    for i in range(0,n):
        c = s[i]
        if(c in c_counts):
            c_counts.put(c,c_counts.get(c)+1)
        else:
            c_counts.put(c,1)

    'For lookup'

    for i in range(0,n):
        c = s[i]
        if(c_counts.get(c) == 1):
            return (c)
    return '-'

sol_2 = fnrc(s,n)
print(sol_2)
        