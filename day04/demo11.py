def fun(n):
    print("00")

if __name__ == '__main__':
    mlist=[i for i in range(1,11)]
    print(mlist)
    nmap=map(fun,mlist)
    print(nmap)
    for i in nmap:
        print(i,end=" ")


# def mymulten(n):
#     return n * 10
#
#
# if __name__ == "__main__":
#         li = [i for i in range(10)]
#         # print(li)
#         nli = map(mymulten, li)
#         # print(nli)
#         for l in nli:
#             print(l, end=" ")

