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

    corou.send('Ricsi')
    corou.send('Dear Ricsi')
    corou.send('Dear Python')
    corou.send('Evil Java')
    corou.send('Pikaaboo')
    corou.send('Dear JavaScript')
    corou.send('Dear JavaScript')


