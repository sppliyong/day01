import random
if __name__ == '__main__':
    str1=input("请输入一个数字：")
    str2=random.randint(10,50)
    if int(str1) > str2:
        print("最大的是："),print(int(str1))
    else:
        print("最大的是："), print(str2)