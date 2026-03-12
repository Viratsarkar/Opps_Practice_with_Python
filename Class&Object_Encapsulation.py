class Atm:

    def __init__(self):
        self.__pin = ''
        self.__balance = 0

    def get_balance(self):
        return self.__balance

    def set_balance(self, new_value):
        self.__balance = new_value


    def menu(self):
        user_input = input("""
        Hi how can I help you?
        1. Press 1 to create pin
        2. Press 2 to change pin
        3. Press 3 to deposite money
        4. Press 4 to withdraw money
        5. Press 5 to check balance
        6. Press anything else to exit......  """)

        if user_input == '1':
            self.create_pin()
        if user_input == '2':
            self.change_pin()
        if user_input == '3':
            self.deposite_money()
        if user_input == '4':
            self.withdraw_money()
        if user_input == '5':
            self.check_balance()
        else:
            print("---Thank you for using ATM---")
    def create_pin(self):
        
        user_pin = len(eval(input("Enter 4 digit pin:...."))) == 4
        reinter_pin = eval(input("Re-inter the 4 digit pin:.... "))
        
        if user_pin == reinter_pin:
            self.__pin = user_pin
            print("Pin created Successfully")
        else:
            print("Entered incorrect pin")
        self.menu()

    def change_pin(self):
        user_pin = eval(input("Enter 4 digit pin:...."))
        if self.__pin == user_pin:
            new_pin = eval(input("Enter new 4 digit pin:...."))
            self.__pin = new_pin
            print("Pin changed successfully")
        else:
            print("Entered incorrect pin")
        self.menu()

    def deposite_money(self):
        user_pin = eval(input("Enter your 4 digit pin...."))
        if user_pin == self.__pin:
            user_amount = eval(input("Enter the Amount...."))
            if user_amount <= 0:
                print("Negative or 0 amount can not deposite")
            else:
                self.__balance += user_amount
                print("Balance deposite successfully")
        else:
            print("Entered incorrect pin")
        self.menu()

    def withdraw_money(self):
        user_pin = eval(input("Enter your 4 digit pin...."))
        if user_pin == self.__pin:
            user_amount = eval(input("Enter the Amount...."))
            if user_amount >= self.__balance:
                print("Insufficient Balance")
            else:
                self.__balance -= user_amount
                print("Balance withdrawl successfully")
                print("\n The available Balance is: ", self.__balance)
        else:
            print("Entered incorrect pin")
        self.menu()

    def check_balance(self):
        user_pin = eval(input("Enter your 4 digit pin...."))
        if user_pin == self.__pin:
            print("The available is: ", self.__balance)
        else:
            print("Entered incorrect pin")
        self.menu()

obj = Atm()
obj.menu()











