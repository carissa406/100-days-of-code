# with open(r"Day 25\weather_data.csv") as file:
#     data = file.readlines()

# print(data)
#--------------------------------------------------
# import csv

# with open(r"Day 25\weather_data.csv") as file:
#     data = csv.reader(file)
#     temperatures = []
#     for row in data:
#         #print(row)
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)
#--------------------------------------------------
import pandas

#data = pandas.read_csv("Day 25\weather_data.csv")
# print(data)
# print(data["temp"])
# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].to_list()
# total = 0
# average = sum(temp_list)/len(temp_list)
# print(average)

# print(data["temp"].mean())

# print(data["temp"].max())

#get columns
# print(data["condition"])
# print(data.condition)

# #get row of data
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])
# #in the data data, where data.temp  == data.temp.max()

# #get data in row
# monday = data[data.day == "Monday"]
# print(monday.condition)
# monday_temp = monday.temp[0]
# print(monday_temp * (9/5) + 32)

#create df from scratch
# data_dict = {
#     "students":["Amy", "James", "Ella"],
#     "scores":[92, 22, 88]
# }
# data = pandas.DataFrame(data_dict)
# data.to_csv("Day 25/new_data.csv")

data = pandas.read_csv("Day 25/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray = len(data[data["Primary Fur Color"] == "Gray"])
red = len(data[data["Primary Fur Color"] == "Cinnamon"])
black = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count":[gray, red, black]
}

df = pandas.DataFrame(data_dict)
df.to_csv("Day 25/squirrel_count.csv")