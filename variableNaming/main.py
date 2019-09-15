class T():
    def __init__(self):
        self._myPrivat = 'I am private...'
        self.__totalPrivat = 'I am real private....'


if __name__ == '__main__':
    print('hello naming\n')

    t = T()
    print(t._myPrivat)
    print(t.__totalPrivat)
