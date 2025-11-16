num1 = int(input('Enter first number:'))
num2 = int(input('Enter second number')) 

print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")

choice = input("Enter your choice")

if choice=='1':
    result=num1+num2
    print(f"Result={result}")

elif choice=='2':
    result=num1-num2
    print(f"Result={result}")

elif choice=='3':
    result=num1*num2
    print(f"Result={result}")

elif choice=='4':
    if num2 !=0:
        result=num1/num2
        print(f"Result={result}")
    else:
        print("Error:Diviion by zero not possible")

else:
    print('Invalid input')
