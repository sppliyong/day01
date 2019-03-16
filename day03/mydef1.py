def myFun(name,cnt,val="spp",):
    print(val)
    print(cnt)
    print(name)


def myFun2(name,passwprd=""):
    pass
def myFun3(**param):
    print(param)

def myFun4(*param):
    print(param)
def aa(*myp):
    print(type(myp))
    mlist=[i for i in myp]
    print("mlist={mlist}".format(mlist=mlist))
def bb():
   pass

#位置应该是  位置传参  没有默认值传参  有默认值最后
#没有默认值在有默认值的前面
if __name__ == '__main__':
    myFun("史盼盼",6)#关键字传参
    myFun3(k=3,v=4)
    aa("hehe","hoho","hahha")

