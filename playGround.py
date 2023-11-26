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


# for numbers we are using int() instead of input()


# height = input("How tall are you, in cm?")
# height = int(height)
# if height >= 180:
#     print("\n You are a tall enought to ride!")
# else:
#     print("\nYou will be able to ride when you are a little older")


# number = input("Enter a number, and i will tell you if it is even or odd:")
# number = int(number)
# if number %2 == 0:
#     print(f"\nThe number {number} is even.")
# else:
#     print(f"\nThe number {number} is odd.")


# current_number = 1
# while current_number <= 5:
#     print(current_number)
#     current_number += 1


# prompt = "\nTell me something, and i will repeat it back to you:"
# prompt += "\Enter 'quit to end program."
# message = ""
# while message != 'quit':
#     message = input(prompt)
#     print(message)


# prompt = "\nTell me something, and i will repeat it back to you:"
# prompt += "\nEnter 'quit' to end the program."
# active = True
# while active:
#     message = input(prompt)
#     if message == 'quit':
#         activate = False
#     else:
#         print(message)


# prompt = "\nPlease enter the name of a city you have visited:"
# prompt += "\n(Enter 'quit' when you are finished.)"
# while True:
#     city = input(prompt)
#     if city == 'quit':
#         break
#     else:
#         print(f"I'd love to go to {city.title()}!")


# current_number = 0
# while current_number < 10:
#     current_number += 1
#     if current_number % 2 == 0:
#         continue
#     print(current_number)


# x = 1
# while x <= 5:
#     print(x)


# #Moving tiems from one list to another
# #Start with users that need to be ferified
# #and an empty list to hold confirmed users
# unconfirmed_users = ['alice', 'brian', 'candace']
# confirmed_users = []
# #Verify each user until there are no more unconfirmed users.
# #Move each verified user into the list of confirmed users.
# while unconfirmed_users:
#     current_user = unconfirmed_users.pop()
#     print(f"Verifying user: {current_user.title()}")
#     confirmed_users.append(current_user)
# #Display all confirmed users.
# print(f"\nThe following user have been confirmed:")
# for confirmed_user in confirmed_users:
#     print(confirmed_user.title())


# pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
# print(pets)
# while 'cat' in pets:
#     pets.remove('cat')
# print(pets)


# responses = {}
# #Set flag to indicate that pooling is active
# pooling_active = True
# while pooling_active:
#     #Prompt for the persons name and response
#     name = input("\nWhat is your name?")
#     response = input("Which mountain would you like to climb someday?")
#     #Store response in the dictionary.
#     responses[name] = response
#     #Find out if anyone else is going to take the pool.
#     repeat = input("Would you like to let another person respond? (yes/no)")
#     if repeat == 'no':
#         pooling_active = False
#  #Pooling is complete. Show the results.
#     print("\n---Poll Results---")
#     for name, response in responses.items():
#         print(f"{name} would you like to climb {response}.")


                        #---FUNCTIONS---


# def greet_user():
#     """"Display a simple greeting."""
#     print("Hello!")
# greet_user()


# def greet_user(username):
#     """"Display a simple greeting."""
#     print(f"Hello, {username.title()}!")
# greet_user('jesse')


# def describe_pet(animal_type, pet_name):
#     """Display information about a pet."""
#     print(f"\nI have a {animal_type}.")
#     print(f"My {animal_type}'s name is {pet_name.title()}.")
# describe_pet('hamster', 'harry')


# def describe_pet(animal_type, pet_name):
#     """Display information about a pet."""
#     print(f"\nI have a {animal_type}.")
#     print(f"My {animal_type}'s name is {pet_name.title()}.")
# describe_pet('hamster', 'harry')
# describe_pet('dog', 'willie')


# def describe_pet(animal_type, pet_name):
#     """Display information about a pet."""
#     print(f"\nI have a {animal_type}.")
#     print(f"My {animal_type}'s name is {pet_name.title()}.")
# describe_pet(animal_type='hamester', pet_name='harry')


# def describe_pet(pet_name, anymal_type='dog'):
#     """Display information about a pet."""
#     print(f"\nI have a {anymal_type}.")
#     print(f"My {anymal_type}'s name is {pet_name.title()}.")
# describe_pet(pet_name='willie')


