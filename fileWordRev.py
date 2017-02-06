""" Program takes word as input and it will print the number of occurrence
    of the word inside the file"""


def word_count(input_file):
    file_read = open(input_file, "r")
    file_read_new = open('new_word_reversed_file.txt', 'w')
    word_list = []
    for line in file_read:
        for word in line.split(" "):
            word_list.append(word)
    # print word_list
    for i in reversed(word_list):
        file_read_new.write(i + ' ')
    file_read.close()
    file_read_new.close()

if __name__ == '__main__':
    file_name = raw_input('Enter the file name\n')
    word_count(file_name)

