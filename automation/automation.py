import re
import shutil

#  Clean up the Phone numbers so they all match the same format
# Format: ###-###-####
# Any number w/o area code must be given "206" area code

def normalize_phone_numbers(phone_number):
    # Remove Open Parenthesis
    digits = phone_number.replace("(", "")
    # Replace closing parenthesis with a hyphen
    digits = digits.replace(")", "-")
    # Replace period sepatators with hyphens
    digits = digits.replace(".", "-")

    # If the refactored phone number is missing an area code 
    # Add the string "206" to the beginning
    if len(digits) == 8:
        digits = "206-" + digits


##############################################################
##############################################################

#  Find all phone numbers in the given document

def contact_finder():

#  Open the "potential contacts" file, use 'with' so it will open and close the document
    with open('assets/potential-contacts.txt') as file:
        # Read the open file and assign it to a variable
        text = file.read
    print('TEXT', text)
##############################################################
# File path will not stop throwing errors even though I have #
# checked the file path to ensure it's correct, using finder #
# bar to confirm regex effectiveness                         #
############################################################## 
    
    # Quick Reference:
    
    # \d{int} = \d looks for numbers, {int} tells it to look for a specific number of numbers that are concatinated inline(i.e if \d{4} it will find 1234 but not 1 2 3 4(Notice the spacing.)) 

    #  Don't forget the values in the middle of phone numbers, both hyphens and periods (- and .)

    # (?) - Question mark makes the parensthesis prior to it optional

    phone_number = re.compile(r'\d{3}[-.]\d{3}[-.]\d{4}(x\d*)?')

    print(phone_number)
    
    number_list = []

    # Use .extend() method to add phone numbers to the end of empty list

    # Find web reference used for .extend()
    number_list.extend(re.findall(phone_number, text))

    print(number_list)



def contact_validation():
#  Validate the phone numbers against existing documents
    with open('../assets/existing-contacts.txt') as file:
        text = file.read


# Store phone numbers in a new file


# Find all email addresses in given document


# Validate the email addresses against existing documents


# Store Emails in a new file


# if __name__ == "__main__":

#     print(contact_finder())
