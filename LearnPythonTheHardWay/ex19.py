#defining a function called cheese_and_crackers that takes two arguments
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man that's enough for a party!"
    print "Get a blanket.\n"


print "We can just give the function numbers directly:"
#calling the function with the numbers 45 and 24 as arguments
cheese_and_crackers(45, 24)


print "or, we can use variables from our script:"
amount_of_cheese = 20
amount_of_crackers = 54
#calling the functions with two variables as arguments
cheese_and_crackers(amount_of_cheese, amount_of_crackers)


print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)


print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

def new_function(fruit, weight):
    print "You have %d kilograms of %s" % (weight, fruit)

new_function("apples",34)
new_function(raw_input("enter fruit: "),int(raw_input("enter weight ")))
