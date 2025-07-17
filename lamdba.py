
#Basic funtion syntax
# def name_of_func(parameters):
#   #code block

def calculate_tax(price):
    #Calculate 7% sales tax
    tax = price * .07
    return tax

print(f"{calculate_tax(136):.2f}")
print(calculate_tax(31))

#Lambda Functions aka Anonymous Functions
#Syntax
# lambda parameters: expression whos value is returned

lambda price: price * .07 #Anonymous function because it has no name.

lambda_calc_tax = lambda price: price * .07

print(lambda_calc_tax(15))

#Key thing with lambda functions is that they are written in a single line.

#=============== SORTING KEYS with LAMBDA FUNCTIONS =============================

products = [
    {'name': 'laptop', 'price': 999.99},
    {'name': 'mouse', 'price': 64.99},
    {'name': 'keyboard', 'price': 119.99}
]

print("Sorting my products")
# print(sorted(products)) Unable to sort dictionaries by default

#create a sorting to target specific fields of individual pieces of data
#Syntax for a lambda sorting key
#lambda item: item['price']
#Total Syntax: sorted(list_to_sort, key = lambda x: 'function to target what we want to sort by')
print(sorted(products, key=lambda product: product['price'], reverse=True)) #Default order is Ascending, reverse = True switchs to descending

students = ['Nicole Cespedes', 'Ray Kofoed', 'Seb F']
#How would I split the names and look at the last name for each of the names in my list
print(sorted(students,)) 

name = 'Nicole Cespedes'
first_char_of_last = name.split()[1]
print(first_char_of_last)

print("Sorting by last name (Target the last name with sort key)")
print(sorted(students, key=lambda student: student.split()[1])) 