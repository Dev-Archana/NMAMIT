# tuple creation Method
t1=(1,)
t2=1,2,3,2
t3=()
# Check Type
print(type(t1))
print(type(t2))
# tuple Methods 
print(len(t2))
print(min(t2))
print(max(t2))
print(t2.count(2))
print(t2.index(2))
# Conversion
l1=list(t2)
print(type(l1))

# Membership Operation(Print With for: )
for i in t2:
    print(i)









