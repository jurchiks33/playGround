 # PEP 8 guidelines for writing style at https://python.org/dev/peps/pep-0008.

# THIS FILE IS MADE OF FUNDAMENTAL PYTHON CONCEPTS. 
# FOR A BIGGER PROJECTS IN A PLAYGROUND LOOK IN OTHER PY FILES

                                       #Variables

# message = "Hello Python World"
# print(message)

# message = "Hello Python World 2"
# print(message)

# message = "I am an error message"
# print(mesage)

                                        #Capital Letters

# name = "ada lovelace"
# print(name.title())

# name = "ada Lovelace"
# print(name.upper())
# print(name.lower())

                                #Variable in strings 20.   <<f>> is for format

# first_name = "ada"
# last_name = "lovelace"
# full_name = f"{first_name} {last_name}"
# print(full_name)

# first_name = "ada"
# last_name = "lovelace"
# full_name = f"{first_name} {last_name}"
# print(f"Hello {full_name.title()}")

# first_name = "ada"
# last_name = "lovelace"
# full_name = f"{first_name} {last_name}"
# message = f"Hello, {full_name.title()}"
# print(message)

                                        #Lists

# bicycles = ['trek', 'cannondale', 'redline', 'specialized']
# print(bicycles)

# bicycles = ['trek', 'cannondale', 'redline', 'specialized']
# print(bicycles[1])

# bicycles = ['trek', 'cannondale', 'redline', 'specialized']
# print(bicycles[1].title())

# bicycles = ['trek', 'cannodale', 'redline', 'specialized']
# print(bicycles[1])
# print(bicycles[2])

# bicycles = ['trek', 'cannodale', 'redline', 'specialized']
# print(bicycles[-1])

# bicycles = ['trek', 'cannodale', 'redline', 'specialized']
# message = f"My first bicycle was a {bicycles[0].title()}. and after {bicycles[1].upper()}"
# print(message)

# motorcycles = ['honda', 'yamaha', 'suzuki']
# print(motorcycles)

# motorcycles[0] = 'ducati'
# print(motorcycles)

# motorcycles[-1] = 'stella'
# print(motorcycles)

# motorcycles = ['honda', 'yamaha', 'suzuku']
# motorcycles.append('ducatti')
# print(motorcycles)


# motorcycles = []
# motorcycles.append('honda')
# motorcycles.append('yamaha')
# motorcycles.append('suzuki')
# motorcycles.append('ducatti')
# print(motorcycles)

# motorcycles = ['honda', 'yamaha', 'suzuki']
# print(motorcycles)
# del motorcycles[0]
# print(motorcycles)

# motorcycles = ['honda', 'yamaha', 'suzuki']
# print(motorcycles)
# popped_motorcycle = motorcycles.pop()
# print(motorcycles)
# print(popped_motorcycle)

# motorcycles = ['honda', 'yamaha', 'suzuki']
# first_owned = motorcycles.pop(0)
# print(f"The first motorcycle I owned was a {first_owned.title()}.")

# motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
# print(motorcycles)
# motorcycles.remove('ducati')
# print(motorcycles)

# motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
# print(motorcycles)
# too_expensive = 'ducati'
# motorcycles.remove(too_expensive)
# print(motorcycles)
# print(f"\nA {too_expensive.title()} is too expensive for me.")

# guest_list = ['misterA', 'misterB', 'misterC', 'misterD']
# print(guest_list)
# print(f"\n invite guest {guest_list[0]} \n invite guest {guest_list[1]} \n invite guest {guest_list[2]} \n invite guest {guest_list[-1]}")

# cars = ['bmw', 'audi', 'toyota', 'subaru']
# print(cars)
# cars.sort()
# print(cars)
# cars.sort(reverse=True)
# print(cars)

                #With sorted() you can reverse to original list, but with 
                #reverse you cant, but you can just simply use reversed again
                #since it is displaying in a reversed order.
# cars = ['bmw', 'audi', 'toyota', 'subaru']
# print("Here is the original list:")
# print(cars)
# print("\nHere is the sorted list:")
# print(sorted(cars))
# print("\nHere is the original list again:")
# print(cars)

# cars = ['bmw', 'audi', 'toyota', 'subaru']
# print(cars)
# cars.reverse()
# print(cars)
# cars.reverse()
# print(cars)

# cars = ['bmw', 'audi', 'toyota', 'subaru']
# len(cars)

                                                        #Work with lists

# magicians = ['alice', 'david', 'carolina']
# for magician in magicians:
#     print(magician)

# magicians = ['alice', 'david', 'caroline']
# for magician in magicians:
#     print(f"{magician.title()}, that was a great trick")

# magicians = ['alice', 'david', 'caroline']
# for magician in magicians:
#     print(f"{magician.title()}, that was a great trick")
#     print(f"I cant wait to see your next trick, {magician.title()} \n")
# print("Thank you, everyone. That was a great magic show!")

# for value in range(1, 5):
#     print(value)

# for value in range(1, 6):
#     print(value)

# numbers = list(range(1, 6))
# print(numbers)

# even_numbers = list(range(2, 20, 2))
# print(even_numbers)

