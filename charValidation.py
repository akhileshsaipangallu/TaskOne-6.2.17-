import re
""" Program takes string as input and it will print whether the string
contains only characters or not"""


def char_validation(char):
    pattern = re.compile(r"^([a-zA-Z]+)$")
    if pattern.match(char):
        return 'Valid character/characters'
    else:
        return 'Invalid character/characters'

if __name__ == '__main__':
    try:
        input = raw_input
    except NameError:
        pass
    char_input = input("Enter character\n")
    print(char_validation(char_input))

