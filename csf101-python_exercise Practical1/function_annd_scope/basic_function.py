def greet():
    print("Good Morning!")
greet()
print()
def greet(name):
    print(f"Hi, {name}")
greet("Namkha")
def square(number):
    return number ** 3
result = square(6)
print(f"The square of the number is: {result}")
print()
def is_even(number):
    return number % 2 == 0 
print(is_even(6)) #TRUE
print(is_even(7)) #FALSE
print()
def print_numbers(d):

    for a in range(2, d+1):
        print(a)
print_numbers(10)

