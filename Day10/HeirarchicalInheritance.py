# Bank -> super class (methods: deposit,withdraw)
# Savings -> sub class 1(method :display minimum balance  )
# Current -> subclass 2(method: roi ->0.05)
class Bank:
    bal=0
    accountNumber=""
    accHolderName=""
    IFSC=""
    def __init__(self,accountNumber,accHolderName,IFSC):
        self.accountNumber=accountNumber
        self.accHolderName=accHolderName
        self.IFSC=IFSC
    def display(self):
        print(self.accountNumber)
        print(self.accHolderName)
        print(self.IFSC)
    def deposit(self):
        print("Enter Your Depositing Amount :💰")
        amt=float(input())
        if(amt>0):
            self.bal=self.bal+amt 
            print("Deposit Succesful")
            print("Available Balance:",self.bal)
        else:
            print("Invalid Amount")
    def withdraw(self):
        amt=float(input())
        bal=self.bal-amt
class Savings(Bank):
    min_bal=500
    def __init__(self):
        super().__init__(123456789,"abc","123ifsc")
    def displayMinimumBalance(self):
        print(self.min_bal)
class Current(Bank):
    roi=0.05
    def calculateROI(self):
        cal=(self.roi*self.bal)+self.bal 
        print(cal)
s=Savings()
s.deposit()


    
    