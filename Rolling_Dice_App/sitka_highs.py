from pathlib import Path
import csv

import matplotlib.pyplot as plt 

path = Path('weather data/sitka_weather_07-2021_simple.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

#Extract high temperatures.
highs = []
for row in reader:
    high = int(row[4])
    highs.append(high)

#Plot the high temperatures.
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(highs, color='red')



# print(highs)