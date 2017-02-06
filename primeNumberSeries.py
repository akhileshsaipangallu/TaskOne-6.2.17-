""" Program takes range as input and it will print Prime Number list
    based on the range"""


def prime_number_series(input_range):
    prime_number_list = [1]
    for count in range(2, input_range + 1):
        flag = 1
        for i in range(2, (count / 2) + 1):
            if count % i is 0:
                flag = 0
                break
        if flag is 1:
            prime_number_list.append(count)
    print prime_number_list

if __name__ == '__main__':
    series_range = input("Enter range for prime number series(>1)\n")
    prime_number_series(series_range)

