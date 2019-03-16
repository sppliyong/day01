if __name__ == '__main__':
    str1=input("请输入：")
    aa=str1[:4:]
    bb=str1[4:6:]
    cc=str1[-2::]
    print(aa)
    print(bb)
    print(cc)
    mdic={1:31,2:28,3:30,4:31,5:30,6:31,7:31,8:30,9:31,10:30,11:31,12:31}
    if int(aa)%100!=0 and int(aa)%4==0:
        dd=0
        for k,v in mdic.items():
            if int(k)==int(bb):
                break
            dd+=int(v)
        print(dd)

