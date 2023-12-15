from pathlib import Path
import csv

path = Path('/weather data/sitka_weather_07-2021_simple.csv')
lines = path.read_text().splitlines()