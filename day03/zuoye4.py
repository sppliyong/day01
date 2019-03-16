import random
if __name__ == '__main__':
    mlist=[random.randint(1,100) for i in range(1,11) ]
    print(mlist)
    str1=random.randint(1,1000)
    print(str1)
    if str1 in mlist:
        print("存在")
    else:
        print("不存在")