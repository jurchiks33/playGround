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

magicians = ['alice', 'david', 'caroline']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick")
    print(f"I cant wait to see your next trick, {magician.title()} \n")