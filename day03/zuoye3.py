if __name__ == '__main__':
    str1=input("请输入第一个人的月份：")
    str2=input("请输入第二个人的月份：")
    bb=int(str1)%int(str2)
    cc=int(str2)%int(str1)
    if int(str1)>int(str2):
        if bb==1:
            print("非常有缘")
        elif bb==2:
            print("比较有缘")
        elif bb==3:
            print("缘分一般")
        elif bb==4:
            print("有仇")
        else:
            print("没缘分")

    if int(str1) < int(str2):
        if bb == 1:
            print("非常有缘")
        elif bb == 2:
            print("比较有缘")
        elif bb == 3:
            print("缘分一般")
        elif bb == 4:
            print("有仇")
        else:
            print("没缘分")


