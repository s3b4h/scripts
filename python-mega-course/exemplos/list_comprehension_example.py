temps = [221, 234, 340, -9999 , 230]

#new_temps = []
#for temp in temps:
#  new_temps.append(temp / 10)
  
#print(new_temps)

new_temps = [temp / 10 for temp in temps]
print(new_temps)

new_temps = [ temp / 10 for temp in temps if temp != -9999]
print(new_temps)

#define a function takes a list containing numbers and strings an returns the lis containing only the numbers

def lista(lst):
  return [item for item in lst if not isinstance(item, str)]

print(lista([99,95, 'aaa', 96, 'asf']))

#define a function takes a list of numbers an returns the lis containing only numbers that are greater than 0

def lista01(lst):
  return [item for item in lst if item > 0]

print(lista01([-5, 3, -1, 101]))


# If Else inside list comprehension
temps = [221, 234, 340, -9999 , 230]

new_temps = [ temp / 10  if temp != -9999 else 0 for temp in temps]
print(new_temps)

#function that takes as parameter a list contains numbers an strings an returns the same list but with zerso instead of strings 
# lista = [99, 'asdf', 95, 94, 'fdsa']

def lista02(lst):
  return [i if isinstance(i, int) else 0 for i in lst ]

print(lista02([99, 'asdf', 95, 94, 'fdsa']))

#function that takes as parameter a list contains decimal numbers as strings and returns the sum of those numbers
#lst = ['1.2', '2.6', '3,3']

def sum_lst(lst):
  return sum([float(i) for i in lst])

print(sum_lst(['1.2', '2.6', '3.3']))