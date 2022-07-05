
########################################################
print('Basic - Print all integers from 0 to 150.\n')
#######################################################
start = 0
stop = 151
step = 1

for i in range(start, stop, step):
    print(i)


################################################
print('\n# Print all the multiples of 5 from 5 to 1,000')
################################################
start = 5
stop = 1001
step = 5
for i in range(start, stop, step):
    print(i)


#######################################################
print('\nCounting, the Dojo Way - Print integers 1 to 100.')
# If divisible by 5, print "Coding" instead.
# If divisible by 10, print "Coding Dojo".
#######################################################
start = 1
stop = 101
step = 1

for i in range(start, stop, step):
    if i % 10 == 0:
        print("Coding Dojo")
    elif i % 5 == 0:
        print("Coding")
    else:
        print(i)


#####################################################
print("\nWhoa. That Sucker's Huge - Add odd integers from 0 to 500,000")
# and print the final sum.
#####################################################
start = 0
stop = 500001
# stop = 50
step = 1

sum = 0

for i in range(start, stop, step):
    if i % 2 != 0:
        sum += i
        # print(i)
    # continue
print(sum)


#####################################################
print('\nCountdown by Fours\n')
# Print positive numbers starting at 2018,
# counting down by fours.
#####################################################
start = 2018
stop = 0
countDown = -4

for i in range(start, stop, countDown):
    if not(i < 0):
        print(i)


###################################################
print('\nFlexible Counter\n')
# - Set three variables: lowNum, highNum, mult.
# Starting at lowNum and going through highNum,
# print only the integers that are a multiple of mult.
# For example, if lowNum=2, highNum=9,
# and mult=3, the loop should print 3, 6, 9 (on successive lines)
#####################################################

lowNum = 0
highNum = 100
mult = 5

for i in range(lowNum, highNum, mult):
    if i % mult == 0:
        print(i)
    else:
        continue
