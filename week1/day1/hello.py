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


# List are ordered, mutable , allow duplicates and can hold any type, and you can mix types
skills = ["Python", "Power Platform", "GitHub Actions"]
numbers = [1, 2, 3, 4, 5]
mixed = ["Ravi", 25, True, 3.14] #mixed types in a list is allowed but not recommended for data processing tasks

# Accessing elements (index starts at 0):
print(skills[0])       # "Python" (first element)
print(skills[-1])      # "GitHub Actions" (last element)
print(skills[0:2])     # ["Python", "Power Platform"] (slicing)

# Modifying lists:
skills.append("LangChain")       # Add to end → ["Python", "Power Platform", "GitHub Actions", "LangChain"]
skills.insert(1, "FastAPI")      # Insert at index 1
skills.remove("Power Platform")  # Remove by value
popped = skills.pop()            # Remove and return last element
skills.sort()                    # Sort alphabetically

# List length:
print(len(skills))    # Number of items

# Check if item exists:
print("Python" in skills)   # True

# List comprehension (VERY important — you'll use this daily):
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = [n for n in numbers if n % 2 == 0]    # [2, 4, 6, 8, 10]
squared = [n ** 2 for n in numbers]            # [1, 4, 9, 16, 25, ...]


# dictionaries are unordered, mutable, allow duplicates and can hold any type, and you can mix types
# A dictionary stores data as key: value pairs
person = {
    "name": "Ravi",
    "age": 25,
    "city": "Hyderabad",
    "skills": ["Python", "Power Platform"],
    "is_employed": True
}

# Accessing values:
print(person["name"])          # "Ravi"
print(person.get("salary"))    # None (doesn't crash if key missing)
print(person.get("salary", 0)) # 0 (default value if key missing)

# Modifying:
person["salary"] = 1500000       # Add new key-value pair
person["age"] = 26               # Update existing value
del person["is_employed"]        # Delete a key

# Useful methods:
print(person.keys())      # dict_keys(["name", "age", "city", ...])
print(person.values())    # dict_values(["Ravi", 26, "Hyderabad", ...])
print(person.items())     # dict_items([("name", "Ravi"), ("age", 26), ...])

# Check if key exists:
print("name" in person)   # True

# Nested dictionaries (like nested JSON):
api_response = {
    "status": "success",
    "data": {
        "user": {
            "name": "Ravi",
            "role": "AI Engineer"
        }
    }
}
print(api_response["data"]["user"]["name"])   # "Ravi"

# Why dictionaries matter: When you call the Anthropic API, the response looks like this:
response = {
    "content": [{"type": "text", "text": "Hello!"}],
    "model": "claude-sonnet-4-20250514",
    "usage": {"input_tokens": 10, "output_tokens": 5}
}
# You access it like:
answer = response["content"][0]["text"]   # "Hello!"


# tuples are ordered, immutable, allow duplicates and can hold any type, and you can mix types
coordinates = (28.6139, 77.2090)    # Delhi coordinates
rgb_color = (255, 128, 0)

# Access like lists:
print(coordinates[0])   # 28.6139

# But you CANNOT modify:
# coordinates[0] = 30.0   # ERROR! Tuples are immutable

# Tuple unpacking (very useful):
lat, lon = coordinates
print(f"Latitude: {lat}, Longitude: {lon}")

# When to use tuple vs list:
# Tuple → data that should NOT change (coordinates, RGB, database rows)
# List  → data that WILL change (shopping cart, task list)



#sets are unordered, mutable, do not allow duplicates and can hold any type, and you can mix types
skills = {"Python", "Python", "Java", "Python", "Java", "SQL"}
print(skills)    # {"Python", "Java", "SQL"} — duplicates removed automatically!

# Set operations:
frontend = {"HTML", "CSS", "JavaScript", "React"}
backend = {"Python", "Node.js", "JavaScript", "SQL"}

# appending to a set:
frontend.add("TypeScript")  # add a new skill to the frontend set
# sets do not maintain order, so the new skill may appear anywhere in the set when printed
# sets are unordered, so the order of elements is not guaranteed. When you print a set, the elements may appear in any order, and this can change each time you run the program. This is because sets are implemented as hash tables, which do not maintain any specific order of elements.
# sets are mutable, so you can add or remove elements after the set is created. However, since they are unordered, you cannot rely on the order of elements when you print the set or iterate over it. If you need an ordered collection, consider using a list or a tuple instead.
# deleting from a set:
frontend.remove("React")  # remove a skill from the frontend set 

