s='121$ mom, 121l' 
s2=''.join(a.lower() for a in s if a.isalpha())
print(s2)
s1=s2[::-1]
if(s==s1):
    print('palindrome')
else:
    print('not palindrome')