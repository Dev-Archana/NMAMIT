# 



s='ABCDCDC'
#  output=['CDC','CDC']
s1='CDC'
count = 0
for i in range(len(s) - len(s1) + 1):
    if s[i:i+len(s1)] == s1:  
        count += 1
print(count)

# Display repeated substring count in a stringDisplay repeated substring count in a string
# Example: s='ABCDCDC', s1='CDC' should return 2