print(frontend & backend)   # {"JavaScript"} — intersection (common)
print(frontend | backend)   # all unique skills — union
print(frontend - backend)   # {"HTML", "CSS", "React"} — in frontend but not backend


# tuples are ordered, immutable, allow duplicates and can hold any type, and you can mix types
# sets are unordered, mutable, do not allow duplicates and can hold any type, and you can mix types
# lists are ordered, mutable , allow duplicates and can hold any type, and you can mix types
# dictionaries are unordered, mutable, allow duplicates and can hold any type, and you can mix
# table of comparing data structures:
# | Data Structure | Ordered | Mutable | Allows Duplicates | Mixed Types Allowed |
# |----------------|---------|---------|-------------------|---------------------|
# | List           | Yes     | Yes     | Yes               | Yes                 |
# | Tuple          | Yes     | No      | Yes               | Yes                 |
# | Set            | No      | Yes     | No                | Yes                 |
# | Dictionary      | No      | Yes     | Yes (keys)       | Yes                 |




# String to int:
age_str = "25"
age_num = int(age_str)     # 25 (now a number)

# Int to string:
year = 2026
year_str = str(year)       # "2026" (now a string)

# String to float:
price = float("99.99")    # 99.99

# Check the type:
print(type("hello"))    # <class 'str'>
print(type(42))         # <class 'int'>
print(type(3.14))       # <class 'float'>
print(type(True))       # <class 'bool'>


# Type conversion can fail if the format is wrong:
# Basic print:
print("Hello World")

# Print multiple values:
name = "Ravi"
age = 25
print("Name:", name, "Age:", age)    # Name: Ravi Age: 25
print(f"Name: {name}, Age: {age}")  # Name: Ravi, Age: 25 (f-string formatting)
print("Name: " + name + ", Age: " + str(age))    # ERROR! Cannot concatenate str and int")

# Custom separator:
print("2026", "04", "29", sep="-")    # 2026-04-29

# Print without newline:
print("Loading", end="")
print("...")                # Loading... (on same line)


# Input from user:
name = input("Enter your name: ")     # Always returns a STRING
age = input("Enter your age: ")       # This is "25" (string), not 25 (number)!
age = int(input("Enter your age: "))  # Convert to int immediately



# Type checking:
x = 42
print(type(x))    # <class 'int'>
y = "hello"
print(type(y))    # <class 'str'>
# Useful for debugging:
data = input("Enter something: ")
print(type(data))  # Always <class 'str'>, no matter what you type


# f-strings:
name = "Ravi"
age = 25
salary = 1500000

# Old way (don't use):
print("My name is " + name + " and I am " + str(age) + " years old")

# f-string way (always use this):
print(f"My name is {name} and I am {age} years old")

# You can put ANY expression inside {}:
print(f"Next year I'll be {age + 1}")
print(f"Salary in lakhs: {salary / 100000}")
print(f"Name in caps: {name.upper()}")

# Formatting numbers:
print(f"Salary: ₹{salary:,}")           # Salary: ₹1,500,000
print(f"Pi: {3.14159:.2f}")              # Pi: 3.14
print(f"Percentage: {85.5:.1f}%")        # Percentage: 85.5%


# Conditional statements:
# Critical Python rule: INDENTATION MATTERS. Python uses indentation (4 spaces) instead of curly braces {} to define code blocks. If your indentation is wrong, your code breaks.
age = 25

if age < 18:
    print("Minor")
elif age < 60:
    print("Adult")
else:
    print("Senior")

# Output: Adult




# Comparison operators:
# ==  equal to
# !=  not equal to
# >   greater than
# <   less than
# >=  greater than or equal
# <=  less than or equal

# Combining conditions:
age = 25
has_experience = True

if age >= 21 and has_experience:
    print("Eligible for the role")

if age < 18 or not has_experience:
    print("Not eligible")




# Loop through a list:
skills = ["Python", "FastAPI", "LangChain"]
for skill in skills:
    print(f"I know {skill}")

