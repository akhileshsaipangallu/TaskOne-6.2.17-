import re
""" Program takes Phone Number as input and it will print whether the input
is a valid Phone Number or not"""


def phone_number_validation(phone_number):
    pattern = re.compile(r"^(\d{10})$")
    if pattern.match(phone_number):
        return 'Valid phone number'
    else:
        return 'Invalid phone number'

if __name__ == '__main__':
    try:
        input = raw_input
    except NameError:
        pass
    phone_number_entered = input("Enter a mobile phone number\n")
    print(phone_number_validation(phone_number_entered))

