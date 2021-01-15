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


# conditional statements

#check = False
check = "hello"
if(check == True):
    print("It is true")
elif check == "hello":
    print("hello greetings..!!")
elif check == "hii":
    print("hii greetings..!!")
else:
    print("It is false")

myNumbers = [1, 3, 4, 5]

for item in myNumbers:
    print(item)

# print from 1 to 20 using while
idx = 0
run = True

while run:
    if idx == 21:
        run = False
    else:
        print(idx)
        idx += 1

# importing regex libraries
mystr5 = "'I AM NOT YELLING', she said. Though we know it to be not true."
import re
# sub params - match, replace on string
newMyStr5 = re.sub('[A-Z]', '', mystr5) # replace caps with empty
print(newMyStr5)
newMyStr6 = re.sub('[a-z]', '', mystr5) # replace small letters with empty
print(newMyStr6)

newMyStr6 = re.sub('[.,\'A-Z+" "]', '', mystr5) # replace special char, space and small letters
print(newMyStr6)

mystr5 = mystr5 + "44 298 - 345"
print(mystr5)
newMyStr6 = re.sub('[^0-9]', '', mystr5) #replace all which are not numbers with nothing
print(newMyStr6) #44298345
