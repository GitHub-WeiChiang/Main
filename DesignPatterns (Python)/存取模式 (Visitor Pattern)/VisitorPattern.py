__author__ = "ChiangWei"
__date__ = "2022/07/01"

# from abc import ABCMeta, abstractmethod

# class DesignPatternBook:
#     def getName(self):
#         return "《從生活的角度解讀設計模式》"

# class Reader(metaclass=ABCMeta):
#     @abstractmethod
#     def read(self, book):
#         pass

# class Engineer(Reader):
#     def read(self, book):
#         print("技術狗讀%s一書後的感受：能抓住模式的核心思想，深入淺出，很有見地！" % book.getName())

# class ProductManager(Reader):
#     def read(self, book):
#         print("產品經理讀%s一書後的感受：配圖非常有趣，文章很有層次感！" % book.getName())

# class OtherFriend(Reader):
#     def read(self, book):
#         print("IT圈外的朋友讀%s一書後的感受：技術的內容一臉懵逼，但故事很精彩，像是看小說或是故事集！" % book.getName())

# def testBook():
#     book = DesignPatternBook()
#     fans = [Engineer(), ProductManager(), OtherFriend()];
#     for fan in fans:
#         fan.read(book)

# testBook()

from abc import ABCMeta, abstractmethod

class DataNode(metaclass=ABCMeta):
    def accept(self, visitor):
        visitor.visit(self)

class Visitor(metaclass=ABCMeta):
    @abstractmethod
    def visit(self, data):
        pass

class ObjectStructure:
    def __init__(self):
        self.__datas = []

    def add(self, dataElement):
        self.__datas.append(dataElement)

    def action(self, visitor):
        for data in self.__datas:
            data.accept(visitor)

class DesignPatternBook(DataNode):
    def getName(self):
        return "《從生活的角度解讀設計模式》"

class Engineer(Visitor):
    def visit(self, book):
        print("技術狗讀%s一書後的感受：能抓住模式的核心思想，深入淺出，很有見地！" % book.getName())

class ProductManager(Visitor):
    def visit(self, book):
        print("產品經理讀%s一書後的感受：配圖非常有趣，文章很有層次感！" % book.getName())

class OtherFriend(Visitor):
    def visit(self, book):
        print("IT圈外的朋友讀%s一書後的感受：技術的內容一臉懵逼，但故事很精彩，像是看小說或是故事集！" % book.getName())

def testVisitBook():
    book = DesignPatternBook()
    objMgr = ObjectStructure()
    objMgr.add(book)
    objMgr.action(Engineer())
    objMgr.action(ProductManager())
    objMgr.action(OtherFriend())

testVisitBook()
