class User:
    def __init__(self, name, email, int_rate = 0.02, balance = 0):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate, balance) 
        #link to methods
        
    def make_deposit(self, amount):
        self.account.deposit(amount)
        
    def make_withdrawl(self, amount):
        self.account.withdraw(amount)
        
    def display_user_balance(self):
        self.account.display_account_info()



class BankAccount:
    bankInfo = []

    @classmethod
    def printAll(cls):
        for balance, interest in cls.bankInfo:
            print('${:,.2f}'.format(balance), interest)

    # don't forget to add some default values for these parameters!

    def __init__(self, int_rate=.02, balance=0):
        self.int_rate = int_rate
        self.balance = balance

        BankAccount.bankInfo.append([self.balance, self.int_rate])
        # your code here! (remember, instance attributes go here)
        # don't worry about user info here; we'll involve the User class soon

    def deposit(self, amount):
        self.balance += amount
        return self

        # increases the account balance by the given amount

    def withdraw(self, amount):
        if amount < self.balance:
            self.balance -= amount
        else:
            self.balance -= 5
            print("Insufficient funds: Charging a $5 fee")

        return self

        # decreases the account balance by the given amount
        # if there are sufficient funds;
        # if there is not enough money,
        # print a message
        # "Insufficient funds: Charging a $5 fee" and deduct $5

    def display_account_info(self):
        print(self.balance)
        return self

        # print to the console: eg. "Balance: $100"

    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance * self.int_rate
        return self

    # increases the account balance
    # by the current balance * the interest rate
    # (as long as the balance is positive)


# j = BankAccount(.35, 945)
# j.deposit(500).display_account_info()

# j2 = BankAccount(.45, 10000)
# j2.deposit(50).deposit(10).deposit(45).withdraw(25).display_account_info()

# j3 = BankAccount(.65, 1450)
# j3.deposit(50).deposit(50).withdraw(5).withdraw(9).withdraw(
    # 8).withdraw(15).yield_interest().display_account_info()
    
# BankAccount.printAll()


jay = User('Jay', 'monkey@pm.me', .5, 95000)

jay.make_deposit(459)
jay.make_withdrawl(55)
jay.display_user_balance()



# print(jay.account.int_rate)
# print(jay.account.balance)















# [x ] Create a BankAccount class with the attributes interest rate and balance

# [ x ] Add a deposit method to the BankAccount class

# [ x ] Add a withdraw method to the BankAccount class

# [ x] Add a display_account_info method to the BankAccount class

# [ x ] Add a yield_interest method to the BankAccount class

# [ x ] Create 2 accounts

# [ x ] To the first account,
# make 3 deposits and 1 withdrawal,
# then yield interest
# and display the account's info all in one line of code (i.e. chaining)

# [ x ] To the second account,
# make 2 deposits and 4 withdrawals,
# then yield interest
# and display the account's info all in one line of code (i.e. chaining)

# [ x ] NINJA BONUS: use a classmethod
# to print all instances of a Bank Account's info