# # A dog named Willie.
# describe_pet('willie')
# decribe_pet(pet_name='willie')
# #A hamster named Harry
# describe_pet('harry', 'hamster')
# describe_pet(pet_name='harry', animal_type='hamster')
# describe_pet(animal_type='hamster', pet_name='harry')
# #Each of these methods would work with example above


# def get_formatted_name(first_name, last_name):
#     """Return a full name, neatly formatted."""
#     full_name = f"{first_name} {last_name}"
#     return full_name.title()
# musician = get_formatted_name('jimi', 'hendrix')
# print(musician)


# def get_formatted_name(first_name, middle_name, last_name):
#     """Return a full name, neatly formatted."""
#     full_name = f"{first_name} {middle_name} {last_name}"
#     return full_name.title()
# musician = get_formatted_name('john', 'lee', 'hooker')
# print(musician)


# def get_formatted_name(first_name, last_name, middle_name=''):
#     """Return a full name, neatly formatted."""
#     if middle_name:
#         full_name = f"{first_name}, {middle_name}, {last_name}"
#     else:
#         full_name = f"{first_name}, {last_name}"
#     return full_name.title()
# musician = get_formatted_name('jimi', 'hendrix')
# print(musician)
# musician = get_formatted_name('john', 'hooker', 'lee')
# print(musician)


# def build_person(first_name, last_name):
#     """Return a dictionary of information about a person."""
#     person = {'first': first_name, 'last': last_name}
#     return person
# musician = build_person('jimi', 'hendrix')
# print(musician)


# def build_person(first_name, last_name, age=None):
#     """Return a dictionary of information about a person"""
#     person = {'first': first_name, 'last': last_name}
#     if age:
#         person['age'] = age
#     return person
# musician = build_person('jimi', 'hendrix', age=27)
# print(musician)


# def get_formatted_name(first_name, last_name):
#     """Return a full name, neatly formatted."""
#     full_name = f"{first_name}, {last_name}."
#     return full_name.title()

# """This is an infinite loop"""
# while True:
#     print("\nPlease tell me your name:")
#     f_name = input("First name:")
#     l_name = input("Last name:")

#     formatted_name = get_formatted_name(f_name, l_name)
#     print(f"\nHello, {formatted_name}!")


# def get_formatted_name(first_name, last_name):
#     """Return a full name, neatly formatted"""
#     full_name = f"{first_name} {last_name}"
#     return full_name.title()

# while True:
#     print("\nPlease enter your name:")
#     print("(enter 'q' at any time to quit)")

#     f_name = input("First name:")
#     if f_name == 'q':
#         break

#     l_name = input('Last name:')
#     if l_name == 'q':
#         break

#     formatted_name = get_formatted_name(f_name, l_name)
#     print(f"\nHello, {formatted_name}!")


# def greet_users(names):
#     """Print a simple greeting to each user in the list."""
#     for name in names:
#         msg = f"Hello, {name.title()}!"
#         print(msg)

# usernames = ['Hannah', 'ty', 'margot']
# greet_users(usernames)


# #Strat with some designs that need to be printed.
# unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
# completed_models = []

# #Simulate printing each design, until none are left.
# #Move eash design to completed_models after printing.
# while unprinted_designs:
#     current_design = unprinted_designs.pop()
#     print(f"Printing model: {current_design}")
#     completed_models.append(current_design)

# #Display all completed models.
# print("\nThe following models have been printed:")
# for completed_model in completed_models:
#     print(completed_model)


# def print_models(unprinted_designs, completed_models):
#     """Simulate printing each design, until none are left.
#     Move each design to completed_models after printing."""
#     while unprinted_designs:
#         current_design = unprinted_designs.pop()
#         print(f"Printing model: {current_design}")
#         completed_models.append(current_design)

# def show_completed_models(completed_models):
#     """Show all the models that were printed."""
#     print("\nfollowing models have been printed:")
#     for completed_model in completed_models:
#         print(completed_model)

# unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
# completed_models = []

# print_models(unprinted_designs, completed_models)
# show_completed_models(completed_models)


# def make_pizza(*toppings):
#     """Print the list of toppings that have been requested."""
#     print(toppings)

# make_pizza('pepperoni')
# make_pizza('mushrooms', 'green peppers', 'extra cheese')


# def make_pizza(*toppings):
#     """Summirize the pizza we are about to make."""
#     print("\nMaking a pizza with the following toppings:")
#     for topping in toppings:
#         print(f"- {topping}")

