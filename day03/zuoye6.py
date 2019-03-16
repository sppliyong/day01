import math
if __name__ == '__main__':
    str1=input("请输入一个数：")
    a=int(str1)
    mlist=[]
    while True:
        b=a%2
        mlist.append(b)
        a=a//2
        if a==0:
            break
    print(mlist)

    mlist.reverse()
    print(mlist)
    bb=""
    for i in mlist:
        bb+=str(i)
    print("这个数的二进制是："+bb)



