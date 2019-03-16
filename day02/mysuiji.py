import  random
if __name__ == '__main__':
    # mlist =[random.randint(1,100) for i in range(0,10)]
# #     # print(mlist)
  #列表的复制
  nlist=[1,2,3]
  mlist=nlist[:]
  nlist[0]=3
  print("nlist={0}".format(nlist))
  print("mlist={0}".format(mlist))
  #赋值是传指的过程
  #复制数是传值的过程
