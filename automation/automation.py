import re
import shutil

#  Clean up the Phone numbers so they all match the same format
# Format: ###-###-####
# Any number w/o area code must be given "206" area code
# Quick Reference:

# \d{int} = \d looks for numbers, {int} tells it to look for a specific number of numbers that are concatinated inline(i.e if \d{4} it will find 1234 but not 1 2 3 4(Notice the spacing.)) 

#  Don't forget the values in the middle of phone numbers, both hyphens and periods (- and .)


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

#  Find all phone numbers in the given document

def phone_finder():


#  Validate the phone numbers against existing documents

# Store phone numbers in a new file


# Find all email addresses in given document


# Validate the email addresses against existing documents


# Store Emails in a new file


