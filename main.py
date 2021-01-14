# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

print(5+6)
print(int("44"))
print("hello, don't do that")
print('hello, don\'t do that')
mystr = "Hello, " + "Nick"
print(mystr)

mystr2 = "This cost " + str(6 + 5) + " dollars"
print(mystr2)

mystr3 = "my name is " + "hello:nick".split(":")[1]
print(mystr3)

print(5 == 5) #True
print(mystr2 == mystr3) # False

# print(5 is 5) #True

# print (4 is not 6) # True

# print ("This" is not 6) #True

# print ("True" is str(True)) #True

#list, arrays
arr = [1,2,3,4,5,6]

#
arr1 = ["movies", "games", "python", str(16), "18"]
print(arr1[3])

# dictionaries (like json key-value)
mydict = {"name":"amrit", "age":31, "hobbies":["code", "movies"], 'ItemA': [123456, 123654], 'ItemB': [456789, 456987]}
print(mydict)
print(mydict["name"])
print(mydict["age"])
print(mydict["hobbies"])

# variables
abc = 555
mystr4 = "hello world"
print(mystr4 + str(abc))
greeting = mystr4.split(" ")[0] + " Monty"
print(greeting)

number = 1
secondNumber = 2
print(number * secondNumber * secondNumber * number)

check = True
print(check)

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
