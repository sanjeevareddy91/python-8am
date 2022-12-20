# operators : A symbol which performs the operation between 2 operands..

# 3+4

# 1) Arthimetic Operators(+,-,*,\,\\,%,**)
# 2) Relational or Comparision(==,!=,>,<,>=,<=)
# 3) Logical Operators(and,or,not)
# 4) Assignment Operators(=,+=,*=,.....)
# 5) Membership Operators(in,not in)
# 6) Identity Operators(is,is not)
# 7) Bitwise Operators(bitwise and(&),bitwise or(|),bitwise XOR(^),Bitwise NOT(~),Left SHift (<<),Right Shift(>>))



# / , //, %

# 13/3           13//3              13%3

# 3) 13(4.3333
#    12
# --------
#     10
#      9
# ---------
#      1


# 3) 13 (4.3333334
#    12
# -------
#     10
#      9
# --------
#      1

# 3) 13(4
#    12
# ------
#     1

# 3) 143(47
#    12
# -------
#     23
#     21
# -------
#      2

# print(13/3)
# print(13//3)
# print(13%3)
# print(143%3)

# print(3*2)
# print(3**2)


# Relational or Comparison Operators(==,!=,>,<,>=,<=): Output for these operators will be True/False only..

a=65

# print(a == 30)

# print(a != 30)

# print(a > 30)

# print(a < 30)

# print(a >= 30)

# print(a <= 30)

# a = 30

# 30 == 65

# Logical Operators(and, or, not):

# A         B          A and B         A or B          not(A)      not(A and B)    not((A or B) and (A and B))
# -------------------------------------------------------------------------------------------------------------
# T         F             F              T               F              T                    T 
# F         T             F              T               T              T                    T 
# T         T             T              T               F              F                    F 
# F         F             F              F               T              T                    T 


# username = "gsanjeevreddy91@gmail.com"
# password = "password@123"
# mobile = "9565065432"

# print(username == "gsanjeev@gmail.com" and password == "password@123") #  - F

# print((username == "gsanjeev@gmail.com" or mobile == "9565065432") and password == "password@123")


# username or mobile:

# username = ""

# print(not(username))

# pin = "1234"

# print(not(pin == "5456"))

# Assignment Operators(=,+=,-=,*=,\=,\\=,%=,**=)

# a = 56

# # a = a+5

# a += 5  # a = a+5

# print(a)

# a -= 5
# print(a)

# a *= 5
# print(a)

# a /= 5

# print(a)

# Datatypes of Python:
    # Numbers
        # integers (int) -- Any numerical without decimal points.
        # floating(float) -- Any numerical with decimal point..
    # String -- Anything declared between " " or ' ' or """ """
    # Lists -- sequence of values or elements which are declared between [ ] seperated with comma(,).
    # Tuples-- sequence of values or elements which are declared between ( ) seperated with comma(,).
    # Dictionary -- Sequence of key:value pair which are declared between { } seperated with comma(,).
    # Sets -- sequence of values or elements which are declared between { } seperated with comma(,) which contains unique elements..

# Membership Operators(in, not in): Output will be boolean(True/False)..


# a="python is a programming language"

# print("a" in a)

# print("is a" in a)

# a = ["64636376374","372873728","35232662767","43252552522"]

# print("3523266276" not in a)

# Identity Operators(is, is not):


# Immutable Datatypes : We cannot make the changes once the value is declared..
    # "Python",54,(54,67,'python',23)
# mutuable datatypes: Where we can make the changes after te declaration.
    # [23,'django',21,65], {'name':'username','email':'username@gmail.com'}.{21,54,76,12,'datascience'}


# a=43

# print(a is 43)
# print(a == 43)

# b="python"
# print(b is "python")
# print(b == "python")


# c=(54,67,'python',23)

# print(id(c))
# print(id((54,67,'python',23)))

# print(c is (54,67,'python',23))
# print(c == (54,67,'python',23))


# d = [23,'django',21,65]


# print(id(d))

# print(id([23,'django',21,65]))

# print(d is [23,'django',21,65])

# print(d == [23,'django',21,65])


# print(d is not [23,'django',21,65])


# Bitwise Operators(Bitwise AND(&),Bitwise OR(|),Bitwise XOR(^),Left Shift(<<),Right Shift(>>),Bitwise NOT(~))

# A      B         A & B      A | B       A ^ B 
# -----------------------------------------------
# 1      0          0           1            1 
# 0      1          0           1            1
# 1      1          1           1            0 
# 0      0          0           0            0

a=43

b=78

print(a&b)

print(bin(a))
print(bin(b))

# 2) 43 (
#     2) 21 - 1
#        2) 10 - 1
#            2) 5 - 0
#               2) 2 - 1
#                  1 - 0

# 43 - 101011
# 78 - 1001110

# 0101011
# 1001110
# ---------
# 0001010 -- 10
# 1101111 -- 111
# 1100101 -- 101

# 0001010  --2+8 - 10
# 1101111 -- 1+2 + 4+8+32+64

# print(a|b)
# print(a^b)

# print(int('1010',2))


# 43 << 1

# 00101011 ->> 01010110
# 
# print(43 << 1)

# 43 >> 1

# 00101011 --> 00010101

# print(43 >> 1)

# print(bin(-43))

# print(~100)


