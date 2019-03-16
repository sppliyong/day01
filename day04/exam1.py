if __name__ == '__main__':
    #请输入生日的格式 如20180909
    str1=input("请输入第一个人的生日：")
    str2=input("请输入第二个人的生日")
    a1=str1[:4:]
    a2=str1[4:6:]
    a3=str1[-2::]
    b1=str2[:4:]
    b2=str2[4:6:]
    b3=str2[-2::]
    if int(a1)>int(b1):
        print("第一个人的年龄大")
    elif int(a1)==int(b1):
        if int(a2)>int(b2):
            print("第一个人的年龄大")
        elif int(a2)==int(b2):
            if int(a3)>int(b3):
                print("第一个人的年龄大")
            elif int(a3)==int(b3):
                print("同年同月生")
            else:
                print("第二个人的年龄大")
        else:
            print("第二个人的年龄大")
    else:
        print("第二个人的年龄大")




