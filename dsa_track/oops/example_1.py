class Atm:
    def __init__(self):
        self.pin = ""
        self.balance = 10000
        self.main()

    def main(self):
        user_input = input(
            """
        1. Check your balance
        2. If you want to change your pin
        3. Withdrawal
        4. Quit

        """
        )

        if user_input == "1":
            self.check_balance()
        elif user_input == "2":
            self.change_pin()
        elif user_input == "3":
            self.withdrawal()
        elif user_input == "4":
            exit()
        else:
            print("Invalid option, please choose any of the below options")
            self.main()

    def request_pin(self):
        user_pin = int(input("Enter Your PIN: "))
        self.pin = user_pin
        self.quit_continue_operation()

    def quit_continue_operation(self):
        opt = input("Enter Q to Quit or Y to Continue: ")
        if opt == "Y":
            self.main()
        elif opt == "Q":
            exit()
        else:
            self.quit_continue_operation()

    def check_balance(self):
        if self.pin:
            print("Your account balance is: ", self.balance)
        else:
            self.request_pin()
        self.main()

    def change_pin(self):
        if self.pin:
            new_pin = input("Enter your new PIN: ")
            self.pin = new_pin
            print("Your ATM PIN has been changed succssully!")
            self.main()
        else:
            self.request_pin()

    def withdrawal(self):
        if self.pin:
            amount = input("Enter the withdrawal amount: ")
            self.balance = self.balance - int(amount)
            print(
                f"{amount} is deducted from your account. Your current balance is: {self.balance}"
            )
            self.main()
        else:
            self.request_pin()


obj = Atm()
