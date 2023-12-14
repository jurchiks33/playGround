import plotly.express as px
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
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

#Visualize results.
title = "Results of rolling one D6 1000 times"
labels = {'x', 'Result', 'y', 'Frequency of Result'}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)
fig.show()

print(results)