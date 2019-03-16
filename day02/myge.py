if __name__ == '__main__':
     for i in range(0,120):
         if (i+1)%10==0:
             print(str(i).rjust(4))
         else:
             print(str(i).rjust(4),end="")