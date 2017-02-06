import re
""" Program takes Email ID as input and it will print whether the Mail ID
is a valid Mail ID name or not"""


def mail_validation(mail):
    pattern = re.compile(r"^([a-zA-Z0-9.-]+)\@(\w+\.(\w+))$")
    if pattern.match(mail):
        return 'Valid mailID'
    else:
        return 'Invalid mailID'

if __name__ == '__main__':
    try:
        input = raw_input
    except NameError:
        pass

    mail_entered = input("Enter a mailID\n")
    print(mail_validation(mail_entered))

