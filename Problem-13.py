#Task Scheduler

def task_scheduler(tasks,n):
    char_counts = [0]*26
    for c in tasks:
        char_counts[ord(c)-ord('A')] = char_counts[ord(c)-ord('A')] + 1
    char_counts.sort()
    
    max_val = char_counts[25] - 1 # last one doesn't included it will run automatically ex.A->B
    idle_slots = max_val * n
    print(idle_slots)

    for i in range(24,-1,-1):
        idle_slots -= min(char_counts[i],max_val)
    print(idle_slots)
    if idle_slots > 0:
        return idle_slots + len(tasks)
    else:
        return len(tasks) 


print('Input : ["A","A","A","B","B","B"] , n=2','\nOutput : ',task_scheduler(["A","A","A","B","B","B"],2))