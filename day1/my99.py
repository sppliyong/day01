if __name__ == '__main__':
   mar= range(1,10)
   for i in mar:
       for j in mar[0:i]:
           if j!=i:
               print(i,end="*"),print(j,end="="),print(i*j,end="  ")
           else:
               print(i, end="*"), print(j, end="="), print(i*j)



   print("--------------------")
   str=int("请输入菱形的边长:")
   i=0
   while i<int(str):
       j=0
       k=0
       while j<int(str)-i:
           print(" ",end=" ")
           j+=1
       