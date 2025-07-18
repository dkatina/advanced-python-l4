#Filter is a higher order function that takes in a list,
#Evaluates the contents individually and creates a new list of items
#Based on who met a certain criteria/condition

numbers = [1,2,3,4,5,6,7,8,9,0]

#Standard Way

#Write a function that took in a list of numbers and returned only evens
def only_evens(nums):
    output = [] #This list I add to when an item passes my check
    for num in nums:
        if num % 2 == 0: #If I can divded this number by 2 and the remainder is 0
            output.append(num)
    return output

print(only_evens(numbers))


#Filter
#syntax:
# filter(function, list)
# function - evaluates a single item at a time returns T/F base on a condition
# IF True = item makes it to the output list
# If False = item gets filtered never to be seen again

#Filtering with lambda

evens = list(filter(lambda num: num % 2 == 0, numbers ))

print(evens)

#Filtering with a user defined function

def is_even(num):
    return num % 2 == 0

ud_evens = list(filter(is_even, numbers)) #don't need the () after my function call

#===================== Filter real data ===================

transactions = [
    {'id': 1, 'amount': 100.0, 'type': 'credit', 'valid': True},
    {'id': 2, 'amount': -50.0, 'type': 'credit', 'valid': False},
    {'id': 3, 'amount': 200.0, 'type': 'debit', 'valid': True},
    {'id': 4, 'amount': 0.0, 'type': 'debit', 'valid': False},
    {'id': 5, 'amount': 75.0, 'type': 'debit', 'valid': True},
]

#Filter by Valid transactions

valid_transactions = list(filter(lambda transaction: transaction['valid'], transactions))
print(valid_transactions)

debit_transactions = list(filter(lambda transaction: transaction['type'] == 'debit', transactions))
print(debit_transactions)

high_credit_transactions = list(filter(lambda transaction: transaction['amount'] >= 100 and transaction['type'] == 'credit', transactions))
print(high_credit_transactions)



