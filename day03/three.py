if __name__ == '__main__':
    klist = [
        "good ", "good ", "study",
        " good ", "good", "study ",
        "good ", " good", " study",
        " good ", "good", " study ",
        "good ", "good ", "study",
        " day ", "day", " up",
        " day ", "day", " up",
        " day ", "day", " up",
        " day ", "day", " up",
        " day ", "day", " up",
        " day ", "day", " up",
        " day ", "day", " up",
    ]
    #编写Python程序判断字符串是否重复。（50分）

    alist=[i.strip() for i in klist]
    print(alist)

    aset=set(alist)
    if len(alist)>len(aset):
        print("有重复！！")
    print(aset)

    for i in aset:
        num=alist.count(i)
        if num>1:
            print(i)
    # 把下面的klist作为字典的键
    adesc={}
    for i in aset:
        adesc[i]=alist.count(i)
    print(adesc)
    blist=list(sorted(adesc))
    for i in blist:
        adesc[i]= alist.count(i)
    print(adesc)