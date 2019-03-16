class MyExcept(Exception):
    pass
    def show(self):
        print("11111")

if __name__ == '__main__':
    mm=MyExcept()#创建对象
    mm.show()#调用方法
    try:
        pass
    except:
        pass

