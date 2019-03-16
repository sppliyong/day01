if __name__ == '__main__':
    readfile= open(r"D:\AI2\day01\day04\aa.png","rb")
    mm=readfile.read()
    print(mm)
    writefile=open(r"D:\AI2\day01\day04\bb.png","wb")
    writefile.write(mm)
    readfile.close()
    writefile.close()

