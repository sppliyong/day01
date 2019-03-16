if __name__ == '__main__':
    for i in range(1,10):
        for j in range(1,i+1):
            if j!=i:
                print(i,end="*"),print(j,end="="),print(str(i*j).rjust(2),end=" ")
            else:
                print(i, end="*"), print(j, end="="), print(str(i*j).rjust(2))