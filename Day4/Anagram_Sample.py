# Sample Anagram Problem 
s1='abc '
s2='cba'
s1=''.join(i.lower() for i in s1 if i.isalpha())
s2=''.join(i.lower() for i in s2 if i.isalpha())
if(sorted(s1)==sorted(s2)):
    print("Anagram")
else:
    print("Not Anagram")