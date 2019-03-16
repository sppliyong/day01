import day04.quest.p1 as pp
if __name__ == '__main__':
    mdic={
        1:"①请输入名字，以及性别",
        2:"②查看并集",
        3:"3邮箱判断",
        4:"④判断是否是回数"
    }
    ndic={
        1:pp.fun1,
        2:pp.fun2,
        3:pp.fun3,
        4:pp.fun4
    }
    while True:
        for i  in mdic.values():
            print(i)
        aa=int(input("请输入编号："))
        for k,v in ndic.items():
            if int(k) == int(aa):
                v()
        if aa==0:
            break













