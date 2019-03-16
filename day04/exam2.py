import  random
if __name__ == '__main__':
    mlist=[random.randint(1,101) for i in range(1,11) ]
    print(mlist)
    int=random.randint(1,101)
    print(int)
    if int in mlist:
        print("在里面")
    else:
        print("不再里面")