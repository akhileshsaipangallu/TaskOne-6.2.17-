""" Program takes word as input and it will print the number of occurrence
    of the word inside the file"""


def word_count(input_word):
    file_read = open("test.txt", "r")
    word_list = []
    for line in file_read:
        for word in line.split(" "):
            for mini_word in word.split("\n"):
                for real_word in mini_word.split("."):
                    word_list.append(real_word)
    counter = word_list.count(input_word)
    return counter

if __name__ == '__main__':
    given_word = raw_input("Enter a word\n")
    print("Word = %s \nOccourance = %d" % (given_word, word_count(given_word)))

