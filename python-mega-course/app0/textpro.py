def sentence_maker(phrase):
  interrogatives = ("how", "what", "why")
  captalized = phrase.capitalize()
  if phrase.startswith(interrogatives):
    return "{}?".format(captalized)
  else:
    return "{}.".format(captalized)
  
#print(sentence_maker("how are you")
results = []

while True:
  user_input = input("Say something: ")
  if user_input == "\end":
    break
  else:
    results.append(sentence_maker(user_input))
    
print(" ".join(results))