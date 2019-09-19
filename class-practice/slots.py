class SlotClass():
    __slots__ = ('a')

if __name__ == '__main__':
    print('Hello slots!!!!')

    sc = SlotClass()
    sc.a = 22

    print(sc.a)
