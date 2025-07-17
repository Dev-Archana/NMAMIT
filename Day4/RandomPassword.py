
import random 

names=['abcd','efgh','ijkl','mnop','qrst']
random_name=random.choice(names)
random_number=random.randint(1000, 9999)
print (f'generated password is : {random_name}{random_number}')