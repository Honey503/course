# Poem
print('''Twinkle, twinkle, little star
    How I wonder what you are
        Up above the world so high
        Like a diamond in the sky
Twinkle, twinkle, little star
    How I wonder what you are''')

# Python version
import sys
print(sys.version)

# Current date and time
from datetime import datetime
now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
print("date and time =", dt_string)

# reverse name and last name
f_name = input("Please enter your first name:\n")
l_name = input("Please enter your last name:\n")
full_name = f_name + ' ' + l_name
print(full_name[::-1])
# You requirements are not clear to me so I'm going to do it second time
print(l_name+' '+ f_name)

# Add user input
a = int(input("Enter first number:\n"))
b = int(input("Enter second number:\n"))
print(a+b)