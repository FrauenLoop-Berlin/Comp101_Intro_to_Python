msg = "Hello World"
print(msg)
# integer
my_age = 36
# string
my_name = 'Nathalie'
print(my_age, my_name)
print("Hello, I am ", my_name , " and I am " , my_age ," years old.")
# Concatenation will give us an error because of the int here!
# print("Hello, I am " + my_name , " and I am " + my_age + " years old.")
# check type
print(type(my_name))

# booleans 

# dictionary dict
my_pet = {
  'name': 'Susi',
  'age': 2,
  'animal': 'cat',
  'cute': True 
}

print(my_pet['cute'])
print(my_pet.get('cute'))

# list: 

my_hobbies = ['running', 'baking', 'dancing']
my_pets = [ {
  'name': 'Susi',
  'age': 2,
  'animal': 'cat',
  'cute': True 
},  {
  'name': 'Doggo',
  'age': 5,
  'animal': 'dog',
  'cute': True 
},  {
  'name': 'Karl',
  'age': 0.1,
  'animal': 'fish',
  'cute': True 
}]

print(my_pets[1]['name'])