def outerFunc(txt):
    def innerFunc():
        print(txt)

    innerFunc()

if __name__ == '__main__':
    print('hello closure!!!\n')

    outerFunc('hey!!!')
