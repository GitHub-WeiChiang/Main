from abc import ABC, abstractmethod

# 抽象元件接口
class Component(ABC):
    @abstractmethod
    def print_name(self):
        pass

# 實作抽象元件接口
class Employee(Component):
    def __init__(self, name):
        self.name = name

    # 實現抽象方法
    def print_name(self):
        print(self.name)

# 實作抽象元件接口
class Department(Component):
    def __init__(self, name, components=[]):
        self.name = name
        self.components = components

    # 實現抽象方法
    def print_name(self):
        print("Department:", self.name)
        for component in self.components:
            component.print_name()

# 實作抽象元件接口
class Team(Component):
    def __init__(self, name, components=[]):
        self.name = name
        self.components = components

    # 實現抽象方法
    def print_name(self):
        print("Team:", self.name)
        for component in self.components:
            component.print_name()

# 實作抽象元件接口
class Manager(Component):
    def __init__(self, name, components=[]):
        self.name = name
        self.components = components

    # 實現抽象方法
    def print_name(self):
        print("Manager:", self.name)
        for component in self.components:
            component.print_name()

# 創建遞歸樹狀結構實例
employees = [Employee("John"), Employee("Jane"), Employee("Bob")]
team = Team("Engineering", employees)
department = Department("Product", [team])
manager = Manager("Alice", [department])

# 遞歸顯示樹狀結構
manager.print_name()

# 如果要修改樹狀結構順序或是新增刪減新的結構，
# 會變得相對簡單且易於維護。
