def fun1():
    str1=input("请输入字符串：")
    str2=str1[::-1]
    print(str2)
def fun2():
    mlist=[input("请输入名字：") for i in range(1,5) ]
    print(mlist)
    nlist=[len(i) for i in mlist ]
    print(nlist)
    mmdic={}
    for i in sorted(nlist):
        mmdic[str(i)]=mlist[nlist.index(i)]
    print(mmdic)
    aalist=[i for i in mmdic.values()]
    aset=set(mlist)-set(aalist)
    klist=list(aset)
    print(klist)
    for i in klist:
        pass



def fun3():
    str1=input("请输入用户名：")
    str2=input("请输入密码：")
    if len(str1) in range(6,17) and len(str2) in range(6,17) and ("*"and"#" not in str1) and ("*"and"#" not in str2):
        print("密码和用户注册成功！！")
def fun4():
    str1=input("请输入社会主义价值观的全拼：")
    print(str1.split(" "))

if __name__ == '__main__':
     fun2()
    # mlist = ["张震", "王越", "靳中伟", "李庸", "李广军5555"]
    # mdict = {m: len(m) for m in mlist}
    # dict_sorted = dict(sorted(mdict.items(), key=lambda x: x[1], reverse=True))
    # print(dict_sorted)

