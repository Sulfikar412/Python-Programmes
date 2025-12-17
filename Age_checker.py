birth_year = int(input("Enter your birth year : "))
birth_month = int(input("Enter your birth month : "))
birth_day = int(input("Enter your birth day : "))

current_year = int(input("Enter current year : "))
current_month = int(input("Enter current month : "))
current_day = int(input("Enter current day : "))

age = current_year - birth_year

if (current_month < birth_month) or (current_month == birth_month and current_day < birth_day):
    age = age - 1

print("You are", age, "years old!")