# make_pizza('pepperoni')
# make_pizza('mushrooms', 'green peppers', 'extra cheese')


# def make_pizza(size, *toppings):
#     """Summarize pizza we are about to make."""
#     print(f"\nMaking a {size}-inch pizza with the following toppings:")
#     for topping in toppings:
#         print(f"-{topping}")

# make_pizza(16, 'pepperoni')
# make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')


# def build_profile(first, last, **user_info):
#     """Build a dictionary containing everything we know about a user."""
#     user_info['first_name'] = first
#     user_info['last_name'] = last
#     return user_info

# user_profile = build_profile('albert', 'einstein',
#                              location='princeton',
#                              field='physics')
# print(user_profile)


# def make_pizza(size, *toppings):
#     """Summarize the pizza we are about to make."""
#     print(f"\nMaking a {size}-inch pizza with the following toppings:")
#     for topping in toppings:
#         print(f" - {topping}")

# #This one below should be on a seperate file so we can inport it from
# import pizza

# pizza.make_pizza(16, 'pepperoni')
# pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

#Each function in the module is available throught following syntax:
#module_name.function_name()


#General syntax for importing a function
#from module_name import function_name
#from module_name import function_0, function_1, function_2


# from module_name import function_name as fn
# # to give a module an Alias
# import module_name as mn
# #to import evry function in a module we use *
# from pizza import *


# def function_name(parameter_0, parameter_1='default value')

# function_name(value_0, parameter_1='value')

# def function_name(
#         parameter_0, parameter_1, parameter_2,
#         parameter_3, parameter_4, parameter_5):
#     function body......


                            #Clases


# class Dog:
#     """A simple attempt to model a dog."""

#     def __init__(self, name, age):
#         """Initialize name and age attributes."""
#         self.name = name
#         self.age = age
    
#     def sit(self):
#         """Initialize a dog sitting in response to a command"""
#         print(f"{self.name} is now sitting.")
    
#     def roll_over(self):
#         """Simulate rolling over in response to a command"""
#         print(f"{self.name} rolled over!")


# class Dog:
#     """A simple attempt to model a dog."""

#     def __init__(self, name, age):
#         """Initialize name and age attributes."""
#         self.name = name
#         self.age = age
    
#     def sit(self):
#         """Initialize a dog sitting in response to a command"""
#         print(f"{self.name} is now sitting.")
    
#     def roll_over(self):
#         """Simulate rolling over in response to a command"""
#         print(f"{self.name} rolled over!")

# my_dog = Dog('Willie', 6)
# print(f"My dog's name is {my_dog.name}.")
# print(f"My dog is {my_dog.age} years old")


# class Dog:
#     """A simple attempt to model a dog."""

#     def __init__(self, name, age):
#         """Initialize name and age attributes."""
#         self.name = name
#         self.age = age
    
#     def sit(self):
#         """Initialize a dog sitting in response to a command"""
#         print(f"{self.name} is now sitting.")
    
#     def roll_over(self):
#         """Simulate rolling over in response to a command"""
#         print(f"{self.name} rolled over!")

# my_dog = Dog('Willie', 6)
# my_dog.sit()
# my_dog.roll_over()


# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
    
#     def sit(self):
#         print(f"{self.name} is now sitting.")
    
#     def roll_over(self):
#         print(f"{self.name} rolled over!")

# my_dog = Dog('Willie', 6)
# your_dog = Dog('Lucy', 3)

# print(f"My dig's name is {my_dog.name}.")
# print(f"My dog is {my_dog.age} years old.")
# my_dog.sit()

# print(f"Your dog's name is {your_dog.name}.")
# print(f"Your dog is {your_dog.age} years old.")
# your_dog.roll_over()


# class Car:
#     """A simple attempt to represent a car."""
#     def __init__(self, make, model, year):
#         """Initialize attributes to describe a car."""
#         self.make = make
#         self.model = model
#         self.year = year
    
#     def get_descriptive_name(self):
#         """Return a neatly formatted descriptive name."""
#         long_name = f"{self.year} {self.make} {self.model}"
#         return long_name.title()
    
# my_new_car = Car('audi', 'a4', 2024)
# print(my_new_car.get_descriptive_name())


# class Car:
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0
    
#     def get_descriptive_name(self):
#         long_name = f"{self.year} {self.make} {self.model}"
#         return long_name.title()
    
