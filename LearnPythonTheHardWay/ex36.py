from sys import exit

def smaug_room():
    print "This room is full with treasure."
    print "You need to get a special jewel underneath a dragon named Smaug"
    print "What do you do?"
    choice=raw_input("> ")
    if "flee" in choice:
        fail("You are a coward.")
    elif "taunt" in choice:
        fail("You exposed yourself to smaug and he burned you alive.")
    elif "stealth" or "take" in choice:
        print "Good job, you made it. Now you need a dwarf to set the jewel in place. Did you free one?"
        dwarf1=raw_input("> ")
        if dwarf1 == "yes":
            print "you got back in the dark room."
            print "The dwarf set the jewel and the room is light again. Congratulations."
            exit(0)
        elif dwarf1 == "no":
            print "You must free a dwarf from the prison."
            dwarf()
        else:
            fail("You should've written Yes or No")
    else:
        fail("Wrong.")
def dwarf():
    print "Welcome to the prison. You must take the key away from an orc"
    print "you find a meat on the ground. How do you use it to take the key?"
    choice=raw_input('> ')
    if "slide" or "throw" or "give" in choice:
        print "Great. Now you can get the key while the orc is busy."
        print "You freed a dwarf. Now he has to put the jewel to its place. Do you have the jewel?"
        jewel=raw_input("> ")
        if jewel == "yes":
            print "you got back in the dark room"
            print "The dwarf set the jewel and the room is light again. Congratulations."
            exit(0)
        elif jewel == "no":
            print "You must go and get it. Opening the second door..."
            smaug_room()
        else:
            fail("You should've written Yes or No")
    else:
        fail("The orc saw you and killed you.")

def fail(reason):
    print reason, " Game over"
    exit(0)

def start():
    print "You are in a dark room. You need light."
    print "There is a hole for a jewel on the ground but you can't reach it."
    print "There is a door to your left and right, which one do you take?"
    choice = raw_input("> ")
    if choice =="left":
        smaug_room()
    elif choice=="right":
        dwarf()
    else:
        fail("You can't even choose a door.")

start()
