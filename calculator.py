def Addition(num1,num2):
    return num1 + num2

def Substraction(num1 , num2):
    return abs(num1-num2)

def Multiplication(num1 , num2):
    return num1*num2

def Division(num1  ,num2):
    return num1/num2

def Modules(num1 , num2):
    return num1%num2

def Percentages(num1 , num2):
    return (num1/num2)*100

def Power(num1 , num2):
    return num1 **num2

def Factorial(num):
    if num == 0:
        return 1
    return num*Factorial(num - 1)

# Main calculator function
def calculator():
    Operation = int(input("Plz select ur operation\n1.Addition\n2.Substraction\n3.Multiplication\n4.Division\n5.Modules\n6.Percentages\n7.Power\n8.Factorial\n"))

    if Operation ==  1:
        num1 = int(input("Enter the 1st values "))
        num2 = int(input("Enter the 2nd values "))
        print("The Addition is ",Addition(num1,num2))
    elif  Operation ==  2:
        num1 = int(input("Enter the 1st values "))
        num2 = int(input("Enter the 2nd values "))
        print("The Substraction is ",Substraction(num1,num2))
    elif  Operation ==  3:
        num1 = int(input("Enter the 1st values "))
        num2 = int(input("Enter the 2nd values "))
        print("The Multiplication is ",Multiplication(num1,num2))
    elif  Operation ==  4:
        num1 = int(input("Enter the 1st values "))
        num2 = int(input("Enter the 2nd values "))
        print("The Division is ",Division(num1,num2))
    elif  Operation ==  5:
        num1 = int(input("Enter the 1st values "))
        num2 = int(input("Enter the 2nd values "))
        print("The Modules is ",Modules(num1,num2))
    elif  Operation ==  6:
        num1 = int(input("Enter the 1st values "))
        num2 = int(input("Enter the 2nd values "))
        print("The Percentages is ",Percentages(num1,num2))
    elif  Operation ==  7:
        num1 = int(input("Enter the 1st values "))
        num2 = int(input("Enter the 2nd values "))
        print("The Power is ",Power(num1,num2))
    elif  Operation ==  8:
        num = int(input("Enter the  values "))
        print("The Factorial is ",Factorial(num))
    else:
        print("Incorrect Option")
        calculator()
calculator()
