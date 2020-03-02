monday_temperature = {"Marry": 9.1, "Sim": 8.8, "John": 7.5}

for item in monday_temperature.items():
  print(item)


for item in monday_temperature.keys():
  print(item)

for item in monday_temperature.values():
  print(item)


phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}
 
for pair in phone_numbers.items():
    print("{} has as phone number {}".format(pair[0], pair[1]))
    
    
phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}

for item in phone_numbers.items():
  print("%s : %s" %(item[0], item[1]))
  
for key, value in phone_numbers.items():
  print("%s : %s" %(key, value))
  
  
phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}

for value in phone_numbers.values():
  print('00'+value[1:])
  
phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}

for value in phone_numbers.values():
    print(value.replace("+", "00"))
    

for i in [1,2,3]:
  print(i)