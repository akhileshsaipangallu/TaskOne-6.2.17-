""" Program takes file name as input and it will reverse the words
	inside the file and gives output in new_reversed_file.txt file"""


def word_count(input_file):
    file_read = open(input_file, "r")
    file_read_new = open('new_reversed_file.txt', 'w')
    word_list = []
    for line in file_read:
        for word in line.split(" "):
            word_list.append(str((word)[::-1]))

    for i in reversed(word_list):
        file_read_new.write(i + ' ')
    file_read.close()
    file_read_new.close()

if __name__ == '__main__':
    file_name = raw_input('Enter the file name\n')
    word_count(file_name)

