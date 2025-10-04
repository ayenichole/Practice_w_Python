#experimenting with dictionaries in python
dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}
phone_numbers = {'boss': 5551234567, 'Suzy': 22657854310}
restaurants = {"McDonald's": 1, "Burger King": 2, "KFC":  "grander","Chicken Inn": 4}
polish_english = {"jablko":"apple", "oczywiscie":"ofcourse", "mishka":"teddy","dobrze":"good"}
empty_dictionary = {}

print(dictionary)
print(phone_numbers)
print(empty_dictionary)
print(restaurants)
print(polish_english)

print(dictionary["cat"])
#adding a new key-value pair to a dictionary
dictionary['swan'] = 'cygne'
print(dictionary)

#adding a new key using update method
dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}

dictionary.update({"duck": "canard"})
print(dictionary)

print(phone_numbers['Suzy'])

#removing a key from a dictionary
dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}

del dictionary['dog']
print(dictionary)

#to remove the last item in a dictionary
dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}

dictionary.popitem()
print(dictionary)    # outputs: {'cat': 'chat', 'dog': 'chien'}





#using dictionaries
dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}
words = ['cat', 'lion', 'horse']

for word in words:
    if word in dictionary:
        print(word, "->", dictionary[word])
    else:
        print(word, "is not in dictionary")

#using the keys method to iterate in a dictionary
dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}

for key in dictionary.keys():
    print(key, "->", dictionary[key])

#using the items method to iterate in a dictionary
dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}

for english, french in dictionary.items():
    print(english, "->", french)

for french in dictionary.values():
    print(french)

#for key in sorted(dictionary.keys()):
 