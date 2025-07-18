numbers = [1,2,3,4,5,6,7,8,9,0]

#DOUBLE Only Evens
#Takes in a list of number and doubles and returns only the even ones
def double_only_evens(nums):
    output = []
    for num in nums:
        if num % 2 ==0: #Check if even
            output.append(num * 2) #add the doubled num to output

    return output

print(double_only_evens(numbers))

#Combining Map and Filter

doubled_evens =  list(map(lambda num: num * 2 ,filter(lambda num: num % 2 == 0, numbers)))
print(doubled_evens)



#==================== List Comprehension (inline for loop that creates a list) ================
                            
doubled_evens_comprehension = [num * 2 for num in numbers if num % 2 == 0]
print(doubled_evens_comprehension)

#just filtering (Only Evens)
evens = [num for num in numbers if num % 2 == 0]
print(evens)

#just processing (Doubling)
doubles = [num*2 for num in numbers]
print(doubles)
# Syntax

# [ expression for item in list condition ]

#==================== Real World Data Processing with  comprehensions

employees = [
    {'name': 'Alice Smith', 'department': 'Engineering', 'salary': 85000},
    {'name': 'John Johnson', 'department': 'Sales', 'salary': 100000},
    {'name': 'James Jameson', 'department': 'Engineering', 'salary': 80000},
    {'name': 'Bro Broadie', 'department': 'Sales', 'salary': 20000},
    {'name': 'Teddy Bear', 'department': 'Human Resource', 'salary': 40000}
]

#Just released a new phone shout out to the engineers, our engineers deserve a raise

engineer_raise = [{'name': employee['name'], 'department': 'Engineering', 'salary': employee['salary'] * 1.1} for employee in employees if employee['department'] == 'Engineering']
print(engineer_raise)


#Show our high earning ales people
high_earners = [employee for employee in employees if employee['salary'] > 50000 and employee['department'] == 'Sales']
print(high_earners)


#Efficiencies 

# List Comprhension
# User Defined functions
# Map and Filter