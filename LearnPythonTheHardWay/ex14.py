from sys import argv

script, user_name, user_lastname = argv
prompt = '@ '

print "Hi %s %s, I'm the %s script." % (user_name, user_lastname, script)
print "I'd like to ask you a few questions."
print "Do you like me %s %s?" % (user_name, user_lastname)
likes = raw_input(prompt)

print "Where do you live %s %s?" % (user_name,user_lastname)
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
Alright, so you said %r about liking me.
You live in %r.  Not sure where that is.
And you have a %r computer.  Nice.
""" % (likes, lives, computer)
