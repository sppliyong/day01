if __name__ == '__main__':
    mstr ="u can u up, u can u go"
    print(mstr[10:1:1])#和下面的对比一下 空的
    print(mstr[10:1:-1])#从第十位到第一位倒着来
    print(mstr[::])
    print(mstr[2:10])#左闭右开的原则
    print(mstr[-10:-1:-1])#和下面的进行对比一下 空的
    print("55"+mstr[-1:-10:-1])
    print("33"+mstr[-10:-1:1])#因为前面是倒这来的 所以最后一个数不能再是负数了
    print("11"+mstr[1:10:2])#说明是1到10 步长是2
    print("22"+mstr[1:10:-2])#空白的




