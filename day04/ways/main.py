import day04.ways.p1 as ff
if __name__ == '__main__':
    mdic={
        1:"第一题",
        2:"第二题",
        3:"第三题",
        4:"第四题"
    }
    ndic={
        1:ff.fun1,
        2:ff.fun2,
        3:ff.fun3,
        4:ff.fun4
    }
    while True:
     for i in mdic.values():
        print(i)

     aa=int(input("请输入编号："))
     for k,v in ndic.items():
         if int(k)==aa:
             v()





