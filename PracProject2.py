try:
    a=int(input("Enter the number of Apples Harry has got: "))
    mn=int(input("Enter the minimum number of students you want to distribute to: "))
    mx=int(input("Enter the maximum number of students you want to distribute to: "))
except ValueError:
    print("Error as you did not enter numbers")
    exit()
if(mn==mx):
    print("\nRange is too small! as mn=mx")
    exit()
elif(mx<mn):
    print("\n'mx<mn' Please enter a valid range by restarting the program!")
    exit()
else:
    for i in range(mn,mx+1):
        if a%i==0:
            print(f"{i} is the divisor of {a}\n")
        else:
            print(f"{i} is not the divisor of {a}\n")
