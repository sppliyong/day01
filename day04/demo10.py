if __name__ == '__main__':
    aa=lambda :1000
    print(aa())
    bb=lambda x:100*x
    print(bb(2))
    def good(n):
        return n*10

    def luck(n,func):
        return func(10)*10

