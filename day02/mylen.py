if __name__ == '__main__':

    str1=input("请输入一个字符串：")
    mset=set(str1)
    mlist=[i for i in mset]
    if len(mlist)<len(str1):
        print("有重复！！")


    for i in mset:
      num=str1.count(i)
      if num>1:
          print(i+"重复了")


    str1=input("请输入：")




