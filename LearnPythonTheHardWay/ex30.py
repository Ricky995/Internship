#initializing variable people with the value 20
people = 20
#initializing variable cars with value 35
cars = 35
#initializing variable trucks with value 15
trucks = 15
#if statement for checking if cars or trucks are greater in number than people
if cars > people or trucks > people:
    #if one of the statements is true, the line 10 will be printed.
    print "We should take the cars or the trucks."
#if none of the statements is true, it will jump to the elif statement to check if cars are less in number than people
elif cars < people:
    #if the statement is true then the line 14 will be printed
    print "We should not take the cars or the trucks."
#if the elif statement isn't true either, then the else statement will be executed and the line 17 will be printed.
else:
    print "We can't decide."
#same goes for every line from now on, only with different variables.

if trucks > cars:
    print "That's too many trucks."
elif trucks < cars:
    print "Maybe we could take the trucks."
else:
    print "We still can't decide."

if people > trucks and trucks < cars:
    print "Alright, let's just take the trucks."
else:
    print "Fine, let's stay home then."
