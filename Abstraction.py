from abc import ABC, abstractmethod
class BankApp(ABC):

    def datbase(self):
        print("Connected to Database")

    @abstractmethod
    def security(self):
        pass

    @abstractmethod
    def display(self):
        pass

class MobileApp(BankApp):

    def mobile_login(self):
        print("Login into the App")

    def security(self):
        print("Mobile security")

    def display(self):
        print("Display")

obj = MobileApp()
obj.mobile_login()


# We can not make an object of Abstract class
# obj = BankApp()