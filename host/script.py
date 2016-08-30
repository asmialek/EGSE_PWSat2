from add_pinout import write_pins


def read_pins():
    try:
        file = open('pinout.txt', 'r')
    except IOError as e:
            if e.errno == 2:
                print('There is no \"pinout.txt\" file.')
                write_pins()
            else:
                print("I/O error({0}): {1}".format(e.errno, e.strerror))
    return eval(file.read())


if __name__ == "__main__":
    pinout = read_pins()
    print(pinout)