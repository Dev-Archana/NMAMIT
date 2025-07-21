# Creating a dictionary
d = {
    'name': 'abc',
    'age': 26,
    'city': 'Bangalore'
}

print("Original Dictionary:")
print(d)

# ---------------------------------------------
# keys(), values(), items()
print("\nKeys:", d.keys())        # dict_keys(['name', 'age', 'city'])
print("Values:", d.values())      # dict_values(['abc', 26, 'Bangalore'])
print("Items:", d.items())        # dict_items([('name', 'abc'), ('age', 26), ('city', 'Bangalore')])

# ---------------------------------------------
# get() - safely get value
print("\nGet 'name':", d.get('name'))          # abc
print("Get 'gender' (not present):", d.get('gender'))  # None

# ---------------------------------------------
# update() - update or add new keys
d.update({'email': 'abc@example.com'})
print("\nAfter update():", d)

# ---------------------------------------------
# pop() - removes specified key
removed = d.pop('age')
print("\nAfter pop('age'):", d)
print("Removed value:", removed)

# ---------------------------------------------
# popitem() - removes the last inserted item
last = d.popitem()
print("\nAfter popitem():", d)
print("Popped item:", last)

# ---------------------------------------------
# setdefault() - returns value if key exists, else inserts with default
value = d.setdefault('country', 'India')
print("\nAfter setdefault():", d)
print("Returned value:", value)

# ---------------------------------------------
# clear() - removes all items
temp_dict = {'a': 1, 'b': 2}
temp_dict.clear()
print("\nAfter clear():", temp_dict)

# ---------------------------------------------
# copy() - shallow copy of dict
copied_dict = d.copy()
print("\nCopied Dictionary:", copied_dict)

# ---------------------------------------------
# fromkeys() - create new dict from list of keys
keys = ['x', 'y', 'z']
new_dict = dict.fromkeys(keys, 0)
print("\nNew Dict from keys:", new_dict)

# ---------------------------------------------
# Looping over dictionary
print("\nIterating over dictionary:")
for key, value in d.items():
    print(f"{key} → {value}")

# ---------------------------------------------
# Using zip() to iterate over keys and values (not preferred over items())
print("\nUsing zip on keys and values:")
for k, v in zip(d.keys(), d.values()):
    print(f"{k}: {v}")

# ---------------------------------------------
# Creating dictionary from list of tuples
list_of_tuples = [('brand', 'Nike'), ('price', 2500)]
dict_from_list = dict(list_of_tuples)
print("\nDict from list of tuples:", dict_from_list)

