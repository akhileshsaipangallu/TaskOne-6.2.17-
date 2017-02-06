import re
""" Program takes string as input and it will print whether the string
contains only the given special characters or not"""


def special_char_validation(special_char):
    pattern = re.compile(r"^([&()'\-']+)$")
    if pattern.match(special_char):
        return 'Valid special character/characters'
    else:
        return 'Invalid special character/characters'

if __name__ == '__main__':
    try:
        input = raw_input
    except NameError:
        pass
    char_input = input("Enter special character/characters(&, -, (, ),)\n")
    print(special_char_validation(char_input))

