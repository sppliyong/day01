if __name__ == '__main__':
   mlist=[1,2,2,2,3,4,5,6,6]
   mset=set(mlist)
   if len(mlist)>len(mset):
       print("有重复！！")

   for i in mset:
       num=mlist.count(i)
       if num>1:
           print(str(i)+"是重复的！！")

   alist=["aa","bb","cc"]
   blist=["aa","aa","cc","dd"]
   mdic={}
   for i in alist:
       mdic[i]=blist.count(i)
   print(mdic)
