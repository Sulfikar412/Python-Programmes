def recurs_factorial(num):
    if num<=1:
        return 1
    return num*recurs_factorial(num-1)

number=int(input("Enter number :"))
print("factorial :",recurs_factorial(number))