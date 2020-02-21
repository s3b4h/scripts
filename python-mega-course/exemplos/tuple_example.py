#tuples are imutables
monday_temperatures = (1, 4 ,5)
print(monday_temperatures)

monday_temperatures2 = [1 , 4 ,5]
print(monday_temperatures2)
monday_temperatures2.append(7)
print(monday_temperatures2)

color_codes = ((1,2,3), (4,5,6), (7,8,9))

day_temperatures = {"morning": (1.1,2.2, 3.3) , "noon": (4.4,5.5,6.6), "evening": (7.7,8.8,9.9)}
day_temperatures.keys()
day_temperatures.values()