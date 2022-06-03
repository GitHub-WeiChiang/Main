__author__ = "ChiangWei"
__date__ = "2022/6/3"

def metafunc(clsname, bases, attrs):
    print(clsname, bases, attrs)
    return type(clsname, bases, attrs)

class Some(metaclass=metafunc):
    def doSome(self):
        print('XD')
