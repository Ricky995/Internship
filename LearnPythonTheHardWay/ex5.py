name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'
height_cm=height*2.54
weight_kg=weight/2.2
print "Let's talk about %s." % name
print "He's %d inches tall which in centimeters is %d." % (height, height_cm)
print "He's %d pounds heavy or in kilograms %r." % (weight,weight_kg)
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
    age, height, weight, age + height + weight)
