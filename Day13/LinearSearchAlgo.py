def linear_search(lst, target):
    for index, value in enumerate(lst):
        if value == target:
            return index  
    return -1  

numbers = [10, 20, 30, 40, 50]
target = 30

result = linear_search(numbers, target)

if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found")
