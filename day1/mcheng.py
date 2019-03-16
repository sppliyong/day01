if __name__ == '__main__':
     m9=[1,2,3,4,5,6,7,8,9]
     for i in m9:
         for j in m9[0:i]:
             if j!=i:
                print(i,end="*"), print(j,end="="),print(i*j,end="  ")
             else:
                print(i, end="*"), print(j, end="="), print(i*j)