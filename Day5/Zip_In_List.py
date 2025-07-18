l1=['books','pen','phone']
l2=[3,5,7]
combined=list(zip(l1,l2))
print(combined)
for i,j in zip(l1,l2):
    print(i,j)

m1,m2=zip(*combined)
m3=list(m1)
print(type(m1))
print(type(m3))
print(m2)