# squares = []
# for value in range(1, 20):
#     square = value ** 2
#     squares.append(square)
# print(squares)

# squares = []
# for value in range(1, 20):
#     squares.append(value**2)
# print(squares)

# digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
# min(digits)
# max(digits)
# sum(digits)

# squares = [value ** 2 for value in range (1, 11)]
# print(squares)

# for value in range (1, 20):
#     print(value)

# for value in range(1, 1000000):
#     print(value)        # CTRL + C to stop operation

# players = ['charles', 'martina', 'michael', 'florence', 'eli']
# print(players[0:3])
# print(players[1:4])
# print(players[:4])
# print(players[2:])
# print(players[-3:])

# players = ['charles', 'martina', 'michael', 'florence', 'eli']
# print("Here are the first three players on my team:")
# for player in players[:3]:
#     print(player.title())

# my_foods = ['pizza', 'falafel', 'carrot cake']
# friends_foods = my_foods

# print("My favorite foods are")
# print(my_foods)

# print("\nMy friends favorite foods are:")
# print(friends_foods)

# my_foods = ['pizza', 'falafel', 'carrot cake']
# friends_foods = my_foods[:]   # [:] this one slices the list by making copy of it

# my_foods.append('cannoli')
# friends_foods.append('ice cream')

# print("My favorite foods are")
# print(my_foods)

# print("\nMy friends favorite foods are")
# print(friends_foods)

# dimensions = (200, 50)    typles () ensure that its size does not change compared to []
# print(dimensions[0])
# print(dimensions[1])

# dimensions = (200, 50)   
# dimensions[0] = 250   #typles () will  not change dimensions and it will print error

# dimensions = (200, 50)
# for dimension in dimensions:
#     print(dimension)

# dimensions = (200, 50)
# print("original dimensions:")
# for dimension in dimensions:
#     print(dimension)

# dimensions = (400, 100)
# print("\nModified dimensions:")
# for dimension in dimensions:
#     print(dimension)

# cars = ['audi', 'bmw', 'subaru', 'toyota']
# for car in cars:
#     if car == 'bmw':
#         print(car.upper())
#     else:
#         print(car.title())

# car = 'bmw' # = sets a car as bmw
# car == 'bmw' # == check if car is bmw
# True

# car = 'audi'
# car == 'bmw'
# False 

# car = 'Audi'
# car == 'audi'
# False

# car = 'Audi'
# car.lover() == 'audi'
# True

# requested_topping = 'mushrooms'
# if requested_topping != 'anchovies':   # != inequality operator
#     print("Hold the anchovies!")

# answer = 17
# if answer != 42:
#     print("That is not correct answer. Please try again!")

# age = 19
# age < 21
# True
# age = 19
# age <= 19
# True
# age = 19
# age > 21
# False
# age = 19
# age >= 21
# False

# requested_toppings = ['mushrooms', 'onions', 'pinaple']
# 'mushrooms' in requested_toppings
# True
# 'pepperoni' in requested_toppings
# False

# banned_users = ['andrew', 'carolina', 'davide']
# user = 'marie'
# if user not in banned_users:
#     print(f"{user.title()}, you can post a response if you wish")

# if conditional_test:
#     do something

# age = 19
# if age >= 18:
#     print("You are old enought to vote!")

# age = 19
# if age >= 18:
#     print("you are old enought to vote!")
#     print("Have you registered to vote yet?")

# age = 17
# if age >= 18:
#     print("You are old enought to vote!")
#     print("Have you registered to vote yet?")
# else:
#     print("Sorry, you are too young to vote.")
#     print("Please register to vote as soon as you turn 18!")

# age = 12
# if age < 4:
#     print("Your admission cost is $0.")
# elif age < 18:
#     print("Your admission cost is $25.")
# else:
#     print("Your admission cost is $40.")

# age = 12
# if age < 4:
#     price = 0
# elif age < 18:
#     price = 25
# else:
#     price = 40

# print(f"Your admission cost is ${price}.")

# age = 12
# if age < 4:
#     price = 0
# elif age < 18:
#     price = 25
# elif age < 65:
#     price = 40
# else:
#     price = 20
# print(f"Your admission price is ${price}.")

# age = 12
# if age < 4:
#     price = 0
# elif age < 18:
#     price = 25
# elif age < 65:
#     price = 40
# elif age >= 65:
#     price = 20
# print(f"Your admission cost is ${price}.")

# requested_toppings = ['mushrooms', 'extra_cheese']
# if 'mushrooms' in requested_toppings:
#     print("Adding mushrooms.")
# if 'pepperoni' in requested_toppings:
#     print("adding pepperoni.")
# if 'extra_cheese' in requested_toppings:
#     print("Adding extra cheese.")
# print("\nFinished making your pizza!")

#if we want to run more than one block, we use if statements, if
#only one after test is passed, we use elif statements.

# alien_color = ['orange']
# if 'red' in alien_color:
#     print("congratulations you got 5 points for red alien")
# if 'yellow'in alien_color:
#     print("Congratulations you got 10 points")
# if 'orange' in alien_color:
#     print("congratulations you got a rare alien and 20 points")

