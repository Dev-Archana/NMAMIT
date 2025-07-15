a=[2,3,4,'a','hello',5.6,True]
print(a)
print(type(a))
l=len(a)
a[0]=20
for i in range(l):
    print(a[i])
