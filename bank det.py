class Bank():
    def __init__(self, username, password, amount=0):
        self.username = username
        self.password = password
        self.amount = amount

    def login(self):
        enter_username = input("Enter your username:")
        enter_password = input("Enter your password:")
        return enter_username == self.username and enter_password == self.password

    def deposit(self, amount):
        self.amount += amount
        print("Amount successfully deposited")

    def withdraw(self, Amount):
        if self.amount - Amount >= 500:
            self.amount = self.amount - Amount
            print("Amount successfully withdrawn")
        else:
            print("Insufficient bank balance")
    def display(self):
        print("Your bank balance is:", self.amount)

    def run(self):
        while True:
            print("1.login\n2.exit")
            options1 = int(input("Enter your choice: "))
            if options1 == 2:
                print("Exiting..")
                break
            elif options1 == 1:
                if self.login():
                    while True:
                        print("1.Deposit\n2.Withdraw\n3.Display\n4.exit")
                        options = int(input("Enter your choice: "))
                        if options == 1:
                            deposit_amount = float(input("Enter amount to deposit: "))
                            self.deposit(deposit_amount)
                        elif options == 2:
                            withdraw_amount = float(input("Enter amount to withdraw: "))
                            self.withdraw(withdraw_amount)
                        elif options == 3:
                            self.display()
                        elif options == 4:
                            print("Exiting...")
                            break
                else:
                    print("Invalid username or password. Please try again.")
            else:
                print("Invalid option. Please enter a valid choice.")

# Create an instance of the Bank class
user_bank = Bank(username="user1", password="12345", amount=1000)

# Run the program
user_bank.run()






