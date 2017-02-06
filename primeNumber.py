""" Program takes a number as input and it will print whether
    its a prime number or not"""


def prime_checking(n):
    flag = 1
    if n is 0 or n is 1:
        flag = 0
    else:
        for i in range(2, (n / 2) + 1):
            if n % i is 0:
                flag = 0
                break
    if flag:
        return True
    else:
        return False

if __name__ == '__main__':
    num = input('Enter a number\n')
    var = prime_checking(num)
    if var:
        print("\n%d is a prime number" % (num,))
    else:
        print("\n%d is not a prime number" % (num,))

