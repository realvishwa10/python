# Squirrel Data analysis

import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

gray_color = data["Primary Fur Color"].value_counts()["Gray"]
cinnamon_color = data["Primary Fur Color"].value_counts()["Cinnamon"]
black_color = data["Primary Fur Color"].value_counts()["Black"]

print(gray_color)
print(cinnamon_color)
print(black_color)

squirrel_colors = {
    "Fur colours": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_color, cinnamon_color, black_color]
}

df = pandas.DataFrame(squirrel_colors)
df.to_csv("squirrel_analysis.csv")
