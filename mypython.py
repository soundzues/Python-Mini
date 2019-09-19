#Name: Aditya Kotahri
#Class: CS344
#Assignment: Python Py - Python Exploration
#use "python2 mypython.py" to compile 

import string
import random

#function to genrate string of 10 random char
def randStr(size=10):
    return ''.join(random.choice(string.ascii_lowercase) for i in xrange(size))

#write to the file
f = open("Goku", "w+")
f.write("%s\n" % randStr())
f.close()


#write to the file
f = open("Vageta", "w+")
f.write("%s\n" % randStr())
f.close()


#write to the file
f = open("Gohan", "w+")
f.write("%s\n" % randStr())
f.close()

#Read files
f = open("Goku", "r")
content = f.read()
#remove trailing newline char
print(content.strip())
f.close()

#Read files
f = open("Vageta", "r")
content = f.read()
#remove trailing newline char
print(content.strip())
f.close()

#Read files
f = open("Gohan", "r")
content = f.read()
#remove trailing newline char
print(content.strip())
f.close()

#genrating 2 random numbers between 1 and 42
a = random.randint(1,42)
b = random.randint(1,42)

#printing the two random number
print("%d" % a)
print("%d" % b)

#printing their product
product = a*b
print("%d" % product)


