

# import csv
# with open("weather_data.csv") as data_file:
#   data = csv.reader(data_file)
#   temperatures = []
#   for row in data:
#       if(row[1]!='temp'):
#         temperatures.append(int(row[1]))
#
#   print(temperatures)

  # The upper code is for simple data files, but when we need to work with more
  # complex data and file we have to use Pandas.

import pandas

# data = pandas.read_csv("weather_data.csv")
# print(type(data["temp"]))
# print(data.to_dict())
#
# temp_list = data['temp'].to_list()
# print(temp_list)
# total = len(temp_list)
# avg_temperature = sum(temp_list,0) / total
# print(avg_temperature)


#read the API reference of Pandas and use methods

# data['temp'].mean()
# print(data['temp'].mean())
# print(data['temp'].max())
#
# # Get data in columns. 2 off the below do exactly the same.
#
# print(data['temp'])
# print(data.temp)

# Get data in rows not column

# monday = data[data.day == 'Monday']
# print(monday.condition)
# in_farenheit = (monday.temp[0 ])* 1.8 + 32
# print(f'In Farenheit : {in_farenheit}')
# print(data[data.temp == data.temp.max()])

# Create  dataframe from scratch

# data_dict = {
#     "students": ["Amy","James", "Angela"],
#     "scores":[76, 56, 65]
# }
#
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")
# print(data)

# Count the total squirell from the fur color in csv file

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20240204.csv")

gray_squrell_count = len(data[data["Primary Fur Color"] =="Gray"])
black_squrell_count = len(data[data["Primary Fur Color"] =="Black"])
red_squrell_count = len(data[data["Primary Fur Color"] =="Cinnamon"])

print(gray_squrell_count)
print(black_squrell_count)
print(red_squrell_count)

data_dict = {
    "Fur Color": ["Gray", "Black", "Cinnamon"],
    "Count": [gray_squrell_count, black_squrell_count,red_squrell_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")