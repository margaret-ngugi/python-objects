# class Account:
#     account_name="james"
# def __init__(self,account_number,account_holder,balance):
#     self.account_number=account_holder
#     self.account_holder=account_holder
#     self.balance=balance
# account=Account()    
# print({"Account.account_holder"})

#corr
class Account:
    def __init__(self,account_name):
        self.account_name=account_name
        self.balance=0
    def deposit(self,amount):
        self.balance+=amount
        return f"you have deposited {amount} your new balance is{self.balance}" 
    def withdraw(self,amount):
        if self.balance<=amount:
            self.balance-=amount
            return f"you have unknown {amount} your new balance is {self.balance}"
        else:
            f"your balance is {self.balance} you cannot widthdraw {amount}" 
                     
