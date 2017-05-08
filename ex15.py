#imports the feature argv from the module sys
from sys import argv
#unpacks the argv and assigns names to the arguments
script, filename = argv
#opens the file
txt = open(filename)
#prints the name of the file
print "Here's your file %r : " %filename
#uses the function read to display the contents of the file
print txt.read()

print "Type the filename again: "
file_again=raw_input("> ")

txt_again=open(file_again)

print txt_again.read()
#closes the files
txt.close()
txt_again.close()
