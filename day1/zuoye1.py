if __name__ == '__main__':
     str=input("请输入行数：")
     i=1
     while i<=int(str):
         j=0
         while j<=i:
            print("*",end="")
            j+=1
            if i==j:
                print()
                break
         i+=1

