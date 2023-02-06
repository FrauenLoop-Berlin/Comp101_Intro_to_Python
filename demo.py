# run using the button in the right hand side corner
# use the terminal `python3 demo.py`

# define a variable, name
msg = 'Hello'
# print the content () on the terminal
print(msg)
my_name = 'Nathalie'
my_name = 'Anna'
# Print the value of a variable
print(my_name)
# string
print('Ivonita')
# Number: Integer 
my_age = 36
# or Float
temp = 2.2
# <class 'int'>
print(type(my_age))

## Calculate the year I was born:
my_birthyear = 2023 - 36

current_year = 2023
my_birthyear = current_year - my_age
print(my_birthyear)

## Data type string, integer, float, 

# boolean, 
mentor = True 
mentor = False 

# list, 
my_hobbies = [ 'running', 'coding', 'eating', 123, False, [1,2,3] ]

# dictionary (dict): key: value
my_pet = {
  'name': 'Susi',
  'animal': 'cat',
  'age': 2,
  'cute': True,
}

my_tweet = {
  'text': 'Hello',
  'date': '2023.01.23'
}

# conditions 
# age = input("what is your age?")

age = 0
# age = int(input("What is your age?"))
print(type(age))

# if age is lower than 18, print : no entry
# if older: print(welcome) 
# older then 65 : 50%
if age < 18:
  print("You are too young")
  print("No entry!")
elif age > 65:
  print("reduced entry, 50 off!")  
else:
  print("Welcome!")


password = "1234_password"

if password == "1234_password":
  print("Correct")
elif len(password) > 7:
  print('is long enough')   
elif len(password) < 7:
  print('too short')       
else:
  print("Not correct") 


print('conditional is done!')

#  Functions
  # guests = 2
  # bill = 20
  # tip = 10

ugly_variable = 'dont do it!'

def calculate_split_bill(bill, tip, guests):
  total_bill = bill + (bill * (tip/100))
  split_bill = total_bill /guests
  print(ugly_variable)
  # print(split_bill) to check, but does nothing!
  # output
  return split_bill

# call function with values, storing the return value in a new variable
result_one = calculate_split_bill(20,10,2)
print(result_one)

input_bill = int(input("What is the bill?"))
input_tip = int(input("What is the tip?"))
input_guests = int(input("how many guests?"))

result_two = calculate_split_bill(input_bill, input_tip, input_guests)
print(result_two)


def sum(x):
 res = 0
 for i in range(x):
  # [0,1,2,3]
   res+=i
 return res

# longer see result:
result_sum = sum(4)
print(result_sum)
# shorter:
print(sum(4))