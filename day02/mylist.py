if __name__ == '__main__':
    mlist=list()# ==mlist=[]
    print(type(mlist))#创建列表
    mlist.append("111")
    mlist.append("222")
    mlist.insert(4,"4444")
    print(mlist)

    var2=mlist.index("4444")
    print(var2)

    mlist.pop()#默认删除最后的一个
    print(mlist)
    del mlist[0]
    print(mlist)
    mlist.append("111")
    mlist.append("222")
    print(mlist)
    mlist.remove("111")
    print(mlist)
    mlist.clear()
    print(mlist)
    mlist.append("111")
    mlist.append("222")
    print(mlist)
    print("222444444444444")
    mlist.pop(0)
    print(mlist)


