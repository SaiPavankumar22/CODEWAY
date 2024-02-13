
n1 = float(input("Enter the first number: "))
n2 = float(input("Enter the second number: "))
print("Select operation:")
print("Add (+)")
print("Subtract (-)")
print("Multiply (*)")
print("Divide (/)")

operator = input("Enter the operation symbol (+, -, *, /): ")

if operator == '+':
    result = n1 + n2
elif operator == '-':
    result = n1 - n2
elif operator == '*':
    result = n1 * n2
elif operator == '/':
    if n2 != 0:
        result = n1 / n2
    else:
        result = "Cannot divide by zero"
else:
    print("Invalid Input")
    exit()
print("{0} {1} {2} = {3}".format(n1,operator,n2,result))
