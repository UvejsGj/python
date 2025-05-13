# print("Hello World")

# x = 10
# y = 10
# print(x * y)

# students_count = 1000
# rating = 4.99
# is_published = False 
# course_name = "Python Programming" 
# print(students_count)     

# course = "Python Programming" 
# print(len(course)) 
# print(course[0])
# print(course[-1])
# print(course[0:3])  
# print(course[0:])
# print(course[:3])
# print(course[:])


# escape_sequences in python 
# \"
# \' 
# \\
# \n

# course = "Python \nProgramming"
# print(course)

# first = "Uvejs"
# last = "Gjelaj"
# full = f"{len(first)} {3+6}"
# print(full)

# course = "python programming  "
# print(course.upper())
# print(course.lower())
# print(course.title())
# print(course.strip())
# print(course.find("Pro"))
# print(course.replace("p", "J"))

# x = 1
# x = 1.1
# x = 1 +2j 

# print(10 + 3)
# print(10 - 3)
# print(10 * 3)
# print(10 / 3)
# print(10 // 3)
# print(10 % 3)
# print(10 ** 3)

# x = 10
# x = x + 3
# x += 3 test

# import math

# print(round(2.6))
# print(abs(-2.9))
# print(math.ceil(1))

# x = input("x: ")
# y = int(x) + 1
# print(f"x: {x}, y: {y}")

# temperature = 69


# if temperature == 69:
#     print("💀🥀")
# elif temperature > 30:
#     print("hot day")
# elif temperature < 30:
#     print("cold day")
# elif temperature == 30:
#     print("average day")

# age = 22

# if age >= 18:
#     mesasge = "Eligible"
# else:
#     mesasge ="not Eligible"

# mesasge = "Eligible" if age >= 18 else "Not Eligible" 
# print(mesasge)

# high_income = False
# good_credit = True
# student = False

# if (high_income or good_credit) and not student:
#     print("jeni per kredi")
# else:
#     print("nuk jeni per kredi")

# age between 18 and 65

# age = 22

# if age >= 18 and age < 65:

# if 18 <= age < 65:
#     print("Eligible")

# if 10 == "10":
#     print("a")
# elif "bag" > "apple" and "bag" > "bag":
#     print("b")
# else:
#     print("c")

# print("Sending a Message")
# print("Sending a Message")
# print("Sending a Message")
# print("Sending a Message")

# for number in range(1, 10, 2):
#     print("Sending a goat", number, (number + 1) * ".")

# successful = True

# successful = False

# for number in range(3):
#     print("Attempt")
#     if successful:
#         print("Successful")
#         break
# else:
#     print("Attempted 3 times and failed") 

# for x in range(5):
#     for y in range(3):
#         print(f"({x}, {y})")

# shopping_cart = "fdshkjfghdlskjgfh"

# for item in shopping_cart:
#     print(item)

# if item > "5":
#     print("wow")

# number = 100
# while number > 0:
#     print(number)
#     number //= 2

# command = ""
# while command != "quit"

# while command.lower() != "quit":
#     command = input(">")
#     print("ECHO", command)
#     if command.lower() == "quit":
#         break

# while True:
#     command = input(">")
#     print("ECHO", command)
#     if command.lower() == "quit":
#         break

# number = 10

# while number > 0:
#     if number % 2 == 0:
#         print(number)
#     number -= 1
# print("we have 4 even numbers")

# count = 0 
# for number in range(1, 10):
#     if number % 2 == 0:
#         count += 1
#         print(number)
# print(f"We have {count} even numbers")

# people = 2

# def greet(first_name, last_name):
#     print(f"Hi {first_name} {last_name}")
#     print(f"Welcome Aboard {first_name}")


# greet("Uvejs", "Gjelaj")

# def greet(name):
#     print(f"Hi {name}")

# def get_greeting(name):
#    return f"Hi {name}"

# message = get_greeting("Uvejs")
# file = open("context.txt", "w")
# file.write(message)

# def greet(name):
#     print(f"Hi {name}")

# print(greet("Uvejs"))

# def increment(number, by=1):
#      return number + by

# print(increment(2, 5))


# def multiply(*numbers):
#     total = 1
#     for number in numbers:
#         total *= number
#     return total

# print(multiply(2, 3, 4, 5))

# age = 21
# age = 17

# try:
#     age = int(input("Enter your age: "))
#     print(door())
# except:
#     print("Invalid input.")

# def scan():
#     if age > 18:
#         return("Access allowed")
#     elif age < 18:                                # ignore function
#         return("Access denied")
#     else:
#         return("not age")

# def door():
#     if scan() == "Access allowed":
#         return("door open")
#     elif scan() == "Access denied":
#         return("door is closed")
#     else:
#         return("no door")

# # def final():
# #     if input() == int:
# #         print(door())


# try:
#     age = int(input("Enter your age: "))

#     def scan():
#         if age > 18:
#             return "Access allowed"
#         elif age < 18:
#             return "Access denied"
#         else:
#             return "not age"

#     def door():
#         if scan() == "Access allowed":
#             return "door open"
#         elif scan() == "Access denied":
#             return "door is closed"
#         else:
#             return "no door"

#     print(door()) 

# except:
#     print("Invalid input.")


try:
    age = int(input("Enter your age: "))

    def ticket():
        if age >= 1 and age <= 3:
            return "Free ticket"
        elif age >= 4 and age < 13:
            return "10 dollas"
        elif age >= 13 and age < 60:
            return "20 dollas"
        elif age >= 60:
            return "15 dollas"
        elif age < -0:
            return "cant be negative old"
        else:
            return("noage")

    print(ticket()) 

except:
    print("Invalid input.")
