class SlotClass(object):

    __slots__ = ['val']

    def __init__(self, val):
        self.val = val


if __name__ == '__main__':
    print('Hello slots!!!!')

    sc = SlotClass(42)

    print(sc.val)

    print('\n')

