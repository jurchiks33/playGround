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

                #With sorted() you can reverse to original list, but with reverse you cant, but you can just simply use reversed again since it is displaying in a reversed order.
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