__author__ = "ChiangWei"
__date__ = "2022/04/29"

class HouseInfo:
    def __init__(self, area, price, hasWindow, hasBathroom, hasKitchen, address, owner):
        self.__area = area
        self.__price = price
        self.__hasWindow = hasWindow
        self.__hasBathroom = hasBathroom
        self.__hasKitchen = hasKitchen
        self.__address = address
        self.__owner = owner

    def getAddress(self):
        return self.__address

    def getOwnerName(self):
        return self.__owner.getName()

    def showInfo(self, isShowOwner = True):
        print("面積: " + str(self.__area) + "平米", "價格: " + str(self.__price) + "元", "窗戶: " + ("有" if self.__hasWindow else "沒有"), "衛生間: " + self.__hasBathroom, "廚房: " + ("有" if self.__hasKitchen else "沒有"), "地址: " + self.__address, "房東: " + self.getOwnerName() if isShowOwner else "")

class HousingAgency:
    def __init__(self, name):
        self.__houseInfos = []
        self.__name = name

    def getName(self):
        return self.__name

    def addHouseInfo(self, houseInfo):
        self.__houseInfos.append(houseInfo)

    def removeHouseInfo(self, houseInfo):
        for info in self.__houseInfos:
            if(info == houseInfo):
                self.__houseInfos.remove(info)

    def getSearchCondition(self, description):
        # do something ...
        return description

    def getMatchInfos(self, searchCondition):
        # do something ...
        print(self.getName(), "為您找到以下最適合的房源: ")
        for info in self.__houseInfos:
            info.showInfo(False)
        return  self.__houseInfos

    def signContract(self, houseInfo, period):
        print(self.getName(), "與房東", houseInfo.getOwnerName(), "簽訂", houseInfo.getAddress(), "的房子的的租賃合同，租期", period, "年。合同期內", self.getName(), "有權對其進行使用和轉租！")

    def signContracts(self, period):
        for info in self.__houseInfos :
            self.signContract(info, period)

class HouseOwner:
    def __init__(self, name):
        self.__name = name
        self.__houseInfo = None

    def getName(self):
        return self.__name

    def setHouseInfo(self, address, area, price, hasWindow, bathroom, kitchen):
        self.__houseInfo = HouseInfo(area, price, hasWindow, bathroom, kitchen, address, self)

    def publishHouseInfo(self, agency):
        agency.addHouseInfo(self.__houseInfo)
        print(self.getName() + "在", agency.getName(), "發布房源出租信息: ")
        self.__houseInfo.showInfo()

class Customer:
    def __init__(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def findHouse(self, description, agency):
        print("我是" + self.getName() + ", 我想要找一個\"" + description + "\"的房子")
        print()
        return agency.getMatchInfos(agency.getSearchCondition(description))

    def seeHouse(self, houseInfos):
        # do something ...
        size = len(houseInfos)
        return houseInfos[size-1]

    def signContract(self, houseInfo, agency, period):
        # do something ...
        print(self.getName(), "與仲介", agency.getName(), "簽訂", houseInfo.getAddress(), "的房子的租賃合同, 租期", period, "年。合同期內", self.__name, "有權對其進行使用！")

def testRenting():
    myHome = HousingAgency("我愛我家")
    zhangsan = HouseOwner("張三");
    zhangsan.setHouseInfo("上地溪裡", 20, 2500, 1, "獨立衛生間", 0)
    zhangsan.publishHouseInfo(myHome)
    lisi = HouseOwner("李四")
    lisi.setHouseInfo("當代城市家園", 16, 1800, 1, "公用衛生間", 0)
    lisi.publishHouseInfo(myHome)
    wangwu = HouseOwner("王五")
    wangwu.setHouseInfo("金隅美和園", 18, 2600, 1, "獨立衛生間", 1)
    wangwu.publishHouseInfo(myHome)
    print()

    myHome.signContracts(3)
    print()

    tony = Customer("Tony")
    houseInfos = tony.findHouse("18平米左右，要有獨衛，要有窗戶，最好是朝南，有廚房更好！價位在2000左右", myHome)
    print()
    print("正在看房，尋找最合適的住巢......")
    print()
    AppropriateHouse = tony.seeHouse(houseInfos)
    tony.signContract(AppropriateHouse, myHome, 1)

testRenting()


# # 框架簡述
# class InteractiveObject:
#     pass

# class InteractiveObjectImplA:
#     pass

# class InteractiveObjectImplB:
#     pass

# class Meditor:
#     def __init__(self):
#         self.__interactiveObjA = InteractiveObjectImplA()
#         self.__interactiveObjB = InteractiveObjectImplB()

#     def interative(self):
#         pass
