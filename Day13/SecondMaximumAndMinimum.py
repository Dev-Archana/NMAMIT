# # Write a program to find second maximum and second minimum in a given list 
lst = [0, 1, 3, 4, 1, 11, 7, 6, 9]

# for i in range(len(lst)):
#     m=lst[i]
#     for j in range(i,len(lst)):
#         if lst[j] < m:
#             lst[i]=lst[j]
#             lst[j]=m
            
# print("SECOND MINIMUM NUMBER : ", lst[1], "SECOND LARGEST NUMBER : ",lst[len(lst)-2])




set_list=set(lst)
set_list=list(set_list)
print("SECOND MINIMUM NUMBER : ", set_list[1], "SECOND LARGEST NUMBER : ",set_list[-2])
