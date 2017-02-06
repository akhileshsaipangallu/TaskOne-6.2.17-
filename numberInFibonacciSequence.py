""" Program takes a number as input and it will print
    whether it is a Fibonacci number or not"""


def series(last_but_one, last_one, series_range):
    while True:
        temp = last_one
        last_one += last_but_one
        last_but_one = temp
        if last_one <= series_range:
            fibonacci_list.append(last_one)
        else:
            break


def check_series(last_but_one, last_one, series_range):
    series(last_but_one, last_one, series_range)
    if series_range in fibonacci_list:
        return 'Entered number is in Fibonacci Sequence'
    else:
        return 'Entered number is not in Fibonacci Sequence'

if __name__ == '__main__':
    input_number = input("Enter a number to check if its a Fibonacci number\n")
    fibonacci_list = [0, 1, 1]
    print(check_series(fibonacci_list[-2], fibonacci_list[-1], input_number))

