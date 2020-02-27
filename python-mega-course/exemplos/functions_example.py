def mean(mylist):
  the_mean = sum(mylist) / len(mylist)
  return the_mean

print(mean([12,4,5]))

#print(type(mean), type(sum))

#complete the lenghter function definition so that it retunrs the number of items for every input lst
def lengther(lst):
    items = len(lst)
    return items
  
#function that calculates the are of a square

def square(num):
  result = num * num
  return result

print(square(2))

def foo(a):
    return a * a
  
print(foo(10))


#function convert fuid ounces to mililiters, fluid onces = 29.57353

def ounces_mililiters(num):
  return num * 29.57353

print(ounces_mililiters(10))

#function without return returns None

