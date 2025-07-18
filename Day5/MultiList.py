name = ["Suraj ", "Aman", "Raju", "Sam"]
maths =[30, 30, 90, 80]
science=[10, 12, 78, 70]
x = input("ENTER AN STUDEBT NAME : ")

for i in range(0,len(name) ):
    y = name[i]
    if y.lower() == x.lower():
        print(x.upper(), " :" , (maths[i]+science[i])/2, "%")