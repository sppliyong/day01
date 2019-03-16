class MyExcep(Exception):
    def show(self):
        print("11111")
if __name__ == '__main__':
    # mm=MyExcep()
    # mm.show()
    try:
        raise MyExcep
    except MyExcep as e:
        print("2222")
        e.show()

