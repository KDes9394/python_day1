Exercise 1
# Use the following list - [1,11,14,5,8,9]
numbers = [1,11,14,5,8,9]
output = []

for number in numbers: 
    if number < 10:
        output.append(number)
    
print(output)




Exercise 2

l_1 = [1,2,3,4,5,6]
l_2 = [3,4,5,6,7,8,10]
l_3 = []

def full_list():
    x=0
    for x in range(len(l_2)):
        l_3=l_1+l_2
        x= x + 1
        l_3.sort()
    print(l_3)
    
full_list()

Exercise 3
first_name = ['John', 'Evan', 'Jordan', 'Max']
last_name = ['Smith', 'Smith', 'Williams', 'Bell']
full_names = []

def print_names():
    i = 0
    while i < len(first_name):
        full_name = (first_name[i] + " " + last_name[i])
        i = i + 1
        full_names.append(full_name)

    print(full_names)
print_names()