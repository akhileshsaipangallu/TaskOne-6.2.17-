import re
""" Program takes string as input and it will print whether the string
contains only numbers or not"""


def number_validation(number):
    pattern = re.compile(r"^(\d{1,})$")

    if pattern.match(number):
        return 'Valid number'
    else:
        return 'Invalid number'

if __name__ == '__main__':
    try:
        input = raw_input
    except NameError:
        pass

    number_entered = input("Enter a number\n")
    print(number_validation(number_entered))

