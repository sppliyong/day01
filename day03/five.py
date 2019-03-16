if __name__ == '__main__':
    # 复合生成式子
    #第一个
    mlist=[i*j for i in range(1,11) if i%2==0 for j in range(1,11)]
    print("mlist={mm}".format(mm=mlist))
    #第二种
    nlist=[i**2 for i  in range(1,11) ]
    print("nlist={mm}".format(mm=nlist))
    #第三种
    adic={k:v for k in range(1,11) for v in range(1,11)}
    print("adic={mm}".format(mm=adic))
    #第三种
    blist=[i for i in range(1,11) if i%2==0]
    print("blist={mm}".format(mm=blist))
    #第四种
    aalist=[1,2,3]
    bblist=["a","b","c"]
    qqlist=[]
    for m in aalist:
        for n in bblist:
            qqlist.append(str(m)+n)
    print("qqlist={mm}".format(mm=qqlist))

    qqlist=[str(m)+n for m in aalist for n in bblist]
    print("qqlist={mm}".format(mm=qqlist))
    nnlist=[i.title() for i in bblist]
    print("bblist={mm}".format(mm=bblist))
