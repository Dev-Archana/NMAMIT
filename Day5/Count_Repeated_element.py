
# 7,49,7,11,6,41,7,1,101-> count the repetation
# target-7

nums =[7,49,7,11,6,41,7,1,101]

target=int(input("Enter the number"))
count=0
if target in nums:
    count=nums.count(target)
    
    
print(count)
    
