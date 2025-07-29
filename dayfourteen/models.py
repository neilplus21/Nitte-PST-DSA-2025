class Account:
    def __init__(self,accountno,accountholder,accountbalance):
        self.accountNo = accountno
        self.accountHolder = accountholder
        self.accountBalance = accountbalance
    def __str__(self):
        return self.accountHolder+" holds "+str(self.accountNo)+" with balance of "+str(self.accountBalance)+"\n"