import plotly.express as px
from die import Die

#Create  D6 and D10 dice.
die_1 = Die()
die_2 = Die(10)

#Make rolls and store results in a list.
results = []
for roll_num in range(50_000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

#Analyze results.
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
poss_results = range(2, max_result+1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

#Visualize results.
title = "Results of rolling D6 and D 10 50000 times"
labels = {'x', 'Result', 'y', 'Frequency of Result'}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)

#Chart customization.
fig.update_layout(xaxis_dtick=1)
fig.show()

print(results)