i = 0
numbers = []

def lists(numbers,incr):
    i=0
    six=6
    for i in range(0,six):
        print "At the top i is %d" % i
        numbers.append(i)
        i+=incr
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i
print "The numbers: "
lists(numbers,1)
for num in numbers:
    print num
