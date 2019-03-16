if __name__ == '__main__':
    str=input("请输入行数：")
    i=1
    while i<=int(str):
        k = 1
        j = 1
        while k<=int(str)-i:
            print(" ",end="")
            k+=1
        while j<=(2*i-1):
            print("*",end="")
            j+=1
        print()
        i+=1

    j=int(str)
    while j>0:
        i = 2
        k= 1
        while k <=int(str)-j+1:
            print(" ", end="")
            k+= 1
        while i < 2*j-1:
            print("*", end="")
            i+= 1
        print()
        j-=1





