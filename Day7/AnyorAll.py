N=int(input())
l1=input().split()
print(all(int(i)>0 for i in l1)and any(i==i[::-1] for i in l1))