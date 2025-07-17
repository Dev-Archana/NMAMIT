def anagram(s):

    if len(s) % 2 != 0:
        return -1

    
    mid = len(s) // 2
    s1 = s[:mid]
    s2 = s[mid:]

 
    from collections import Counter
    count1 = Counter(s1)
    count2 = Counter(s2)

   
    changes = 0
    for char in count1:
        if count1[char] > count2.get(char, 0):
            changes += count1[char] - count2.get(char, 0)

    return changes
t = int(input()) 
for _ in range(t):
    s = input().strip()
    print(anagram(s))
