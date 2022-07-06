##############################################
# # Update Values in Dictionaries and Lists ##
##############################################

# Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
x = [[5, 2, 3], [10, 8, 9]]
# nested list outer i = x[0, 1]
# inner loop  x[0][j] ==> [5, 2, 3]
# inner loop  x[1][j] ==> [10, 8, 9]

x[1][0] = 15
print(x)
print('\n')


# Change the last_name of the first student from 'Jordan' to 'Bryant'
students = [
    {'first_name':  'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'}
]
# list of dictionaries
# target 'Jordan' ==> students[0]['last_name']

students[0]['last_name'] = 'Bryant'
print(students)
print('\n')


# In the sports_directory, change 'Messi' to 'Andres'
sports_directory = {
    'basketball': ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer': ['Messi', 'Ronaldo', 'Rooney']
}
sports_directory['soccer'][0] = 'Andres'
print(sports_directory)
print('\n')


z = [{'x': 10, 'y': 20}]
# Change the value 20 in z to 30
z[0]['y'] = 30
print(z)
print('\n')

#
#
#
#
#
###########################################
# Iterate Through a List of Dictionaries ##
###########################################
students = [
    {'first_name':  'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'}
]


def iterateDictionary(some_list):
    for person in range(len(some_list)):
        fName = some_list[person]['first_name']
        lName = some_list[person]['last_name']
        print('first_name -' + fName + ', last_name -' + lName)
        print('\n')


# iterateDictionary(students)
# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel


#
#
#
#
#
#############################################
# # Get Values from a List of Dictionaries ##
#############################################

def iterateDictionary2(key_name, some_list):
    for i in range(len(some_list)):
        print(some_list[i][key_name])


iterateDictionary2('first_name', students)
iterateDictionary2('last_name', students)


#
#
#
#
#
####################################################
# # Iterate through a dictionary with List Values ##
####################################################

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}


def printInfo(some_dict):
    new_ = '\n'

    for i in some_dict:
        category = str(i).upper()
        numOfLoc = len(some_dict[i])
        cities = some_dict[i]
        print(f'{new_}{numOfLoc} {category}')

        for j in cities:
            print(f'{j}')
        # print(cities)


printInfo(dojo)

# output:
# 7 LOCATIONS
# San Jose
# Seattle
# Dallas
# Chicago
# Tulsa
# DC
# Burbank

# 8 INSTRUCTORS
# Michael
# Amy
# Eduardo
# Josh
# Graham
# Patrick
# Minh
# Devon

"""
Create a function printInfo(some_dict) that given a dictionary whose values are all lists,
prints the name of each key
along with the size of its list,
and then prints the associated values within each key's list.

"""
