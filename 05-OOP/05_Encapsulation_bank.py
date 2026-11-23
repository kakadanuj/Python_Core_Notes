# Encapsulation: keep data private and control access with getter and setter

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance              # private attribute

    def get_balance(self):                    # getter
        return self.__balance

    def set_balance(self, balance):           # setter with validation
        if balance >= 0:
            self.__balance = balance
        else:
            print("Balance cannot be negative.")


account = BankAccount(1000)
print(account.get_balance())

account.set_balance(-1500)                    # rejected
print(account.get_balance())

account.set_balance(2500)                     # accepted
print(account.get_balance())

# Access modifiers in Python are conventions:
#   name     -> public
#   _name    -> protected (by convention)
#   __name   -> private (name mangling)
# print(account.__balance)                    # AttributeError
