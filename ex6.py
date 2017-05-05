#x is a variable that takes the string in quotes
x = "There are %d types of people." % 10
#binary is a string variable also that takes the text binary
binary = "binary"
#do_not is a string variable also that takes the text don't
do_not = "don't"
#y is a string variable that takes some text wchich includes the previous two variables
y = "Those who know %s and those who %s." % (binary, do_not) #1 and 2place where string is in a string
# printing the x variable
print x
#printing the y variable
print y
#printing two string one after the other in new line
print "I said: %r." % x #3
print "I also said: '%s'." % y #4
#hilarious is a boolean type of variable that takes the value FALSE
hilarious = False
#initializing the variable joke_evaluation to some text with some variable
joke_evaluation = "Isn't that joke so funny?! %r"
#which is hilarious because of the variable name after the procent symbol
print joke_evaluation % hilarious
#defining 2 more string variables
w = "This is the left side of..."
e = "a string with a right side."
#concatening 2 strings together
print w + e
