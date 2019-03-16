import random
def fun1(num):
    for i in range(0, num):
        print("  " * (num - i), end=" ")
        print(" * ".center(3) * i)
    for i in range(0, num):
        print(" " * i, end=" ")
        print(" * ".center(3) * (num - i))
if __name__ == '__main__':
   fun1(5)
   print(random.randrange(1,10))
   print(random.randint(1, 10))
