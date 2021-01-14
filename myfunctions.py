print(str(5))

print(str(5.5))

print(str(True))

print(int("5"))

print(float("6.7"))

print(bool("True"))

print(len("Hello"))

arrLength = print(len([4,5,6]))

print(sorted([2, 3, 76, 43, 65, 12, 13, 66, 99, 53]))

# sorted with numbers then caps then small letters
print(sorted(["B", "R", "N", "F", "a", "5", "d", "3.5", "2"]))

#use snake case for function names
def my_function(str1, str2, str3):
    print("This is my function")
    print("second string inside this function , str1 = " + str(str1))
    print(str2)
    print(str3)

my_function(5555, 66, "this is arg3")

#separated print stmt using comma
def print_my_details(name, age, lastName="Singh"):
    print("My name is :", name, lastName, "and age is :", age)

print_my_details("Amrit", 31)
print_my_details("Amrit", 31, "Bagga")


# print using keyword args
print_my_details(age=30, name="Monty")

# infinite arguments
# *(asterik) denotes  array of all passed arguments
def print_people(*people):
    for person in people:
        print("This person is :", person)

print_people("Monty", "Amrit", "Honey")


# return value from function
def do_math(num1, num2):
    return num1 + num2

math1 = do_math(4, 5)
math2 = do_math(11, 33)

print("First sum is :", math1, "and second sum is :", math2)



