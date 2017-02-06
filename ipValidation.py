import re
""" Program takes IP as input and it will print whether the given IP
valid or not"""


def ip_validation(ip):
    pattern = re.compile(r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$")
    flag = 1

    if not pattern.match(ip):
        return 'Invalid IP'
    else:
        t = pattern.search(ip).groups()
        for elem in t:
            if int(elem) > 255:
                flag = 0
                break
        if flag is 1:
            return 'Valid IP'
        else:
            return 'Invalid IP'

if __name__ == '__main__':
    try:
        input = raw_input
    except NameError:
        pass
    ip_entered = input("Enter an IP\n")
    print(ip_validation(ip_entered))

