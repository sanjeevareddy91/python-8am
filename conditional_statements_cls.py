
# Conditional Statements : Those Statements which will be executed based upon certain conditons..

# age = 12

# print("Your age is",age,"you are eligible for voting.")


# if condition
# if-else condition
# if-elif-else condition

# if statement:

# Syntax of if condition:

# if condition:
#     statements(line of codes)

# Indentation : block of code writing in python..

# age = 32

# input() -- It will ask the user to provide the input..

# age = int(input("Enter age:"))


# print(type(age))

# if age >= 18:
#     print("Your age is",age,"you are eligible for voting.")

# print("Your age is",age,"you are not eligible for voting.")

# if-else statements:
"""
if condition:
    statements
else:
    statements
"""

# age = int(input("Enter age:"))

# if age >= 18:
#     print("Your age is",age,"you are eligible for voting.")
# else:
#     print("Your age is",age,"you are not eligible for voting.")


# if-elif-else Statements

"""
if condition:
    statements
elif condition:
    statements
else:
    statements
"""

# Before writing the elif statement, if statement is mandatory..

# percentage = float(input("Enter your percentage:"))


# if percentage >= 70:
#     print("You got distinction!")
# elif percentage >= 60 and percentage < 70:
#     print("You got First Class!")
# elif percentage >= 50 and percentage < 60:
#     print("You got Second Class!")
# else:
#     print("Just passed Candidate!")

# Nested Conditons:

# district = "kadapa"
# city = "produttur"

# district1 = input("Enter your district:")

# if district == district1:
#     city1 = input("Enter your city:")
#     if city1 == city:
#         print("You are from ",district1,"and from ",city1)
#     else:
#         print("Your district is ",district1,"We dont know you city")
# else:
#     print("Match not found!")


# pin -- 1234
    # acccountype - saving
        # amount to withdraw:
            # 3000 has been debited from your account..
    # acccountype doesnot matched!
# Pin incorrect!