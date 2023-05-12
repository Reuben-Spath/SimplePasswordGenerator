import random


# A function do shuffle all the characters of a string
def shuffle(string):
    temp_list = list(string)
    random.shuffle(temp_list)
    return ''.join(temp_list)


def length_creator(special, number, lower, upper):
    password = ascii_range(97, 122, lower) + ascii_range(65, 90, upper) + ascii_range(48, 57, number) + ascii_range(0,
                                                                                                                    1,
                                                                                                                    special)
    password = shuffle(password)
    print(password)

    # Generate password using all the characters, in random order


def ascii_range(start, end, length):
    creator = ''
    i = 0
    while i < length:
        if length != 'special':
            item = chr(random.randint(start, end))  # Generate a random Uppercase letter (based on ASCII code)
        else:
            item = chr(random.randint(*random.choice([(32, 47), (58, 64), (91, 96), (123, 126), (145, 149)])))

        creator = creator + item
        i += 1
    return creator


# Ouput
if __name__ == '__main__':
    length = input('How many characters would you like your system to be?')
    length = int(length)

    special = input('How many special would you like your system to be?')
    special = int(special)

    number = input('How many numbers would you like your system to be?')
    number = int(number)
    lower = input('How many lower case letters would you like your system to be?')
    lower = int(lower)

    upper = input('How many upper case characters would you like your system to be?')
    upper = int(upper)

    if length != (special + number + lower + upper):
        print(
            'There is an error, the length you have specified does not match with the length of the characters you chose')
    else:
        length_creator(special, number, lower, upper)
