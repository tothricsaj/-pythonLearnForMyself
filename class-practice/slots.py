class SlotClass(object):
    __slots__ = ('a')


class SlotWithDict():
    __slots__ = ('__dict__', 'b')


if __name__ == '__main__':
    print('Hello slots!!!!')

    sc = SlotClass()
    sc.a = 22

    print(sc.a)

    print('\n')

    swd = SlotWithDict()
    swd.a = 23
    swd.b = 'Susi musi'
    swd.c = 42

    print(swd.a)
    print(swd.b)
    print(swd.c)
    print(swd.__dict__)
