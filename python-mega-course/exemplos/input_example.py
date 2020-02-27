def weather_condition(param):
  if param > 7:
    return "warm"
  if param <= 7:
    return "cold"
  
  
user_input = float(input("Enter temperature: "))
print(weather_condition(user_input))
print(type(user_input))

###################

