from die import Die

#Create D6.
die = Die()
#Make rolls and store results in a list.
results = []
for roll_num in range(100):
    result = die.roll()
    results.append(result)

print(results)