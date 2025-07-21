# converting tuple to list and operating list operations 
# Tuple to list conversion
tup1 = (1, 4, 6, 9)       # Use parentheses for clarity (optional but recommended)
l1 = list(tup1)           # Convert tuple to list

# List modifications
l1.append(10)             # Add 10 to the list
l1.append(2)              # Add 2 to the list
l1.remove(2)              # Remove the first occurrence of 2

# Convert back to tuple
l2 = tuple(l1)            # Convert list back to tuple

# Output
print(type(l2))           # Should print: <class 'tuple'>
print(l2)                 # Should print: (1, 4, 6, 9, 10)
