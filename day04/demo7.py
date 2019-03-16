if __name__ == '__main__':
      #mfile=open(r"D:\AI2\day01\day04\a.c")
      with open(r"D:\AI2\day01\day04\a.c") as f:
            while True:
                  mline=f.readline()
                  if mline=="":
                        break



      # mpost=mfile.tell()#汉字是三个光标
      # print("before seek"+str(mpost))
      #
      # mfile.seek(2)
      # npost=mfile.tell()
      # print(npost)

      #val=mfile.read()
      # mbool=mfile.readable()
      # mlist=mfile.readlines()
      # print(mbool)
      # print(mlist)

      # mwr=mfile.write("gundan")
      # mlist = ["gun", "dan", "heheh11111"]
      # mfile.writelines(mlist)
      # print("mwr={mwr}".format(mwr=mwr))
      # mfile.close()




      # while True:
      #     val = mfile.readline()
      #     if val=="":
      #         break
      #     print(val)


