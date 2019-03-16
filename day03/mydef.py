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
    nlist=[i.strip() for i in klist]
    nset=set(nlist)
    print(nset)
    mset=set(nlist)
    mdic={}
    alist=list(nset)
    blist=list(nset)
    print("alist={alist}".format(alist=alist))
    print("blist={blist}".format(blist=blist))
    for i in alist:
        mdic[i]=blist[blist.index(i)]
    print(mdic)
    plist=list("wsxedc")
    pset=set("wsxedc")
    print(plist)
    print(pset)
