s1={1,2,3,4,4,2,1,5}
# s2={1,2,3}
# s3=s1^s2
# print(s3)
result=0
for nums in s1:
    result=result^nums
print(result)