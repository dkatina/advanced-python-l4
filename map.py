#Map is a higher order function that will do something to every item in a list, and produce the modified list

numbers = [1,2,3,4,5]

#Standard Approach
def double_nums(alist): #Function that takes in a list of nums doubles every num, adds num to a new list and returns the new_list
    output = [] #Where I will add all my doubled nums
    for num in alist:
        output.append(num*2)

    return output

doubled_nums = double_nums(numbers)


#The MAP Approach with Lambda
#Syntax

# map(function, alist)
# The function will process the items in the list one at a time
# Map then produces a Map Object that we can convert back into a list using list(map object)

new_doubled_nums = list(map(lambda num: num* 2, numbers))
print(new_doubled_nums)

#The MAP Approach with User Defined function

def double_num(num):
    return num * 2

newer_doubled_nums = list(map(double_num, numbers))

print(newer_doubled_nums)

# ================== Processing more complicated data ==============

users = [
    {'name': 'Petter Cottontail', 'email': 'PCOTTON@EMAIL.COM'},
    {'name': 'Tony stark', 'email': 'TSTARK@EMAIL.COM'},
    {'name': 'peter Quil', 'email': 'STARLORD@EMAIL.COM'}
]

#Create a function to normalize our users
#.title() case their name
#.lower() case their email
#Give username, lowercase name, names separated by _

def normalize_user(user): 
    return {
        'name': user['name'].title(), #Title case the user's name and restore it in a new dictionary
        'email': user['email'].lower(),
        'username': user['name'].lower().replace(' ', '_') #replace takes in 2 args (what we replace, what we replace it with)
    }

#User defined functions are better for large scale processing.
processed_users = list(map(normalize_user, users))
print(processed_users)

#Lambdas are good for simple processing
process_emails_only = list(map(lambda user: {"name": user['name'], 'email': user['email'].lower()} , users))

print(process_emails_only)

