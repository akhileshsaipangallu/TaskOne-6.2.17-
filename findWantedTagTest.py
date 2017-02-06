from bs4 import BeautifulSoup
""" Program takes Tag name, Attribute name, Attribute value as input and it
    will print content inside the tag and print it."""


def find_tags(input_tag, input_attr, input_attr_value):
    try:
        soup = BeautifulSoup(open('sampleHTML.html'))
        tag = soup.find(input_tag, {input_attr: input_attr_value})
        return tag.string
    except AttributeError:
        return 'No such attribute/tag/value'

if __name__ == '__main__':
    tag = raw_input('Enter a tag to find in file\n')
    attr = raw_input('Enter a attribute to find in file\n')
    attr_value = raw_input('Enter the attribute value to find in file\n')
    print(find_tags(tag, attr, attr_value))

