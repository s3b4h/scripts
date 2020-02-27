#************#
#Conditionals
#************#

def mean(value):
  if type(value) == dict:  
    the_mean = sum(value.values()) / len(value)
  else:
    the_mean = sum(value) / len(value)
  return the_mean

monday_temperatures = [8.8, 9.1, 9.9]
students_grades = {"Marry": 9.1, "Sim": 8.8, "John": 7.5}
print(mean(students_grades))
print(mean(monday_temperatures))


#isinstance#

def mean(value):
  if isinstance(value, dict):  
    the_mean = sum(value.values()) / len(value)
  else:
    the_mean = sum(value) / len(value)
  return the_mean

monday_temperatures = [8.8, 9.1, 9.9]
students_grades = {"Marry": 9.1, "Sim": 8.8, "John": 7.5}
print(mean(students_grades))
print(mean(monday_temperatures))

#examples    
if 3 > 1:
  print("Greater")
else:
  print("Not Greater")
  
  
3 > 1
type(3) == int
isinstance(3,int)

###############
# Defines a funcition that:
# 1 takes a string as parameter
# 2 returns false if the string contanis less than 8 characters
# 3 returns true if the string contains 8 or more characters

# if called funcaoint with foo("mypass") it would return false, if called with("mylongpassword") it would return True

###############

def passwd(password):
  if len(password)>= 8:
    return True
  else:
    return False

######################
# 1 takes a temperature parameter
# 2 returns warm if the temperature is greater than 7
# 3 returns cold if the temperature is equal or less than 7
#########################

def temperature(param):
  if param > 7:
    return "warm"
  if param <= 7:
    return "cold"
  
temperature(10)
temperature(5)


########################
x = 3
y = 1
if x > y:
  print("x is greater than y")
elif x == y:
  print("x is equal than y")
else:
  print("x is less than y")
  
#######################

#1 takes a temperature parameter
#2 returns Hot if the temperature is greater than 25
#3 returns Warm if the temperature is between 15 and 25, including 15 and 25
#4 returns Cold if the temperature is less than 15
########################3

def weather_condition(param):
  if param > 25:
    return "Hot"
  elif param >= 15 and param<= 25:
    return "Warm"
  else:
    param < 15
    return "Cold"
      
weather_condition(32)
weather_condition(18)
weather_condition(10)

