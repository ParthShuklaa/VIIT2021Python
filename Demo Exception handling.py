

try:
    Name = input("Enter Your name")
    print(Name)

    Value = 10/0
except ZeroDivisionError:
    print("You cant divide a no by Zero")

except:
    print("Caught Exception")

finally:
    print("Thank you for using our Applications")