# 🏧 Python OOP — Complete Guide with ATM & Banking App

> A deep-dive into every Object-Oriented Programming concept in Python, demonstrated through two real projects: an **ATM Machine** and a **Bank Mobile App**.

---

## 📚 Table of Contents

| # | Topic | Sub-topics |
|---|-------|------------|
| 1 | [🏛️ Class & Object](#%EF%B8%8F-1-class--object) | [Class](#-class) · [Object](#-object) · [Reference Variable](#-reference-variable) |
| 2 | [🔒 Encapsulation](#-2-encapsulation) | [Access Modifiers](#-access-modifiers) · [Private Variables](#-private-variables) · [Getters & Setters](#-getters--setters) · [Property Decorator](#-property-decorator) |
| 3 | [🧬 Inheritance](#-3-inheritance) | [Single](#-single-inheritance) · [Multiple](#-multiple-inheritance) · [Multilevel](#-multilevel-inheritance) · [super()](#-the-super-function) |
| 4 | [🎭 Abstraction](#-4-abstraction) | [Abstract Class](#-abstract-class) · [Abstract Method](#-abstract-method) · [ABC Module](#-abc-module) |
| 5 | [🔀 Polymorphism](#-5-polymorphism) | [Method Overriding](#-method-overriding) · [Method Overloading](#-method-overloading) · [Duck Typing](#-duck-typing) · [Operator Overloading](#-operator-overloading) |
| 6 | [🔧 Constructor](#-6-constructor) | [\_\_init\_\_](#-the-__init__-constructor) · [\_\_new\_\_](#-__new__-vs-__init__) · [Parameterized](#-parameterized-constructor) |
| 7 | [📦 Methods](#-7-methods) | [Instance](#-instance-methods) · [Class Method](#-class-methods) · [Static Method](#-static-methods) |
| 8 | [📊 Variables](#-8-variables) | [Instance Variables](#-instance-variables) · [Class / Static Variables](#-class--static-variables) |
| 9 | [📨 Pass by Reference vs Value](#-9-pass-by-reference-vs-value) | |
| 10 | [✨ Magic / Dunder Methods](#-10-magic--dunder-methods) | |
| 11 | [⚠️ Bugs in This Code](#%EF%B8%8F-11-bugs-found-in-this-code) | |
| 12 | [🗂️ Quick Reference Table](#%EF%B8%8F-12-concepts-quick-reference) | |

---

## 📄 Source Code

### 🏧 ATM Machine

```python
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
```

### 📱 Bank Mobile App (Abstraction Demo)

```python
from abc import ABC, abstractmethod

class BankApp(ABC):

    def database(self):
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

# We CANNOT make an object of Abstract class
# obj = BankApp()   ← TypeError
```

---

## 🏛️ 1. Class & Object

### 📌 Class

A **class** is a blueprint or template for creating objects. It defines what attributes (data) and methods (behaviour) every object of that type will have. Think of a class as a cookie cutter — the class is the mold, and each object is a cookie made from it.

**Syntax:**
```python
class ClassName:
    # attributes and methods
    pass
```

**In our ATM code:**
```python
class Atm:                   # ← The CLASS — blueprint for every ATM
    def __init__(self):
        self.__pin = ''
        self.__balance = 0
```

**In our Banking App code:**
```python
class BankApp(ABC):          # ← Abstract CLASS — blueprint for all bank apps
    pass

class MobileApp(BankApp):    # ← Concrete CLASS — a specific type of bank app
    pass
```

---

### 📌 Object

An **object** is a real instance created from a class. Each object occupies its own memory and holds its own data independently.

```python
obj = Atm()          # ← obj is an OBJECT (instance) of the Atm class
obj.menu()

obj2 = MobileApp()   # ← obj2 is an OBJECT of the MobileApp class
obj2.mobile_login()
```

You can create multiple independent objects from the same class:

```python
atm1 = Atm()
atm2 = Atm()

# They are completely independent
atm1.set_balance(5000)
print(atm2.get_balance())   # 0 — unaffected
```

---

### 📌 Reference Variable

A **reference variable** stores the memory address of an object, not the object itself. The variable is just a label pointing to where the object lives in memory.

```python
obj = Atm()     # obj is a REFERENCE VARIABLE pointing to the Atm object in memory
obj2 = obj      # obj2 points to the SAME object — not a copy!

obj2.set_balance(9999)
print(obj.get_balance())   # 9999 — both labels point to one object
```

```
Memory:
obj  ──┐
       ├──→  [ Atm object at 0x7f3a... ]
obj2 ──┘
```

> 💡 Setting `obj2 = None` does not delete the object — it just removes one label. The object is deleted only when no reference points to it (Python's garbage collector handles this).

---

## 🔒 2. Encapsulation

**Encapsulation** means bundling data and the methods that work on that data together inside a class, while restricting direct outside access. It protects an object's internal state from being accidentally or maliciously modified.

> 🔍 In our ATM: `__pin` and `__balance` are private — you cannot touch them directly. You must go through `get_balance()` / `set_balance()` or through the menu methods.

### 📌 Access Modifiers

Python uses **naming conventions** (not strict keywords like Java) to signal access levels:

| Convention | Type | Example | Accessible From |
|---|---|---|---|
| `name` | Public | `self.name` | Anywhere |
| `_name` | Protected | `self._balance` | Class + subclasses (by convention only) |
| `__name` | Private | `self.__pin` | Only inside the defining class |

---

### 📌 Private Variables

In the ATM code, both the PIN and balance are private:

```python
class Atm:
    def __init__(self):
        self.__pin = ''       # ← PRIVATE — double underscore prefix
        self.__balance = 0    # ← PRIVATE — double underscore prefix
```

Trying to access them directly from outside raises an error:

```python
obj = Atm()
print(obj.__pin)       # ❌ AttributeError
print(obj.__balance)   # ❌ AttributeError
```

Python achieves privacy through **name mangling** — `__pin` is stored internally as `_Atm__pin`:

```python
print(obj._Atm__pin)   # 😬 Technically works, but never do this
```

---

### 📌 Getters & Setters

Since private variables can't be accessed directly, the ATM code provides controlled access through **getter** and **setter** methods:

```python
class Atm:
    def __init__(self):
        self.__balance = 0

    def get_balance(self):            # GETTER — safely returns balance
        return self.__balance

    def set_balance(self, new_value): # SETTER — validates before setting
        if new_value >= 0:
            self.__balance = new_value
        else:
            print("Balance cannot be negative")

obj = Atm()
obj.set_balance(5000)
print(obj.get_balance())   # 5000
```

---

### 📌 Property Decorator

Python offers a cleaner, more Pythonic way to define getters and setters using `@property`:

```python
class Atm:
    def __init__(self):
        self.__balance = 0
        self.__pin = ''

    @property
    def balance(self):            # Called like an attribute: obj.balance
        return self.__balance

    @balance.setter
    def balance(self, value):     # Called like: obj.balance = 5000
        if value >= 0:
            self.__balance = value
        else:
            print("Invalid balance")

    @property
    def pin(self):
        return "****"             # Never expose the real PIN

    @pin.setter
    def pin(self, value):
        if len(str(value)) == 4 and str(value).isdigit():
            self.__pin = value
        else:
            print("PIN must be exactly 4 digits")

obj = Atm()
obj.balance = 5000     # Calls the setter
print(obj.balance)     # 5000 — calls the getter
print(obj.pin)         # ****
```

---

## 🧬 3. Inheritance

**Inheritance** lets a new class (child) acquire attributes and methods from an existing class (parent). It promotes code reuse and models "is-a" relationships.

```
BankApp  ──(is a parent of)──→  MobileApp
```

### 📌 Single Inheritance

One child class inherits from one parent class. This is exactly what our `MobileApp` code demonstrates:

```python
class BankApp(ABC):          # Parent
    def database(self):
        print("Connected to Database")

class MobileApp(BankApp):    # Child — inherits database() from BankApp
    def mobile_login(self):
        print("Login into the App")

obj = MobileApp()
obj.database()       # ✅ Inherited from BankApp
obj.mobile_login()   # ✅ MobileApp's own method
```

---

### 📌 Multiple Inheritance

A child class inherits from more than one parent class:

```python
class CardReader:
    def read_card(self):
        print("Card read successfully")

class CashDispenser:
    def dispense_cash(self):
        print("Cash dispensed")

class Atm(CardReader, CashDispenser):   # Inherits from BOTH
    pass

obj = Atm()
obj.read_card()       # From CardReader
obj.dispense_cash()   # From CashDispenser
```

**MRO — Method Resolution Order:**
When multiple parents have the same method, Python uses MRO to decide which one to call. You can inspect it:

```python
print(Atm.__mro__)
# (<class 'Atm'>, <class 'CardReader'>, <class 'CashDispenser'>, <class 'object'>)
```

---

### 📌 Multilevel Inheritance

A chain of inheritance — grandparent → parent → child:

```python
class Machine:
    def power_on(self):
        print("Machine powered on")

class BankMachine(Machine):
    def authenticate(self):
        print("User authenticated")

class Atm(BankMachine):
    def dispense(self):
        print("Cash dispensed")

obj = Atm()
obj.power_on()      # From Machine (grandparent)
obj.authenticate()  # From BankMachine (parent)
obj.dispense()      # From Atm (self)
```

---

### 📌 The `super()` Function

`super()` calls a method from the **parent class**. It is most important in `__init__` to ensure the parent is properly set up before the child adds its own initialization.

```python
class BankApp:
    def __init__(self, bank_name):
        self.bank_name = bank_name
        print(f"BankApp initialized: {bank_name}")

class MobileApp(BankApp):
    def __init__(self, bank_name, app_version):
        super().__init__(bank_name)   # ← Calls BankApp's __init__ first
        self.app_version = app_version
        print(f"MobileApp v{app_version} ready")

obj = MobileApp("PyBank", "2.0")
# Output:
# BankApp initialized: PyBank
# MobileApp v2.0 ready
```

`super()` also works for regular methods:

```python
class BankApp:
    def security(self):
        print("Base encryption enabled")

class MobileApp(BankApp):
    def security(self):
        super().security()              # Call parent's version first
        print("Biometric auth added")   # Then extend it

obj = MobileApp()
obj.security()
# Base encryption enabled
# Biometric auth added
```

---

## 🎭 4. Abstraction

**Abstraction** means hiding complex implementation details and exposing only what is necessary. Users of a class know *what* it does, not *how* it does it internally.

> 🔍 In our Banking App: `BankApp` defines *what* every bank app must do (`security`, `display`) without dictating *how*. Each subclass decides the how.

### 📌 ABC Module

Python implements abstraction through the `abc` (Abstract Base Class) module:

```python
from abc import ABC, abstractmethod
```

- `ABC` — the base class your abstract class must inherit from
- `@abstractmethod` — decorator that marks a method as abstract (must be overridden)

---

### 📌 Abstract Class

An abstract class **cannot be instantiated**. It acts as a contract — any class that inherits from it must implement all abstract methods.

```python
from abc import ABC, abstractmethod

class BankApp(ABC):           # ← Abstract class

    def database(self):       # ← Concrete method (has body, inherited as-is)
        print("Connected to Database")

    @abstractmethod
    def security(self):       # ← Abstract method (no body, MUST be overridden)
        pass

    @abstractmethod
    def display(self):        # ← Abstract method (no body, MUST be overridden)
        pass
```

```python
obj = BankApp()    # ❌ TypeError: Can't instantiate abstract class BankApp
                   #    with abstract methods: display, security
```

---

### 📌 Abstract Method

A method decorated with `@abstractmethod` is a **promise** — the abstract class says "every subclass will have this method" but leaves the implementation to each subclass.

```python
class MobileApp(BankApp):

    def mobile_login(self):          # Extra method unique to MobileApp
        print("Login into the App")

    def security(self):              # ✅ Implements the abstract contract
        print("Mobile security — Face ID enabled")

    def display(self):               # ✅ Implements the abstract contract
        print("Mobile display — 6 inch AMOLED")

obj = MobileApp()    # ✅ Works — all abstract methods are implemented
obj.mobile_login()
obj.database()       # ✅ Inherited concrete method from BankApp
```

What happens if a subclass skips an abstract method?

```python
class BrokenApp(BankApp):
    def security(self):
        print("security done")
    # display() not implemented!

obj = BrokenApp()   # ❌ TypeError: Can't instantiate BrokenApp
                    #    with abstract method: display
```

---

## 🔀 5. Polymorphism

**Polymorphism** means "many forms." The same method name behaves differently depending on which object calls it or how it is called.

### 📌 Method Overriding

A child class provides its own version of a method already defined in the parent. At runtime, Python always uses the most specific (child's) version.

```python
class BankApp:
    def security(self):
        print("Basic PIN security")

class MobileApp(BankApp):
    def security(self):              # ← OVERRIDES BankApp's security
        print("Mobile security — Biometric + PIN")

class WebApp(BankApp):
    def security(self):              # ← OVERRIDES BankApp's security
        print("Web security — OTP + CAPTCHA")

# Same method name, different behaviour
apps = [MobileApp(), WebApp()]
for app in apps:
    app.security()

# Mobile security — Biometric + PIN
# Web security — OTP + CAPTCHA
```

> 🔍 In our code: `MobileApp.security()` and `MobileApp.display()` both override the abstract methods from `BankApp`.

---

### 📌 Method Overloading

Python does **not** support traditional method overloading (same name, different parameter counts). If you define the same method twice, the second replaces the first. The Pythonic approach uses default arguments or `*args`:

```python
class Atm:
    # Simulating overloading with default parameters
    def deposit(self, amount, currency="INR", notify=True):
        self.__balance += amount
        if notify:
            print(f"Deposited {currency} {amount}. Balance: {self.__balance}")

obj = Atm()
obj.deposit(1000)                    # Uses defaults
obj.deposit(500, "USD")              # Custom currency
obj.deposit(200, "INR", False)       # No notification
```

Using `*args` for true variable-argument overloading:

```python
class Calculator:
    def add(self, *args):
        return sum(args)

calc = Calculator()
print(calc.add(10, 20))          # 30
print(calc.add(10, 20, 30, 40))  # 100
```

---

### 📌 Duck Typing

Python doesn't care about object *type* — only whether the object has the required method. "If it walks like a duck and quacks like a duck, it's a duck."

```python
class MobileApp:
    def display(self):
        print("Mobile display")

class WebApp:
    def display(self):
        print("Web browser display")

class ATMMACHINE:
    def display(self):
        print("ATM 7-inch touchscreen")

def render(app):
    app.display()   # Works for ANY object with a display() method

render(MobileApp())    # Mobile display
render(WebApp())       # Web browser display
render(ATMMACHINE())   # ATM 7-inch touchscreen
```

---

### 📌 Operator Overloading

Python allows you to redefine what operators like `+`, `==`, `>` do for your custom objects using magic methods:

```python
class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def __add__(self, other):       # Defines + operator
        return BankAccount(self.balance + other.balance)

    def __eq__(self, other):        # Defines == operator
        return self.balance == other.balance

    def __gt__(self, other):        # Defines > operator
        return self.balance > other.balance

    def __str__(self):
        return f"Account(₹{self.balance})"

a1 = BankAccount(1000)
a2 = BankAccount(2000)

merged = a1 + a2
print(merged)        # Account(₹3000)
print(a1 == a2)      # False
print(a2 > a1)       # True
```

---

## 🔧 6. Constructor

A **constructor** is a special method automatically called the moment an object is created. It sets up the object's initial state.

### 📌 The `__init__` Constructor

`__init__` is Python's primary constructor. It runs right after the object is created in memory.

```python
class Atm:
    def __init__(self):           # ← Constructor
        self.__pin = ''           # Initialize PIN as empty
        self.__balance = 0        # Initialize balance as zero
        print("ATM ready!")

obj = Atm()    # "ATM ready!" printed automatically — __init__ was called
```

---

### 📌 Parameterized Constructor

Constructors can accept arguments to initialize objects with custom values:

```python
class BankApp:
    def __init__(self, bank_name, version):
        self.bank_name = bank_name
        self.version = version
        print(f"{bank_name} App v{version} initialized")

app1 = BankApp("PyBank", "1.0")    # PyBank App v1.0 initialized
app2 = BankApp("SBI", "3.5")       # SBI App v3.5 initialized
```

---

### 📌 `__new__` vs `__init__`

Object creation is actually a two-step process in Python:

| Method | Role | Runs |
|---|---|---|
| `__new__(cls)` | **Creates** the object — allocates memory | First |
| `__init__(self)` | **Initializes** the object — sets attributes | Second |

```python
class Atm:
    def __new__(cls):
        print("Step 1: __new__ — memory allocated, object created")
        return super().__new__(cls)

    def __init__(self):
        print("Step 2: __init__ — object initialized")
        self.__balance = 0

obj = Atm()
# Step 1: __new__ — memory allocated, object created
# Step 2: __init__ — object initialized
```

> 💡 You almost never need to override `__new__` in everyday Python. It is mainly used for advanced patterns like Singleton or immutable types.

---

## 📦 7. Methods

A **method** is a function defined inside a class. Python has three distinct types.

### 📌 Instance Methods

The most common type. They receive `self` as the first argument and can read/modify instance-level attributes. Every method in the ATM code is an instance method.

```python
class Atm:
    def __init__(self):
        self.__balance = 0

    def deposit(self, amount):        # ← Instance method
        self.__balance += amount      # Accesses instance data via self

    def get_balance(self):            # ← Instance method (getter)
        return self.__balance
```

---

### 📌 Class Methods

Decorated with `@classmethod`. They receive `cls` (the class itself) as the first argument instead of an instance. They can access and modify class-level data but cannot touch instance attributes.

```python
class BankApp:
    total_apps = 0          # Class-level attribute

    def __init__(self):
        BankApp.total_apps += 1

    @classmethod
    def get_app_count(cls):                  # ← Class method
        return f"Total apps created: {cls.total_apps}"

app1 = MobileApp()
app2 = MobileApp()
print(BankApp.get_app_count())   # Total apps created: 2
```

---

### 📌 Static Methods

Decorated with `@staticmethod`. They receive neither `self` nor `cls`. They are utility functions that logically belong to the class but don't need any class or instance data.

```python
class Atm:
    @staticmethod
    def validate_pin(pin):                    # ← Static method
        return len(str(pin)) == 4 and str(pin).isdigit()

    @staticmethod
    def validate_amount(amount):
        return isinstance(amount, (int, float)) and amount > 0

# Called on the class — no object needed
print(Atm.validate_pin(1234))    # True
print(Atm.validate_pin(12))      # False
print(Atm.validate_amount(-50))  # False
```

**Comparison Summary:**

| | First Param | Access Instance Attrs | Access Class Attrs | Called On |
|---|---|---|---|---|
| Instance method | `self` | ✅ | ✅ | Object |
| Class method | `cls` | ❌ | ✅ | Class or Object |
| Static method | — | ❌ | ❌ | Class or Object |

---

## 📊 8. Variables

### 📌 Instance Variables

Defined inside methods using `self`. Each object gets its **own independent copy**. Changes to one object never affect another.

```python
class Atm:
    def __init__(self):
        self.__pin = ''       # Instance variable — unique per object
        self.__balance = 0    # Instance variable — unique per object

atm1 = Atm()
atm2 = Atm()

atm1.set_balance(5000)
print(atm2.get_balance())   # 0 — completely independent
```

---

### 📌 Class / Static Variables

Defined directly inside the class body (outside any method). **Shared across ALL instances** of the class — there is only one copy of the variable regardless of how many objects exist.

```python
class BankApp:
    bank_name = "PyBank"       # Class variable — shared
    total_apps_created = 0     # Class variable — shared counter

    def __init__(self):
        BankApp.total_apps_created += 1
        self.session_id = id(self)   # Instance variable — unique

app1 = MobileApp()
app2 = MobileApp()

print(app1.bank_name)              # "PyBank"
print(app2.bank_name)              # "PyBank" — same value
print(BankApp.total_apps_created)  # 2

# Modifying via class — affects all objects
BankApp.bank_name = "NewBank"
print(app1.bank_name)              # "NewBank"
print(app2.bank_name)              # "NewBank"
```

> ⚠️ **Pitfall:** If you do `app1.bank_name = "Other"`, Python creates a **new instance variable** that *shadows* the class variable for `app1` only. The class variable itself is unchanged. Always modify class variables through the class: `BankApp.bank_name = "Other"`.

---

## 📨 9. Pass by Reference vs Value

Python uses **pass by object reference** (also called "pass by assignment"). The behaviour depends on whether the object is mutable or immutable:

| Type | Examples | Behaviour |
|---|---|---|
| Immutable | `int`, `str`, `float`, `tuple` | Like pass by value — original unaffected |
| Mutable | `list`, `dict`, `set`, object | Like pass by reference — original can be changed |

```python
# --- Immutable (int) — like pass by value ---
def add_bonus(amount):
    amount += 500         # Creates a new int — original unchanged
    print(f"Inside: {amount}")

balance = 1000
add_bonus(balance)
print(f"Outside: {balance}")
# Inside: 1500
# Outside: 1000  ← unchanged

# --- Mutable (list) — like pass by reference ---
def add_transaction(history, amount):
    history.append(amount)   # Modifies the SAME list object

transactions = [100, 200]
add_transaction(transactions, 300)
print(transactions)   # [100, 200, 300] ← changed!
```

**With objects — the ATM example:**

```python
def reset_atm(atm_obj):
    atm_obj.set_balance(0)   # Modifies the original object

obj = Atm()
obj.set_balance(9999)
reset_atm(obj)
print(obj.get_balance())    # 0 — the object was modified
```

```
Memory view:
obj ──→ [ Atm object ]
              ↑
reset_atm also points here — same object, not a copy
```

---

## ✨ 10. Magic / Dunder Methods

**Magic methods** (double underscore methods, aka **dunder** methods) are special methods Python calls automatically in specific situations. They let you define how your objects behave with built-in operations, print statements, comparisons, and more.

| Method | Automatically triggered by | Common use |
|---|---|---|
| `__init__` | `Atm()` | Object initialization |
| `__new__` | Object creation | Memory allocation |
| `__str__` | `print(obj)`, `str(obj)` | Friendly string for users |
| `__repr__` | `repr(obj)`, REPL display | Debug string for developers |
| `__len__` | `len(obj)` | Custom length |
| `__eq__` | `obj1 == obj2` | Custom equality |
| `__lt__` | `obj1 < obj2` | Custom less-than |
| `__add__` | `obj1 + obj2` | Custom addition |
| `__del__` | Object garbage collected | Cleanup logic |
| `__call__` | `obj()` | Make object callable |
| `__contains__` | `x in obj` | Custom membership test |

**Applied to our ATM:**

```python
class Atm:
    def __init__(self):
        self.__pin = ''
        self.__balance = 0

    def __str__(self):
        # Called by print(obj) — human-friendly
        return f"ATM | Balance: ₹{self.__balance}"

    def __repr__(self):
        # Called by repr(obj) — developer-friendly
        return f"Atm(balance={self.__balance}, pin_set={bool(self.__pin)})"

    def __eq__(self, other):
        # Two ATMs are "equal" if they have the same balance
        return self.__balance == other.get_balance()

    def __del__(self):
        print("ATM session ended — object destroyed")

atm = Atm()
atm.set_balance(2000)

print(atm)           # ATM | Balance: ₹2000         ← __str__
print(repr(atm))     # Atm(balance=2000, pin_set=False)  ← __repr__
```

**Applied to BankApp — making it callable:**

```python
class MobileApp(BankApp):
    def security(self):
        print("Mobile security")

    def display(self):
        print("Mobile display")

    def __call__(self, action):
        print(f"App executing: {action}")

obj = MobileApp()
obj("transfer money")   # App executing: transfer money  ← __call__
```

---

## ⚠️ 11. Bugs Found in This Code

Here are the bugs in the original ATM code and how to fix each one:

| # | Bug | Where | Impact | Fix |
|---|---|---|---|---|
| 1 | `eval()` used for PIN/amount input | All methods | 🔴 Critical security hole — user can execute arbitrary Python code | Use `input()` with `int()` conversion |
| 2 | `create_pin` stores `True/False` not the actual PIN | `create_pin()` | 🔴 PIN is always `True` after creation | Fix the logic — see below |
| 3 | `if` chains instead of `elif` in `menu()` | `menu()` | 🟡 `else` always triggers for options 1–4 | Use `elif` |
| 4 | `else` only paired with last `if` in `menu()` | `menu()` | 🟡 "Thank you" prints for every input except option 5 | Use `if/elif/else` chain |
| 5 | No check if PIN exists before allowing transactions | All auth methods | 🟡 Can deposit/withdraw before PIN is ever set | Add `if not self.__pin` guard |
| 6 | Infinite recursion — methods call `menu()` endlessly | All methods | 🟠 Stack overflow on long use | Use `while True` loop |
| 7 | `withdraw_money` uses `>=` instead of `>` | `withdraw_money()` | 🟡 Cannot withdraw exact balance | Change `>=` to `>` |

**The critical `eval()` bug:**

```python
# ❌ DANGEROUS — user can type: __import__('os').system('rm -rf /')
user_pin = eval(input("Enter PIN: "))

# ✅ SAFE
user_pin = input("Enter PIN: ").strip()
```

**The `create_pin` logic bug:**

```python
# ❌ BROKEN — stores True/False, not the PIN
user_pin = len(eval(input("Enter 4 digit pin:...."))) == 4   # This is True or False!
reinter_pin = eval(input("Re-inter the 4 digit pin:.... "))
if user_pin == reinter_pin:     # True == 1234 → always False
    self.__pin = user_pin       # Stores True, not the PIN

# ✅ FIXED
def create_pin(self):
    user_pin = input("Enter 4 digit pin: ").strip()
    reenter_pin = input("Re-enter the 4 digit pin: ").strip()
    if len(user_pin) == 4 and user_pin.isdigit() and user_pin == reenter_pin:
        self.__pin = user_pin
        print("PIN created successfully")
    else:
        print("PIN must be 4 digits and both entries must match")
```

**Fully fixed `menu()` using `while` loop:**

```python
def menu(self):
    while True:
        user_input = input("""
        Hi, how can I help you?
        1. Create PIN
        2. Change PIN
        3. Deposit money
        4. Withdraw money
        5. Check balance
        6. Exit: """).strip()

        if user_input == '1':
            self.create_pin()
        elif user_input == '2':
            self.change_pin()
        elif user_input == '3':
            self.deposit_money()
        elif user_input == '4':
            self.withdraw_money()
        elif user_input == '5':
            self.check_balance()
        elif user_input == '6':
            print("--- Thank you for using ATM ---")
            break
        else:
            print("Invalid option. Please try again.")
```

---

## 🗂️ 12. Concepts Quick Reference

| Concept | Keyword / Symbol | Example from Code |
|---|---|---|
| Class | `class` | `class Atm:`, `class BankApp(ABC):` |
| Object | `ClassName()` | `obj = Atm()`, `obj = MobileApp()` |
| Constructor | `__init__` | `def __init__(self):` |
| Parameterized constructor | `__init__(self, arg)` | `def __init__(self, name):` |
| Reference variable | Variable holding object | `obj = Atm()` |
| Private variable | `__` prefix | `self.__pin`, `self.__balance` |
| Protected variable | `_` prefix | `self._balance` |
| Public variable | No prefix | `self.name` |
| Class / Static variable | Defined in class body | `bank_name = "PyBank"` |
| Instance variable | `self.name` in method | `self.__balance = 0` |
| Getter | `def get_x(self)` | `def get_balance(self):` |
| Setter | `def set_x(self, v)` | `def set_balance(self, v):` |
| Property | `@property` | `@property def balance(self):` |
| Instance method | `def method(self)` | `def menu(self):` |
| Class method | `@classmethod` + `cls` | `@classmethod def count(cls):` |
| Static method | `@staticmethod` | `@staticmethod def validate():` |
| Inheritance | `class Child(Parent)` | `class MobileApp(BankApp):` |
| Abstract class | `class X(ABC)` | `class BankApp(ABC):` |
| Abstract method | `@abstractmethod` | `def security(self): pass` |
| `super()` | `super().method()` | `super().__init__()` |
| Method overriding | Redefine in child | `def security(self):` in `MobileApp` |
| Method overloading | Default args / `*args` | `def deposit(self, amt, cur="INR")` |
| Duck typing | No type check needed | `app.display()` on any object |
| Operator overloading | `__add__`, `__eq__`, etc. | `def __eq__(self, other):` |
| Magic/dunder method | `__method__` | `__str__`, `__repr__`, `__del__` |
| Name mangling | `__x` → `_Class__x` | `obj._Atm__pin` (avoid!) |
| `@abstractmethod` | Forces subclass to implement | `@abstractmethod def security():` |

---

## 🚀 How to Run

```bash
# Clone the repository
git clone https://github.com/your-username/python-oop-atm.git
cd python-oop-atm

# Run ATM simulation
python atm.py

# Run Banking App abstraction demo
python bank_app.py
```

**Requirements:** Python 3.6+, no external libraries needed.

---

## 📁 Project Structure

```
python-oop-atm/
│
├── atm.py          # ATM Machine — Encapsulation, Constructors, Methods
├── bank_app.py     # Banking App — Abstraction, Inheritance, Polymorphism
└── README.md       # This file
```

---

## 📝 License

This project is open for learning. Fork it, break it, improve it — that's how you learn OOP. 🐍

---

> Built with ❤️ to master Python OOP — one concept at a time.
