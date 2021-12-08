'''Bank Account Class
Create a Python class called BankAccount which represents a bank account, having as attributes: accountNumber (numeric type), name (name of the account owner as string type), balance.
Create a constructor with parameters: accountNumber, name, balance.
Create a Deposit() method which manages the deposit actions.
Create a Withdrawal() method which manages withdrawals actions.
Create an bankFees() method to apply the bank fees with a percentage of 5% of the balance account.
Create a display() method to display account details.'''




class BankAccount:
    def __init__(self,account_number,name,):
        self.accountnumber=account_number
        self.name=name
        self.__accountbalance=0  
    def deposit(self,funds):
        self.__accountbalance += funds
        print(f"Current account balance is ${self.__accountbalance} after a deposit of ${funds}")
    def withdrawal(self,funds):
        if self.__accountbalance <= funds:
            print("Insufficient funds")

        if self.__accountbalance >= funds:
            self.__accountbalance -= funds
            print(f"Account balance is ${self.__accountbalance} after a withdraw of ${funds}")
        
    def bankfees(self):
        if self.__accountbalance < 5: 
            print("Account blance must be atleast $5.00")
        if self.__accountbalance >= 5:
            self.__accountbalance *= .95
            print(f"You new account balance after ridiculously high 5% bank fees is ${self.__accountbalance}")
        
    def display(self):
        balance = (f"Your accountr balance is ${self.__accountbalance}")
        print(balance)


user_account=input('What is your account number: ')
user_name=input(F'What is the name on the account {user_account}? ')
#match with existing accounts
#add to dictionary?
 
user=BankAccount(user_account,user_name)
action_user=input(f"Hello {user_name}, for depoits press 1, for withdraws press 2, for balance press 3 and to pay your bank fees press 4: ")

for act in action_user: 
    user.deposit(5)#for testiing purpose 
    if action_user == "1":
        deposit_amt=float(input("Enter deposit amount: "))
        user.deposit(deposit_amt)
        
    if action_user == "2":
        withdraw_amt=float(input("Enter withdraw amount:"))
        user.withdrawal(withdraw_amt)
        
    if action_user == "3":
        user.display()
        
    if action_user == "4":
        user.bankfees()
        
    








