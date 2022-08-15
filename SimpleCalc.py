num1 = int(input("Enter 1st number: "))
ope = input("Enter operator: ")
num2 = int(input("Enter 2nd number: "))

if(ope == "+"):
    print(num1 + num2)
elif(ope == "-"):
    print(num1 - num2)
elif(ope == "*"):
    print(num1 * num2)
elif(ope == "/"):
    print(num1/num2)
else:
    print("Error undefined")
