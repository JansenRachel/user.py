class User:		# here's what we have so far
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    # adding the deposit method
    def make_deposit(self, amount):	# takes an argument that is the amount of the deposit
    	self.account_balance += amount	# the specific user's account increases by the amount of the value received
    def make_withdrawal(self, amount):
        self.account_balance -= amount
    def display_user_balance(self):
        print(f"User: {self.name}, Balance: ${self.account_balance}")
        # print(self.account_balance)
    # def transfer_money(self, name, amount):
    #     self.account_balance += amount
    #     name.account_balance -= amount

mitchell = User("Mitchell Caldwell", "mitchel@python.com")
kristy = User("Kristy Blair", "kristy@python.com")
darin = User("Darin James", "darin@python.com")

mitchell.make_deposit(250)
mitchell.make_deposit(550)
mitchell.make_deposit(100)
mitchell.make_withdrawal(200)
mitchell.display_user_balance()

kristy.make_deposit(200)
kristy.make_deposit(250)
kristy.make_withdrawal(100)
kristy.make_withdrawal(175)
kristy.display_user_balance()

darin.make_deposit(800)
darin.make_withdrawal(200)
darin.make_withdrawal(300)
darin.make_withdrawal(250)
darin.display_user_balance()



