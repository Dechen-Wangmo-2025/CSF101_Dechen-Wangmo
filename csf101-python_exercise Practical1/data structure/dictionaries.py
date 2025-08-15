name =input("what is your name")
age = input ("How old are you?")
height = input("how tall are you")
is_student = True
personal_info = {
    "name":name,
    "age":age,
    "height":height,
    "is_student":is_student
}
print(personal_info)
personal_info["favorite_color"] = ("green")
print(personal_info)