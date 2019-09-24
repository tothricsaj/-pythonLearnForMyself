def outerFunc(txt):
    def innerFunc(iTxt):
        print(txt + " " + iTxt)

    return innerFunc

if __name__ == '__main__':
    print('hello closure!!!\n')

    my_func = outerFunc('hey!!!')
    my_func('honyDucky')
