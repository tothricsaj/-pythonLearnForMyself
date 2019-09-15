class T():
    def __init__(self):
        self._myPrivat = 'I am private...'
        self.__totalPrivat = 'I am real private....'

    @property
    def total_private(self):
        return self.__totalPrivat

    @total_private.setter
    def total_private(self, new_str):
        self.__totalPrivat = new_str

    def update(self):
        print('This is update function from T class!')



class T_Sub(T):
    def __init__(self):
        T.__init__(self)


if __name__ == '__main__':
    print('hello naming\n')

    t = T()
    t_sub = T_Sub()

    print(t_sub._myPrivat)
    print(t.total_private)

    t.total_private = 'I am swaped....sad    :('

    print(t.total_private)

    t_sub.update()

