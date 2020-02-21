student_grades = [9.1, 8.8, 7.5]

mysum = sum(student_grades)
length = len(student_grades)
mean = mysum / length

print(mean)


seconds = [1.2323442655, 1.4534345567, 1.023458894]
current = 1.10001399445
seconds.append(current)


seconds = [1.2323442655, 1.4534345567, 1.023458894, 1.10001399445]
seconds.remove(1.10001399445)
seconds.remove(1.023458894)
seconds.remove(1.4534345567)




monday_temperatures = [9.1, 8.8, 7.5]
monday_temperatures[1]
monday_temperatures.__getitem__(1)


serials = ["RH80810A", "AA899819A", "XYSA9099400", "OOP8988459", "EEO8904882", "KOC9889482"]
print(serials[2])

serials = ["RH80810A", "AA899819A", "XYSA9099400", "OOP8988459", "EEO8904882", "KOC9889482"]
print(serials[0], serials[2], serials[5])

#append the first item of weekend to workdays
workdays = ["Mon", "Tue", "Wed", "Thu", "Fri"]
weekend = ["Sat", "Sun"]
workdays.append(weekend[0])


monday_temperatures = [9.1, 8.8, 7.5, 6.6, 9.9]
len(monday_temperatures)
monday_temperatures[1:4]
monday_temperatures[0:2]
monday_temperatures[:2]
monday_temperatures[3:5]
monday_temperatures[3:]
monday_temperatures[-1]
monday_temperatures[-5]
monday_temperatures[-2:]
monday_temperatures[-4:-2]

my_string = 'hello'
my_string[:3]

monday_temperatures = ['hello', 1,2,3]
monday_temperatures[0][2]

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(letters[1:4])

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(letters[:3])

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(letters[-3:])