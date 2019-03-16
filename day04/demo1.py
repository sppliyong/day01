if __name__ == '__main__':
    mlist=["name","age","sex"]
    nlist=["spp","12","男"]
    adic={}
    for i in mlist:
        print(i)
        adic[i]=nlist[mlist.index(i)]
    print(adic)
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
    print("nset={nset}".format(nset=nset))
    alist=list(nset)
    blist=alist.copy()
    print("alist={alist}".format(nset=nset))
    print("nset={nset}".format(nset=nset))

