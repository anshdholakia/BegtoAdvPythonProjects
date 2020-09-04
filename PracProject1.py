def func(num):
    currentyear=2020
    return f"You will turn 100 years old in the year {(currentyear-num)+100}"
def func1(year):
    return f"You will turn 100 years old in the year: {year+100}"
a=int(input("Enter 1 for age and 2 for year of birth: "))
if a==1:
    age=int(input("Enter your age:"))
    if age>105:
        print("You seem to be the oldest person alive :)")
    else:
        print(func(age))
        b = int(input("Enter the year you want: "))
        while b<(2020-age):
            print("Please enter again")
            b = int(input("Enter the year you want: "))
        print(f"{b-(2020-age)}")
else:
    year=int(input("Enter your year of birth\n"))
    if (year>2020):
        print("You are not born yet!\n")
        exit()
    elif(year<1915):
        print("You are too old to use this!\n")
        exit()
    else:
        print(func1(year))
        b = int(input("Enter the year you want:"))
        while b < (year):
            print("Please enter again")
            b = int(input("Enter the year you want:"))
        print(f"{b-year}")