import sys
"""arg[0]: scriptName    arg[1]:fileName
    Program takes line number as input and prints the line from the file"""


def read_nth_line(line, file_name):
    file_read = open(file_name, 'r')
    content = file_read.readlines()
    return content[line - 1]

if __name__ == '__main__':
    line_number = input('Enter the line number\n')
    line = read_nth_line(line_number, sys.argv[1])
    print(line)

