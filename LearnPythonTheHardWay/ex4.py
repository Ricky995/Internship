#number of cars
cars = 100
#number of seats in a cars
space_in_a_car = 4.0 #if it were just 4, python would see the variable as an integer type and it is not necessary to be 4.0
#number of drivers
drivers = 30
#number of passengers
passengers = 90
#cars that aren't driven because of shortage of drivers
cars_not_driven = cars - drivers
#cars that will be driven
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven
#The Car_pool_capacity error is there because there isn't a variable by that
#name defined, if it was carpool_capacity then no error would've appeared.

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."
