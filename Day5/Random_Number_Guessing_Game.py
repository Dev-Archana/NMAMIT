import random
secrate_number=random.randint(1,10)
while True:
    entered_number=int(input("Enter Your Number: "))
    if(secrate_number-entered_number==0):
        print("Congratulations!...")
        break
    elif(secrate_number-entered_number>=2):
        print('HOT')
        print('\U0001F525')
    elif(secrate_number-entered_number<=2):
        print('COLD')