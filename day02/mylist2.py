import  random
if __name__ == '__main__':
    str1=[1,10,3,2,5,6]
    random.shuffle(str1)
    print(str1)
    str1.sort(reverse=True)
    print(str1)
    nnmum=sorted(str1,reverse=True)
    print("nnum={0}".format(nnmum))
