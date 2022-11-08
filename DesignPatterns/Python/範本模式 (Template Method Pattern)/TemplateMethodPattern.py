__author__ = "ChiangWei"
__date__ = "2022/07/02"

from abc import ABCMeta, abstractmethod

class Template(metaclass=ABCMeta):
    @abstractmethod
    def stepOne(self):
        pass

    @abstractmethod
    def stepTwo(self):
        pass

    @abstractmethod
    def stepThree(self):
        pass

    def templateMethold(self):
        self.stepOne()
        self.stepTwo()
        self.stepThree()

class TemplateImplA(Template):
    def stepOne(self):
        print("步驟一")

    def stepTwo(self):
        print("步驟二")

    def stepThree(self):
        print("步驟三")

class TemplateImplB(Template):
    def stepOne(self):
        print("Step one")

    def stepTwo(self):
        print("Step two")

    def stepThree(self):
        print("Step three")

def testTemplate():
    templateA = TemplateImplA()
    templateA.templateMethold()
    templateB = TemplateImplB()
    templateB.templateMethold()

testTemplate()
