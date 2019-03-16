if __name__ == '__main__':
    str1=input("输入某年某月某日，判断这一天是这一年的第几天？")
    aa1=str1[:4:]
    aa2=str1[4:6:]
    aa3=str1[-2::]
    if int(aa3)>10:
        mm=aa3
    else:
        mm=str(aa3).split(1)
    print("这是："+aa1+"年的"+mm+"天")