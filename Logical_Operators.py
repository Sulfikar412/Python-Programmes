a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

x = a > 0
y = b > 0

print("Logical Operators")
print("-----------------")
print("a > 0 :", x)
print("b > 0 :", y)
print("AND (a > 0 and b > 0) :", x and y)
print("OR  (a > 0 or  b > 0) :", x or y)
print("NOT (not a > 0)       :", not x)
