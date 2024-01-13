# Method 1 Using if-elif statements
print('''
+ ADD
- SUBTRACT
* MULTIPLY
/ DIVIDE
''')
num1 = int(input("Enter the Value 1:- "))
num2 = int(input('Enter the Value 2:- '))
opr = input("Enter the Opr...(+,-,*,/)")

if opr == "+":
    print(num1 + num2)
elif opr == "-":
    print(num1 - num2)
elif opr == "*":
    print(num1 * num2)
elif opr == "/":
    print(num1 / num2)
else:
    print("Invalid Opr...")

# Method 2 using only if statements
print('''
+ ADD
- SUBTRACT
* MULTIPLY
/ DIVIDE
''')
num1 = int(input("Enter the Value 1:- "))
num2 = int(input('Enter the Value 2:- '))
opr = input("Enter the Opr...(+,-,*,/)")

if opr == "+":
    print(num1 + num2)
if opr == "-":
    print(num1 - num2)
if opr == "*":
    print(num1 * num2)
if opr == "/":
    print(num1 / num2)
if opr!= "+" and opr!= "-" and opr!= "*" and opr!= "/":
    print("Invalid Opr...")