# Loop with index using enumerate:
# enumerate() gives you both the index and the value as you loop through a list. The index starts at 0 by default, but you can specify a different starting point if needed.
for index, skill in enumerate(skills):
    print(f"{index + 1}. {skill}")
# Output:
# 1. Python
# 2. FastAPI
# 3. LangChain

# range() — generate a sequence of numbers:
for i in range(5):           # 0, 1, 2, 3, 4
    print(i)

for i in range(1, 6):        # 1, 2, 3, 4, 5
    print(i)

for i in range(0, 10, 2):    # 0, 2, 4, 6, 8 (step of 2)
    print(i)

# Loop through a dictionary:
person = {"name": "Ravi", "age": 25, "city": "Hyderabad"}
for key, value in person.items():
    print(f"{key}: {value}")




# While loop:
count = 0
while count < 5:
    print(f"Count is {count}")
    count += 1     # Don't forget this or you get an infinite loop!

# Practical example — keep asking until valid input:
while True:
    age = input("Enter your age (1-120): ")
    if age.isdigit() and 1 <= int(age) <= 120:
        age = int(age)
        break     # exit the loop
    else:
        print("Invalid! Try again.")


    

# break — exit the loop entirely:
for i in range(10):
    if i == 5:
        break
    print(i)    # prints 0, 1, 2, 3, 4

# continue — skip current iteration, go to next:
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)    # prints 1, 3, 5, 7, 9 (skips even numbers)



# Creating a set
skills = {"Python", "Java", "SQL", "Python"}
print(skills)    # {"Python", "Java", "SQL"} — duplicates removed automatically

empty_set = set()    # To create an empty set, use set(), NOT {} 
                     # {} creates an empty dictionary, not a set!

# Adding items:
skills.add("React")           # Add one item
skills.update(["Docker", "Git"])  # Add multiple items at once

# Removing items:
skills.remove("Java")         # Remove — gives ERROR if item doesn't exist
skills.discard("C++")         # Remove — NO error if item doesn't exist (safer!)
skills.pop()                  # Remove and return a random item
skills.clear()                # Remove ALL items (empty the set)

# Checking:
"Python" in skills            # True (is this item in the set?)
"Rust" not in skills          # True (is this item NOT in the set?)
len(skills)                   # Number of items

# Set operations (this is where sets really shine):
frontend = {"HTML", "CSS", "JavaScript", "React"}
backend = {"Python", "Node.js", "JavaScript", "SQL"}

# Intersection — what's COMMON in both:
frontend & backend                    # {"JavaScript"}
frontend.intersection(backend)        # {"JavaScript"} (same thing, different syntax)

# Union — EVERYTHING from both (no duplicates):
frontend | backend                    # {"HTML", "CSS", "JavaScript", "React", "Python", "Node.js", "SQL"}
frontend.union(backend)               # Same thing

# Difference — in first but NOT in second:
frontend - backend                    # {"HTML", "CSS", "React"}
frontend.difference(backend)          # Same thing

backend - frontend                    # {"Python", "Node.js", "SQL"}
backend.difference(frontend)          # Same thing

# Symmetric Difference — in one OR the other, but NOT both:
frontend ^ backend                    # {"HTML", "CSS", "React", "Python", "Node.js", "SQL"}
frontend.symmetric_difference(backend)  # Same thing (JavaScript is excluded because it's in BOTH)

# Subset and Superset:
small = {"Python", "SQL"}
big = {"Python", "SQL", "Java", "React"}

small.issubset(big)      # True (every item in small is also in big)
big.issuperset(small)    # True (big contains everything in small)
small.isdisjoint(backend)  # False (they share "Python" and "SQL")

# Looping through a set:
for skill in skills:
    print(skill)
# Note: order is NOT guaranteed! Sets are unordered.

# Converting between set and list:
my_list = [1, 2, 2, 3, 3, 3, 4]
unique = set(my_list)         # {1, 2, 3, 4} — quick way to remove duplicates!
back_to_list = list(unique)   # [1, 2, 3, 4] — convert back if you need a list

# Frozen set — an IMMUTABLE set (cannot add/remove):
permanent = frozenset(["Python", "SQL", "Git"])
# permanent.add("Java")  # ERROR! Cannot modify a frozenset