def myfilter(n):
    return n%2==0
if __name__ == '__main__':
    mlist=[i for i in range(1,11)]
    nf=filter(myfilter,mlist)
    for f in nf:
        print(f)
