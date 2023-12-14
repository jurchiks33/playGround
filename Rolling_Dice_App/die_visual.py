from die import Die

#Create D6.
die = Die()
#Make rolls and store results in a list.
results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)

#Analyze results.
frequencies = []
poss_results = range(1, die.num_sides+1)
for value in pos_results:
    frequency = results.count(value)
    frequencies.append(frequency)

print(results)