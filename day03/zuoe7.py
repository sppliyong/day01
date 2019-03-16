def fun(name,password):
    print("name={namekey}".format(namekey=name))
    print("password={passwordkey}".format(passwordkey=password))
if __name__ == '__main__':
    fun(name="张三",password=123)