#     def read_odometer(self):
#         """Print a statement showing the cars mileage."""
#         print(f"This car has {self.odometer_reading} miles on it")

# my_new_car = Car('audi', 'a4', '2024')
# print(my_new_car.get_descriptive_name())
# my_new_car.read_odometer()  


# class Car:
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0
    
#     def get_descriptive_name(self):
#         long_name = f"{self.year} {self.make} {self.model}"
#         return long_name.title()
    
#     def read_odometer(self):
#         print(f"This car has {self.odometer_reading} miles on it")

# my_new_car = Car('audi', 'a4', 2024)
# print(my_new_car.get_descriptive_name())

# my_new_car.odometer_reading = 23
# my_new_car.read_odometer()



# class Car:
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self. year = year
#         self.odometer_reading = 0
    
#     def get_descriptive_name(self):
#         long_name = f"{self.year} {self.make} {self.model}"
#         return long_name.title()
    
#     def read_odometer(self):
#         print(f"This car has {self.odometer_reading} miles on it")
    
#     def update_odometer(self, mileage):
#         """Set the odometer reading to the given value."""
#         self.odometer_reading = mileage

# my_new_car = Car('audi', 'a4', 2024)
# print(my_new_car.get_descriptive_name())

# my_new_car.update_odometer(23)
# my_new_car.read_odometer()


# class Car:
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self. year = year
#         self.odometer_reading = 30
    
#     def get_descriptive_name(self):
#         long_name = f"{self.year} {self.make} {self.model}"
#         return long_name.title()
    
#     def read_odometer(self):
#         print(f"This car has {self.odometer_reading} miles on it")
    
#     def update_odometer(self, mileage):
#         """Set the odometer reading to the given value.
#         Reject the change if it attempts to roll the odometer back"""
#         if mileage >= self.odometer_reading:
#             self.odometer_reading = mileage
#         else:
#             print("You cant roll back an odometer.")

# my_new_car = Car('audi', 'a4', 2024)
# print(my_new_car.get_descriptive_name())

# my_new_car.update_odometer(25)
# my_new_car.read_odometer()


# class Car:
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self. year = year
#         self.odometer_reading = 0
    
#     def get_descriptive_name(self):
#         long_name = f"{self.year} {self.make} {self.model}"
#         return long_name.title()
    
#     def read_odometer(self):
#         print(f"This car has {self.odometer_reading} miles on it")
    
#     def update_odometer(self, mileage):
#         """Set the odometer reading to the given value."""
#         self.odometer_reading = mileage

#     def increment_odometer(self, miles):
#         """Add the given amount to the odometer reading."""
#         self.odometer_reading += miles

# my_used_car = Car('subaru', 'outback', 2019)
# print(my_used_car.get_descriptive_name())

# my_used_car.update_odometer(23_500)
# my_used_car.read_odometer()

# my_used_car.increment_odometer(100)
# my_used_car.read_odometer()


# class Car:
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self. year = year
#         self.odometer_reading = 0
    
#     def get_descriptive_name(self):
#         long_name = f"{self.year} {self.make} {self.model}"
#         return long_name.title()
    
#     def read_odometer(self):
#         print(f"This car has {self.odometer_reading} miles on it")
    
#     def update_odometer(self, mileage):
#         """Set the odometer reading to the given value."""
#         self.odometer_reading = mileage

#     def increment_odometer(self, miles):
#         """Add the given amount to the odometer reading."""
#         self.odometer_reading += miles

# class ElectricCar(Car):
#     """Represents aspect of a car, specific to electric vehicles."""
#     def __init__(self, make, model, year):
#         """Initialize attributes of the parent class."""
#         super().__init__(make, model, year)

# my_leaf = ElectricCar('nissan', 'model', 2024)
# print(my_leaf.get_descriptive_name())


# class Car:
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self. year = year
#         self.odometer_reading = 0
    
#     def get_descriptive_name(self):
#         long_name = f"{self.year} {self.make} {self.model}"
#         return long_name.title()
    
#     def read_odometer(self):
#         print(f"This car has {self.odometer_reading} miles on it")
    
#     def update_odometer(self, mileage):
#         """Set the odometer reading to the given value."""
#         self.odometer_reading = mileage

#     def increment_odometer(self, miles):
#         """Add the given amount to the odometer reading."""
#         self.odometer_reading += miles

