def power(num,i):
    if i<=0:
        return 1
    return num*(power(num,i-1))

base=int(input("Enter base number :"))
exponent=int(input("Enter exponent number :"))
print(f"{base}^{exponent} is :",power(base,exponent))