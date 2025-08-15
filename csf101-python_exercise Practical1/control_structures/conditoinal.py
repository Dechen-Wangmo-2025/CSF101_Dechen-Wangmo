number = int(input("give any number"))
if number > 0:
    print("The number is positive")
else: 
    print("The number is negative")
print()
number = 0 
if number > 0:
    print("positive")
elif number < 0:
    print("negative")
else:
    print("zero")
print()
score = int(input("enter your marks"))
if score >= 95:
    grade = "A"
elif score >= 80:
    grade = "B" 
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"
print(f"Your grade is: {grade}")
print()
number = int(input("enter any number"))
result = "even" if number % 2 == 0 else "odd"
print(f"The number is: {result}.")
print()
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
operator = "+, -, *, /2"

if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    result = num1 / num2 if num2 != 0 else "Error: Division by zero"
else:
    result = "Error: Invalid operator"

print(f"Result: {result}")
