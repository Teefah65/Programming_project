#\"
#/'
# \\
# \n



#course = "       python programming"
#print(len(course))
#print(course[0])
#print(course[0:3])

#cousera = "python \nprogramming"
"""print(cousera)


first = "Lateefat"
last = "Olasunkanmi"
full = f"{len(first)} {4+4}"
print(full)"""



#print(course.upper())
#print(course.lower())
#print(course.title())
#print(course.strip())
#print(course.find("pro"))
#print(course.replace("p", "k"))
#print("pro" in course) 
#print("swift" not in course)

# Numbers

x = 1
x = 1.1
x = 1 + 2j # a + bi

#print(10 + 3)
#print(10 - 3)
#print(10 * 3)
#print(10 / 3)
#print(10 // 3)
#print(10 % 3)
#|print(10 ** 3)


x = 10
x = x + 3
x += 3

#working with number
"""import math
print(round(2.99))
print(abs(-2.99))

print(math.ceil(2.2))
print(math.fabs(-56.78))"""


"""x = input("x: ")
y = int(x) + 1
print(f"x: {x}, y: {y}")"""

#falsy values
# ""
# 0
# None

#loop
"""for number in range(1, 10, 2 ):
    print("Attempt", number, (number) * ".")"""
    
    
#logical operators and or not

"""high_income = False
good_credit = True
student = False

if (high_income or good_credit) and not student :
    print("Eligible")
else:
    print("Not eligible")"""
    
#Iteration for loop
"""print(type(5))
print(type(range(5)))
for x in "Python":
    print(x)"""

#chaining comparison operator
#age should be between and 25
"""age = 22
if age >= 18 and age < 65:
    print("Eligible")
if 18 <= age < 65:
    print("Eligible")"""
    
    
#while loop
"""number = 100
while number > 0:
    print(number)
    number //= 2

command = ""
while command.lower() != "quit":
    command = input(">")
    print("ECHO", command)"""
    
#Exercise
"""count = 0
for number in range(1, 10):
    if number % 2 == 0:
        count += 1
        print(number)
print(f"We have{count} even numbers")"""

#Conditional statement
"""temperature = 15
if temperature > 30:
    print("It's warm")
    print("Drink water")
elif temperature > 20:
    print("It's nice")
else:
    print("It's cold")
print("Done")"""

#for else
"""successful = False
for number in range(3):
    print("Attempt")
    if successful:
        print("successful")
        break
else:
    print("Attempted 3 times and failed")"""

#infinite loop always find a way to jump out of a program
#nested loops
"""for x in range(5):
    for y in range(3):
        print(f"({x}, {y})")"""

#Tenary OPerator
"""age = 22
message = "Eligible" if age >= 18 else "Not eligible"
print(message)"""

#functions
"""def greet():
    print("Hi there")
    print("Welcome aboard")
    
    
greet()"""

#Argument
"""def greet(first_name, last_name):
    print(f"Hi {first_name} {last_name}")
    print("Welcome aboard")
    
    
greet("Mosh", "Layla")
greet("Tom", "Abdul")"""

#types of functions 2 types functions that perform a task and one that returns value
# all functions by default return none value unless specifically stated to return a value
"""def greet(name):
    print(f"Hi {name}")
    
    
def get_greeting(name):
    return f"Hi {name}"

message = get_greeting("Abdul")
file = open("context.txt", "w")
file.write(message)"""

#keywords arguments
"""def increment(number, by):
    return number + by
    
    
print(increment(2, by=1))"""

#default argument
"""def increment(number, by=1):
    return number + by


print(increment(2, 6))"""

#xargs wait, what?
"""def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total



print(multiply(2,3,4,5,6,7))"""   

#xxargs    
"""def save_user(**user):
    print(user["name"])
    
    
save_user(id = 1, name ="Parsley", age = 34)"""

#Scope refers to the region of the code where variable is defined
# we have global variable and local variable global overrides local
#global variable is mostly outside the function while local variable is in the function
# def greet(name):
#     message = "a"
    
# def send_email(name):
#     message = "b"
    
# greet("Par")

#debugging read again you didn't get it with the laptop you are using

# exercise
# def fizz_buzz(input):
#     if (input % 3 == 0) and (input % 5 == 0):
#         return "FizzBuzz"
#     if input % 3 == 0:
#         return "Fizz"
#     if input % 5 == 0:
#         return "Buzz"
#     return input
    
    
# print(fizz_buzz(7))

#DATA STRUCTURES LIST[], TUPLES(), DICTIONARY{} AND SETS
#LISTS..
# letters =["a", "b", "c"]
# matrix = [[0,1], [2,3]]
# zeros = [0] * 5
# combined = letters + zeros
# numbers = list(range(30))
# chars = list("Hello World")
# print(len(chars))

#ACCESSING ITEMS SLICING LIST BY USING :
# letters = ["a", "b", "c", "d"]
# letters[0] = "A"
# print(letters[0:3])
# print(letters[::2])

# numbers = list(range(20))
# print(numbers[::-1])

#LIST UNPACKING
# numbers = [1, 2, 3, 4, 5, 6, 7, 8]
# first, second, *other = n umbers
# print(second)
# print(other)  

#LOOPING OVER LISTS
# letters = ["a", "b", "c"]
# items = (0, "a")
# index, letter = items
# for index, letters in enumerate(letters):
#     print(index,letters)

# ADDING OR REMOVING ITEMS IN A LIST ; ADD we use append, remove we use pop, del remove a range of items and clear remove of the obj in the list
# letters = ["a", "b","c"]
# letters.append("d")
# letters.insert(0, "-")

# letters.pop(0)
# letters.remove("b")
# del letters[0:3]
# print(letters)

#FINDING ITEMS IN LIST
# letters = ["a", "b", "c"]
# print(letters.count("d"))
# if "d" in letters:
#     print(letters.index("d"))

#SORTING LIST
#numbers =[3,51,2,8,6,9,4]
#numbers.sort(reverse=True)
#print(sorted(numbers, reverse=True))
#print(numbers)


# items = [
#     ("Product1", 10),
#     ("Product2", 9),
#     ("Product3", 12),
# ]

# def sort_item(item):
#     return item[1]


# items.sort(key=lambda item:item[1])
# print(items)


#lambda
# lambda is a one line anonymous function dat can be passed to other functions
# items.sort(key=lambda item:item[1])
# print(items)

#Map Function
# items = [
#      ("Product1", 10),
#      ("Product2", 9),
#      ("Product3", 12),
#  ]

# """prices = []
# for item in items:
#     prices.append(item[1])"""
    
# prices = list(map(lambda item: item[1], items))

# print(prices)

#filter function
# items = [
#       ("Product1", 10),
#       ("Product2", 9),
#       ("Product3", 12),
#   ]

# filtered = list(filter(lambda item: item[1] >= 10, items))
# print(filtered) 


#list comprehension performant  and beautiful code
# items = [
#       ("Product1", 10),
#       ("Product2", 9),
#       ("Product3", 12),
#   ]

# prices = [item[1] for item in items]

# filtered = [item[1] for item in items if item[1] >= 10]


#Zip function
# list1 = [1, 2, 3]
# list2 = [10, 20, 30]

# print(list(zip("abc", list1, list2)))

#Stacks
browsing_session = []
browsing_session.append(1)
browsing_session.append(2)
browsing_session.append(3)
print(browsing_session)
last = browsing_session.pop()
print(last)
print(browsing_session)
print("redirect", browsing_session[-1])
if not browsing_session:
    print("disable")