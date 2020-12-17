# s = r"C:\\d\new.txt"  # r"" - raw string
# print(s)

# s = "Py" "thon"
# print(s)

# s1 = "Hello, "
# s2 = "World!"
# s3 = s1 + s2
# print(s3)

# name = "John"
# age = 20
#
# print("My name is" + name + " I'm " + str(age))

# print("Hi " * 10)

# ---String indexing

# s = "Hello World!"
# print(s[0])
# print(s[12])
# print(s[-1])
# s[0] = "D"

"""
+---+---+---+---+---+---+---+---+---+---+---+---+
| H | e | l | l | o |   | W | o | r | l | d | ! |
+---+---+---+---+---+---+---+---+---+---+---+---+
0   1   2   3   4   5   6   7   8   9   10  11  12
-12 -11 -10 -9 -8  -7  -6  -5  -4  -3  -2  -1
"""

# [X:Y:Z]  X - start, Y - end, Z - step

s = "Hello World!"

print(s[0:12])  # Hello World!
print(s[-1])  # !
print(s[0:5])  # Hello
print(s[:5])  # Hello
print(s[6:12])  # World!
print(s[6:])  # World!
print(s[::2])  # HloWrd
print(s[::-1])  # !dlroW olleH
print(s[:5] + s[6:])  # HelloWorld!




