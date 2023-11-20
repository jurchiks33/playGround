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

# requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
# for requested_topping in requested_toppings:
#     print(f"adding {requested_topping}.")

# print("\nFinished making your pizza!")

# requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
# for requested_topping in requested_toppings:
#     if requested_topping == 'green peppers':
#         print("Sorry, we are out of green peppers right now.")
#     else:
#         print(f"adding {requested_topping}.")
# print("\nFinished making your pizza.")

# requested_toppings = []
# if requested_toppings:
#     for requested_topping in requested_toppings:
#         print(f"adding {requested_topping}.")
#         print("\nFinishing making your pizza!")
# else:
#     print("Are you sure you want a plain pizza?")


# available_toppings = ['mushrooms', 'olives', 'green peppers',
#                       'pepperoni', 'pineapple', 'extra cheese']

# requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

# for requested_topping in requested_toppings:
#     if requested_topping in available_toppings:
#         print(f"adding {requested_topping}.")
#     else:
#         print(f"Sorry, we dont have {requested_topping}.")
# print("\nFinishing making your pizza!")


                #DICTIONARIES


# alien_0 = {'color': 'green', 'points': 5}

# print(alien_0['color'])
# print(alien_0['points'])


#in PYTHON dictionary is wrapped in {}


# alien_0 = {'color': 'green', 'points': 5}
# new_points = alien_0['points']
# print(f"You just earned {new_points} points!")


# alien_0 = {'color': 'green', 'points': 5}
# print(alien_0)
# alien_0['x_position'] = 0
# alien_0['y_position'] = 25
# print(alien_0)


# alien_0 = {}
# alien_0['color'] = 'green'
# alien_0['points'] = 5
# print(alien_0)


# alien_0 = {'color': 'green'}
# print(f"The alien is {alien_0['color']}.")
# alien_0['color'] = 'yellow'
# print(f"the alien is now {alien_0['color']}.")


# alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
# print(f"Original position {alien_0['x_position']}")
# #Move alien to the right
# if alien_0['speed'] == 'slow':
#     x_increment = 1
# elif alien_0['speed'] == 'medium':
#     x_increment = 2
# else:
#     x_increment = 3
# #The new increment is the old position + increment.
# alien_0['x_position'] = alien_0['x_position'] + x_increment
# print(f"New position: {alien_0['x_position']}")


# alien_0 = {'color': 'green', 'points': 5}
# print(alien_0)
# del alien_0['points']
# print(alien_0)


# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'C',
#     'edward': 'rust',
#     'phil': 'python',
# }
# language = favorite_languages['sarah'].title()
# print(f"sarah's favorite language is {language}.")


# alien_0 = {'color': 'green', 'speed': 'slow'}
# point_value = alien_0.get('points', 'No point value assigned.')
# print(point_value)


# user_0 = {
#     'username': 'efermi',
#     'first': 'enrico',
#     'last': 'fermi',
# }
# for key, value in user_0.items():
#     print(f"\nKey: {key}")
#     print(f"Value: {value}")


# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'C',
#     'edward': 'rust',
#     'phila': 'python',
# }
# for name, language in favorite_languages.items():
#     print(f"{name.title()}'s favorite language is {language.title()}.")


# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'C',
#     'edward': 'rust',
#     'phil': 'python',
# }
# for name  in sorted(favorite_languages.keys()):
#     print(f"{name.title()}, thank you for taking the poll.")


# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'C',
#     'edward': 'rust',
#     'phil': 'python',
# }
# print("The following languages have been mentioned:")
# for language in favorite_languages.values():
#     print(language.title())


# alien_0 = {'color': 'green', 'points': 5}
# alien_1 = {'color': 'yellow', 'points': 10}
# alien_2 = {'color': 'red', 'points': '15'}
# aliens = [alien_0, alien_1, alien_2]
# for alien in aliens:
#     print(alien)


#         #Make an empty list for storing aliens
# aliens = []
#         #Make 30 green aliens
# for alien_number in range(30):
#     new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
#     aliens.append(new_alien)
#         #Show the first 5 aliens
# for alien in aliens[:5]:
#     print(alien)
# print('.....')
#         #Show how many aliens have been created
# print(f"Total number of aliens: {len(aliens)}")


# #         #Make an empty list for storing aliens
# aliens = []
# #         #Make 30 green aliens
# for alien_number in range(30):
#     new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
#     aliens.append(new_alien)
# for alien in aliens[:3]:
#     if alien['color'] == 'green':
#         alien['color'] = 'yellow'
#         alien['speed'] = 'medium'
#         alien['points'] = '10'
# for alien in aliens[:5]:
#     print(alien)
# print("....")


                #Make an empty list for storing aliens
# aliens = []
#                 #Make 30 green aliens
# for alien_number in range(30):
#     new_alien = {'color': 'yellow', 'points': 5, 'speed': 'slow'}
#     aliens.append(new_alien)
# for alien in aliens[:3]:
#     if alien['color'] == 'green':
#         alien['color'] = 'yellow'
#         alien['speed'] = 'medium'
#         alien['points'] = '10'
#     elif alien['color'] == 'yellow':
#         alien['color'] = 'red'
#         alien['speed'] = 'fast'
#         alien['points'] = '15'
# for alien in aliens[:5]:
#     print(alien)
# print("....")


# pizza = {
#     'crust': 'thick',
#     'toppings': ['mushrooms', 'extra cheese'],
# }
# print(f"you ordered a {pizza['crust']}-crust pizza "
#        "with the following toppings:")
# for topping in pizza['toppings']:
#     print(f"\t{topping}")


# favorite_languages = {
#     'jen': ['python', 'rust'],
#     'sarah': ['c'],
#     'edward': ['rust', 'go'],
#     'phil': ['python', 'haskall'],
# }
# for name, languages in favorite_languages.items():
#     print(f"\n{name.title()}'s favorite languages are:")
#     for language in languages:
#         print(f"\t{language.title()}")


# users = {
#     'aeinstein': {
#         'first': 'albert',
#         'last': 'einstein',
#         'location': 'princeton',
#     },
#     'mcurie': {
#         'first': 'marie',
#         'last': 'curie',
#         'location': 'paris',
#     }
# }
# for username, user_info in users.items():
#     print(f"\nUsername: {username}")
#     full_name = f"{user_info['first']} {user_info['last']}"
#     location = user_info['location']
# print(f"\tFull name: {full_name.title()}")
# print(f"\tLocation: {location.title()}")


# message = input("Tell me something, and i will repeat it back to you:")
# print(message)


# name = input("Please enter your name:")
# print(f"\nHello, {name}!")


# prompt = "If you share your name, we can personilize the message you see."
# prompt += "\nWhat is your first name?"
# name = input(prompt)
# print(f"\nHello, {name}")


