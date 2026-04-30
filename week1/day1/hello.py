print("Hello, I am starting my AI Engineer journey!")


# String variables:
name = "Smadavaram Kumar Kumar"
company = 'Deloitte'

# Key string operations:
print(len(name))                    # 16 (length)
print(name.upper())                 # "SMADAVARAM KUMAR KUMAR - returns a new string in uppercase"
print(name.lower())                 # "smadavaram kumar"
print(name.replace("Kumar", "K"))  # "Smadavaram K - replace every occurrence of 'Kumar' with 'K'"
print(name.split(" "))              # ["Smadavaram", "Kumar"]
print(name[0])                      # "S" (first character, index starts at 0)
print(name[0:10])                   # "Smadavaram" (slicing: index 0 to 9)
print("Kumar" in name)              # True (check if substring exists)
print(name + " works at " + company)  # "Smadavaram Kumar works at Deloitte" (concatenation) - 
print("all the above functions return new strings, they do not modify the original string stored in the variable 'name'.")


# Numeric variables:
age = 25
big_number = 1_00_00_000    # 1 crore (underscores for readability)

print(age + 5)       # 30 (addition)
print(age - 5)       # 20 (subtraction)
print(age * 2)       # 50 (multiplication)
print(age / 5)       # 5.0 (division — ALWAYS returns float!)
print(age // 5)      # 5 (floor division — returns int)
print(age % 3)       # 1 (modulo — remainder)
print(age ** 2)      # 625 (power — 25 squared)
age += 5            # age is now 30 (increment)
print(age)          # 30
age -= 5            # age is now 25 (decrement)
print(age)          # 25
print("above operations do not modify the original variable 'age' unless we use an assignment operator like += or -=.")
print("/ always returns a float (5.0, not 5). Use // for integer division.")


# Float variables:

salary = 1500000.50
pi = 3.14159
percentage = 85.5

# Be careful with float precision:
print(0.1 + 0.2)    # 0.30000000000000004 (NOT 0.3!)
# This is a known issue in ALL programming languages, not just Python.
# For financial calculations, use the 'decimal' module instead.

print(round(0.1 + 0.2, 1))    # 0.3 (round to 1 decimal place)



# Boolean variables:
is_employed = True
is_student = False

# Booleans are the result of comparisons:
print(5 > 3)         # True
print(5 == 3)        # False (== checks equality, = assigns value)
print(5 != 3)        # True (not equal)
print(5 >= 5)        # True (greater than or equal)

# Logical operators:
print(True and False)   # False (both must be True)
print(True or False)    # True (at least one must be True)
print(not True)         # False (flips the value)

# Truthy and Falsy values (this trips up beginners):
# These are "falsy" (treated as False):
# 0, 0.0, "", [], {}, None, False
# Everything else is "truthy"

print(bool(0))        # False
print(bool(""))       # False
print(bool([]))       # False
print(bool("hello"))  # True
print(bool(42))       # True