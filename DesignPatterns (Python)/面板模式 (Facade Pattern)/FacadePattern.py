__author__ = "ChiangWei"
__date__ = "2022/05/28"

class Register:
    def register(self, name):
        print("活動中心:%s同學報到成功！" % name)


class Payment:
    def pay(self, name, money):
        print("繳費中心:收到%s同學%s元付款，繳費成功！" % (name, money) )


class DormitoryManagementCenter:
    def provideLivingGoods(self, name):
        print("生活中心:%s同學的生活用品已發放。" % name)


class Dormitory:
    def meetRoommate(self, name):
        print("宿舍:" + "大家好！這是剛來的%s同學，是你們未來需要共度四年的室友！相互認識一下……" % name)


class Volunteer:
    def __init__(self, name):
        self.__name = name
        self.__register = Register()
        self.__payment = Payment()
        self.__lifeCenter = DormitoryManagementCenter()
        self.__dormintory = Dormitory()

    def welcomeFreshmen(self, name):
        print("你好,%s同学! 我是新生报到的志愿者%s，我将带你完成整个报到流程。" % (name, self.__name))
        self.__register.register(name)
        self.__payment.pay(name, 10000)
        self.__lifeCenter.provideLivingGoods(name)
        self.__dormintory.meetRoommate(name)

def testRegister():
    volunteer = Volunteer("Frank")
    volunteer.welcomeFreshmen("Tony")

testRegister()
