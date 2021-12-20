# with open("./weather_data.csv") as weather_data:  # the normal way to get data from the csv file
#     print(weather_data.readlines())

# import csv
#
# with open("./weather_data.csv") as data_file: # we can get data importing csv package
#     data = csv.reader(data_file) # read the csv data
#     temperature = []
#     for row in data:
#         if row[1] != "temp":
#
#             temperature.append(int(row[1]))
#     print(temperature)

import pandas # import the panda library[external library]

data = pandas.read_csv("./weather_data.csv") # read the csv file

print(data) # print the file data
print(data["temp"]) # print the temp Column

data_dict = data.to_dict()
print(data_dict) # print  data as dictionary

temp_list = data["temp"].to_list() # add data to a list

print(sum(temp_list) / len(temp_list)) # normal way to get average of the temp

print(data["temp"].mean()) # get the average using pandas library

print(data["temp"].max()) # get the maximum value

print(data["condition"]) # print the condition field
print(data.condition) # print the condition field

print(data[data.day == "Monday"]) # print the monday row
print(data[data.temp == data.temp.max()]) # gat the monday row data
monday = data[data.day == "Monday"] # gat the monday row data
monday_temp = int(monday.temp) # get the monday temp

monday_temp_F = monday_temp * 9/5 + 32 # convert into F
print(monday_temp_F)

data_dic = {
    "Students" : ["Tony", "Bruce", "Sam"],
    "Score" : [65, 89, 45]
}

data_n = pandas.DataFrame(data_dic) # print data as a table
data_n.to_csv("new_data.csv")  # add the data to csv file call new_data.csv

