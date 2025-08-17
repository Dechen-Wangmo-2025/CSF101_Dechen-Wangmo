def min_max(numbers):
    return min(numbers), max(numbers)

result = min_max([5, 2, 8, 1, 9])
print(f"Min: {result[0]}, Max: {result[1]}")
print()
def greet_with_default(name = "Guests"):
    print("Hi", {name})

greet_with_default()
greet_with_default("Namkha")
print()
def calculate_area(length, width):
    return length * width
a = input("Enter one side lenght")
b = input("Enter another side width")
area =calculate_area(int (a), int(b))
print(f"The area of the rectangle is: {area}")
print()
def print_info(**dwang):
    for key, value in dwang.items():
        print(f"{key}: {value}")
print_info(name = "namkha", age = 19, city = "Samdrupjongkhar")
print()
a = input("Enter a number: ")
b = input("Enter another number: ")
def safe_divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b

print(safe_divide(10, 2))
print(safe_divide(5, 0))