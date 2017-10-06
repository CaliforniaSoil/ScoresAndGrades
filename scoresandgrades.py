from random import randint # import random integer library from the "random" module
print "Scores and Grades"
for x in range(10): # loop ten times
    x = randint(50, 100) # set x to a random integer from 60 to 100
        
    if x >= 90: # check if x is greater than or equal to 90
        print "Score: {}; Your grade is A".format(x) # print string with x interlope 
    if x >= 80 and x < 90: # check if x is less than 90 and greater than or equal to 80
        print "score: {}; Your grade is B".format(x) # print string with x interlope
    if x >= 70 and x < 80: # check if x is less than 80 and greater than or equal to 70
        print "Score: {}; Your grade is C".format(x) # print string with x interlope
    if x >= 60 and x < 69: # check if x is less than 69 and greater than or equal to 60
        print "Score: {}; Your grade is D".format(x) # print string with x interlope
    if x <= 59: # check if x is less than or equal to 59
        print "Score: {}; Your grade is F".format(x) # print string with x interlope
    
print "End of the program. Bye!"