# class ElectricCar(Car):
#     """Represents aspect of a car, specific to electric vehicles."""
#     def __init__(self, make, model, year):
#         """Initialize attributes of the parent class.
#         Then initialize attributes specific to an electric car."""
#         super().__init__(make, model, year)
#         self.battery_size = 40
    
#     def describe_battery(self):
#         """Print a statement describing the battery size."""
#         print(f"This car has a {self.battery_size}-kwh battery.")

# my_leaf = ElectricCar('nissan', 'model', 2024)
# print(my_leaf.get_descriptive_name())
# my_leaf.describe_battery()


# class ElectricCar(Car):
#     """Represents aspect of a car, specific to electric vehicles."""
#     def __init__(self, make, model, year):
#         """Initialize attributes of the parent class.
#         Then initialize attributes specific to an electric car."""
#         super().__init__(make, model, year)
#         self.battery_size = 40
    
#     def describe_battery(self):
#         """Print a statement describing the battery size."""
#         print(f"This car has a {self.battery_size}-kwh battery.")
    
#     def fill_gass_tank(self):
#         """Electric cars dont have gas tanks."""
#         print("This car doesnt have a gass tank")


# class Car:
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self. year = year
#         self.odometer_reading = 0
    
#     def get_descriptive_name(self):
#         long_name = f"{self.year} {self.make} {self.model}"
#         return long_name.title()
    
#     def read_odometer(self):
#         print(f"This car has {self.odometer_reading} miles on it")
    
#     def update_odometer(self, mileage):
#         """Set the odometer reading to the given value."""
#         self.odometer_reading = mileage

#     def increment_odometer(self, miles):
#         """Add the given amount to the odometer reading."""
#         self.odometer_reading += miles

# class Battery:
#     """A simple attempt to model a battery for an electric car."""

#     def __init__(self, battery_size=40):
#         """Initialize the batterys attributes."""
#         self.battery_size = battery_size
    
#     def describe_battery(self):
#         """Print a statement describing the battery size."""
#         print(f"This car has a {self.battery_size}-kwh battery")

# class ElectricCar(Car):
#     """Represents aspect of a car, specific to electric vehicles."""
#     def __init__(self, make, model, year):
#         """Initialize attributes of the parent class.
#         Then initialize attributes specific to an electric car."""
#         super().__init__(make, model, year)
#         self.battery  = Battery()
    
#     def describe_battery(self):
#         """Print a statement describing the battery size."""
#         print(f"This car has a {self.battery_size}-kwh battery.")

# my_leaf = ElectricCar('nissan', 'model', 2024)
# print(my_leaf.get_descriptive_name())
# my_leaf.battery.describe_battery()


# class Car:
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self. year = year
#         self.odometer_reading = 0
    
#     def get_descriptive_name(self):
#         long_name = f"{self.year} {self.make} {self.model}"
#         return long_name.title()
    
#     def read_odometer(self):
#         print(f"This car has {self.odometer_reading} miles on it")
    
#     def update_odometer(self, mileage):
#         """Set the odometer reading to the given value."""
#         self.odometer_reading = mileage

#     def increment_odometer(self, miles):
#         """Add the given amount to the odometer reading."""
#         self.odometer_reading += miles

# class Battery:
#     """A simple attempt to model a battery for an electric car."""

#     def __init__(self, battery_size=65):
#         """Initialize the batterys attributes."""
#         self.battery_size = battery_size
    
#     def describe_battery(self):
#         """Print a statement describing the battery size."""
#         print(f"This car has a {self.battery_size}-kwh battery")
    
#     def get_range(self):
#         """Print a statement about the range this battery provides."""
#         if self.battery_size == 40:
#             range = 150
#         elif self.battery_size == 65:
#             range = 225

#             print(f"This car can go about {range} miles on a full charge/")

# class ElectricCar(Car):
#     """Represents aspect of a car, specific to electric vehicles."""
#     def __init__(self, make, model, year):
#         """Initialize attributes of the parent class.
#         Then initialize attributes specific to an electric car."""
#         super().__init__(make, model, year)
#         self.battery  = Battery()
    
#     def describe_battery(self):
#         """Print a statement describing the battery size."""
#         print(f"This car has a {self.battery_size}-kwh battery.")

# my_leaf = ElectricCar('nissan', 'model', 2024)
# print(my_leaf.get_descriptive_name())
# my_leaf.battery.describe_battery()
# my_leaf.battery.get_range()


"""A class that can be used to represent a car"""
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    
    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()