"""WORKING WITH CSV AND PANDAS"""
# with open("weather_data.csv") as weather_data:
#     f = weather_data.readlines()
#     print(f)

# import csv
# with open("weather_data.csv") as weather_data:
#     data = csv.reader(weather_data)
#     temperature = []
#     for row in data:
#         new_temperature = row[1]
#         if new_temperature != 'temp':
#             temperature.append(int(new_temperature))
#
#     print(temperature)

import pandas

data_file = pandas.read_csv("weather_data.csv")
# print(data_file)
# print(data_file["temp"])

"""FINDING AVERAGE TEMP THE LONG METHOD"""
# temp_list = data_file["temp"].to_list()
# total_temp = 0
# for temp in temp_list:
#     total_temp += temp
#
# average_temp = total_temp/(len(temp_list))
# print(round(average_temp, 2))

"""FINDING AVERAGE TEMP USING IN BUILT METHODS"""
# print(data_file["temp"].mean())
# print(data_file["temp"].max())

"""PULLING A ROW WHERE TEMP IS MAX"""
# print(data_file[data_file["temp"] == data_file["temp"].max()])

"""CONVERTING MONDAYS TEMPERATURE TO FAHRENHEIT"""
monday = data_file[data_file["day"] == "Monday"]
monday_temp = monday["temp"][0]
monday_temp_F = (monday_temp * 1.8) + 32
print(monday_temp_F)