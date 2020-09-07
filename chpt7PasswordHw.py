# Checks to see if a password is strong
import re
#TO DO: Make a Regex to check password strength
passwordStrengthRegex=re.compile(r'[A-Z]+\d+\w+')

#Check the strength of the input
def strongPassword(password):
    passwordStrengthRegex.search(password)
    if len(password)>8 and passwordStrengthRegex==True:
        print('This is a valid password')
    else:
        print('Please enter an acceptable password')

#Ask for user input
print('Please enter a password')
password=input()
strongPassword(password)
