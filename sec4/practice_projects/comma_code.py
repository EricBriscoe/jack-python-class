def list_thing(list):
    new_string = ''
    for i in list:
        new_string = new_string + str(i)
        if list.index(i) == (len(list) - 2):
            new_string = new_string + ', and '
        elif list.index(i) < (len(list) - 2):
            new_string = new_string + ', '
    return new_string


def list_thing_range(list):
    new_string = ''

    for i in range(len(list)):
        new_string += list[i]

        if i == (len(list) - 2):
            new_string += ', and '
        elif i < (len(list) - 2):
            new_string += ', '

    return new_string


def list_thing_enumerate(list):
    new_string = ''

    for i, thing in enumerate(list):
        new_string += thing

        if i < (len(list) - 2):
            new_string += ', '
        elif i == (len(list) - 2):
            new_string += ', and '

    return new_string


if __name__ == "__main__":
    # print(list_thing(['apples', 'bananas', 'tofu', 'apples', 'cats']))
    print(list_thing_range(['apples', 'bananas', 'tofu', 'apples', 'cats']))
