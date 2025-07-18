List1=['Q','W','H','J','K']
target='Q'
# Way-1
def find_element(List1,target):
    for i in range(len(List1)-1):
        if target==List1[i]:
            return i
    return -1
    
# Way-2
    if target in List1:
        return List1.index(target)
    else:
        return -1
print(find_element(List1,target))







    