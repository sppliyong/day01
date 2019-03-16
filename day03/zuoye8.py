def fun1(x):
    i=0
    while i<=x:
        j = x-i
        k = 0
        while j>0:
            print(" ",end="")
            j-=1
        while k<i:
            print("*",end=" ")
            k+=1
        print()
        i+=1
def fun2(x):
    i=0
    while i<x:
        j=x-i
        k=0
        while j>0:
            print(" ",end="")
            j-=1
        while k<i:
            print("*",end=" ")
            k+=1
        print()
        i+=1
    m=0
    while m<x:
        j=0
        k=x-m
        while j<m:
            print(" ",end="")
            j+=1
        while k>0:
            print("*",end=" ")
            k-=1
        print()
        m+=1

def fun3(x):
    for i in range(1,x+1):
        for j in range(1,i+1):
            print(str(j)+"*"+str(i)+"="+str(i*j).rjust(2),end=" ")
            if i==j:
                print()



def fun4():
    for i in range(0,110):
        print(str(i).rjust(4),end="  ")
        if (i+1)%3==0:
            print()


if __name__ == '__main__':
    fun4()