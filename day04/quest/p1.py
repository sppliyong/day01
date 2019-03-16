import  random
def fun1():
    name = input("请输入姓名：")
    sex = input("请输入性别：")
    nlist=["男","femal","man","先生"]
    mlist=["女","woman","girl","女士"]
    if sex in nlist:
        print("{namekey}先生你好！".format(namekey=name))
    if sex in mlist:
        print("{namekey}女士你好！".format(namekey=name))

def fun2():
    nlist=[random.randint(1,101) for i in range(1,11)]
    mlist=[random.randint(1, 101) for i in range(1, 11)]
    nset=set(nlist)
    mset=set(mlist)
    aaset=nset|mset
    print(aaset)
def fun3():
    name = input("请输入名字：")
    email = input("请输入邮箱：")
    if len(name)>6 and "@"in email:
        print("信息合法")
    else:
        print("信息不会合法姓名长度不能少于6位，邮件中包含@")

def fun4():
    num = int(input("请输入一个数："))
    if len(str(num))%2==1:
     mm=str(num)
     m1=mm[:(len(mm)+1)//2-1:]
     m2=mm[-((len(mm)+1)//2-1)::]
     print(m1)
     print(m2)
     m3=m2[::-1]
     print(m3)
     if int(m1)==int(m3):
         print("是合数")
     else:
         print("不是合数")
    else:
        print("不是合数")
if __name__ == '__main__':
       pass
