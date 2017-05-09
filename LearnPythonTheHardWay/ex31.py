print "You enter a dark room with three doors.  Do you go through door #1, door #2 or door #3?"

door = raw_input("> ")

if door == "1":
    print "There's a giant bear here eating a cheese cake.  What do you do?"
    print "1. Take the cake."
    print "2. Scream at the bear."

    bear = raw_input("> ")

    if bear == "1":
        print "The bear eats your face off.  Good job!"
    elif bear == "2":
        print "The bear eats your legs off.  Good job!"
    else:
        print "Well, doing %s is probably better.  Bear runs away." % bear

elif door == "2":
    print "You stare into the endless abyss at Cthulhu's retina."
    print "1. Blueberries."
    print "2. Yellow jacket clothespins."
    print "3. Understanding revolvers yelling melodies."

    insanity = raw_input("> ")

    if insanity == "1" or insanity == "2":
        print "Your body survives powered by a mind of jello.  Good job!"
    else:
        print "The insanity rots your eyes into a pool of muck.  Good job!"

elif door == "3":
    print "You are standing in front of a man who asks you: Who is the greatest basketball player of all time?"
    print "1. Michael Jordan"
    print "2. Lebron James"
    print "3. Kobe Bryant"

    player = raw_input("> ")

    if player == "1":
        print "You must be old and haven't watched the true GOAT play. You die."
    elif player =="2":
        print "You are correct. You live."
    elif player =="3":
        print "You must like missing shots, so you missed the correct answer. You die."
else:
    print "You stumble around and fall on a knife and die.  Good job!"
