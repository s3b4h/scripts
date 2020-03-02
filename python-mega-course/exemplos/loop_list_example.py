monday_temperatures = [9.1, 8.8, 7.6]

#print(round(monday_temperatures[0]))
#print(round(monday_temperatures[1]))
#print(round(monday_temperatures[2]))


for temperature in monday_temperatures:
  print(round(temperature))
  print("Done")
  
  
for letter in 'hello':
  print(letter.title())
  
# Loop over colors =  [11, 34, 98, 43, 45, 54, 54]

colors = [11, 34, 98, 43, 45, 54, 54]
 
for color in colors:
  print(color)
  
#print only if the item is greter than 50

colors = [11, 34, 98, 43, 45, 54, 54]
 
for color in colors:
  if color > 50:
    print(color)

#print only if is an integer
colors = [11, 34.1, 98.2, 43, 45.1, 54, 54]

for item in colors:
  if isinstance(item, int):
    print(item)
    
#print only if is an integer and greater than 59

colors = [11, 34.1, 98.2, 43, 45.1, 54, 54]

for item in colors:
  if isinstance(item, int) and item > 50:
    print(item)