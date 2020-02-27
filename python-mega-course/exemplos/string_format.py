#python 2 and python3
user_input = input("Enter your name: ")
message = "Hello %s!" % user_input
print(message)

#python 3.6
user_input = input("Enter your name: ")
message = f"Hello {user_input}!!"
print(message)

name = input("Enter your name: ")
surname = input("Enter your surname: ")

#message = "Hello %s  %s!" %(name, surname)
message = f"Hello {name} {surname}."
print(message)

#############

def hello(name):
  return "Hi %s" % name


def hello_upper(name):
  return "Hi %s" % name.title()