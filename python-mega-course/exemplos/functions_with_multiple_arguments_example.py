def area(a,b):
    return a * b

print(area(4, 5))

def mean(*args):
     return sum(args)  / len(args)

print(mean(1,2, 4))

# define function that takes indefinite number of numbers as arguments and returns their average, 
# if i called foo(10, 20, 30 , 40) should return 25

def avg(*args):
    return sum(args) / len(args)

print(avg(10, 20, 30, 40))

# function that takes an indefinite number of strings as param an returns a list containingall the strings
# in uppercase and sorted alphabetically.
# ex? foo('snow', 'glacier', 'iceberg') should return ['GLACIER', 'ICEBERG', 'SNOW']

def upper_ex(*args):
    args = [ x.upper() for x in args]
    return sorted(args)

print(upper_ex('snow', 'glacier', 'iceberg'))


def mean(**kwargs):
    return kwargs

print (mean(a=1, b=2, c=3))


# exemplo

def find_sum(**kwargs):
    return sum(kwargs.values())

print(find_sum(a=1, b=2, c=6))

