class BankAccount:
    def __init__(self,name,acc_no,balance):
        self.name = name
        self.acc_no = acc_no
        self.balance = balance
    def deposit(amount):
        if amount<5000:
            print("deposit not succesful! please add!") 
        else:
            print("deposit succesfull!") 
            self.balance = self.balance + amount #type: ignore
            print("new balance",self.balance) #type: ignore



    def withdraw(amount):
        if amount>self.balance: #type: ignore
            print("salio lako halitoshi.tafuta hela! Acha tamaa")
        else:
            self.balance = self.balance - amount #type: ignore
            print("hongera,umefanikiwa kutoa kiasi",amount,"salio lako jipya ni,",self.balance) #type: ignore



account1 = BankAccount("luqman",1,100000) 
account2 = BankAccount("mamu",2,500000)
account3 = BankAccount("shaloom",3,300000)
print(account1.name)
print(account2.name)
print(account3.name)
print(account1.balance)
print("account ya",account1.name,"ina salio la TZS",account1.balance)