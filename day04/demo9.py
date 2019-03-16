if __name__ == '__main__':
    str1="ssss    eee dd d d d dd  " \
         "11111" \
         "2222             "
    str2=str1.center(100,"0")
    print(str2)
    aa=int(str1.rfind("e"))
    print(aa)
    str3=str1.partition("e")
    print(str3)
    mlist=str1.splitlines()
    print(mlist)
    str4="111aaa "
    print(str4.isalnum())
    print(str4.isalpha())

    nlist=["aa","bb","cc"]
    mm=str(nlist)
    nn="".join(nlist)
    print(nn)
    print(mm)
    klist=list(nn)
    print(klist)















