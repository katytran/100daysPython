# # with open("weather_data.csv", mode="r") as data:
# #     content = data.readlines()
# #     print(content)
#
# import csv
#
# # with open("weather_data.csv", mode="r") as data_file:
# #     data = csv.reader(data_file)
# #     #Skip headline csv
# #     next(data)
# #     print(data)
# #     temperature = []
# #     for row in data:
# #         print(row)
# #         temperature.append(int(row[1]))
# #     print(temperature)
#
import pandas
#
# data = pandas.read_csv("weather_data.csv")
# print(data)
#
# #Get column data
# print(data["temp"])
#
#
# max_temp = data["temp"].max()
# print(max_temp)
#
# #Get row data
#
# #Get row has Monday
# print(data[data.day == "Monday"])
# #Get row temp has highest temp
# print(data[data.temp == data["temp"].max()])
#
# #Create Dataframe
# data_dict = {
#     "student": ["EM", "BE", "CA"],
#     "scores": [10,200,400],
# }
#
# data = pandas.DataFrame(data_dict)
#
# #sava data frame to csv
# data.to_csv("csv_file.csv")

squirrel_data = pandas.read_csv("./2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

# print(squirrel_data)
data_fur = squirrel_data["Primary Fur Color"]
print(data_fur)


squirrel_gray = data_fur[data_fur == "Gray"]
squirrel_red = data_fur[data_fur == "Cinnamon"]
squirrel_black = data_fur[data_fur == "Black"]

# squirrel_gray = data[data["Primary Fur Color"] == "Gray"]
# squirrel_red = data[data["Primary Fur Color"] == "Cinnamon"]
# squirrel_black = data[data["Primary Fur Color"] == "Black"]

print(squirrel_gray)
print(squirrel_red)
print(squirrel_black)

data_frame_squirrel = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [squirrel_gray.count(), squirrel_red.count(), squirrel_black.count()]
}

cvs_squirrel = pandas.DataFrame(data_frame_squirrel)
cvs_squirrel.to_csv("./cvs_squirrel.cvs")
