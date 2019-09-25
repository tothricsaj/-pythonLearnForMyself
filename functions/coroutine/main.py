def print_name(prefix):
    print("Searhchin prefix: {}".format(prefix))

    while True:
        name = (yield)
        if prefix in name:
            print(name)


if __name__ == '__main__':
    print('Hello coroutene!!!\n')

    corou = print_name('Dear')

    corou.__next__()
