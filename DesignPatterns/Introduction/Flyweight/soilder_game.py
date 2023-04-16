from typing import Dict
from abc import ABC, abstractmethod

# 士兵享元接口
class SoldierFlyweight(ABC):
    # 定義通用方法
    @abstractmethod
    def display(self, x: int, y: int):
        pass

# 實現士兵類型享元接口的具體類
class SoldierType(SoldierFlyweight):
    # 建構時，儲存共享狀態
    def __init__(self, soldier_type: str, weapon: str, armor: str):
        # 類型
        self.soldier_type = soldier_type
        # 武器
        self.weapon = weapon
        # 護甲
        self.armor = armor

    # 實現抽象方法
    def display(self, x: int, y: int):
        print(f"Displaying {self.soldier_type} at ({x}, {y}) with weapon {self.weapon} and armor {self.armor}")

# 生成工廠，管理士兵類型
class SoldierFlyweightFactory:
    def __init__(self):
        # 幫助獲取共享實例
        self.soldier_type_map: Dict[str, SoldierFlyweight] = {}

    # 獲取實例
    def get_soldier_type(self, soldier_type: str, weapon: str, armor: str) -> SoldierFlyweight:
        # 此處要注意多執行緒下可能重複生成單一實例的問題
        
        soldier_flyweight = self.soldier_type_map.get(soldier_type)

        if soldier_flyweight is None:
            soldier_flyweight = SoldierType(soldier_type, weapon, armor)
            self.soldier_type_map[soldier_type] = soldier_flyweight
        
        return soldier_flyweight

# 士兵類別
class Soldier:
    # 用於存取不共享內容
    def __init__(self, soldier_flyweight: SoldierFlyweight, x: int, y: int):
        self.soldier_flyweight = soldier_flyweight
        self.x = x
        self.y = y

    def display(self):
        self.soldier_flyweight.display(self.x, self.y)

class SoldierGame:
    @staticmethod
    def main():
        # 創建工廠實例
        soldier_type_factory = SoldierFlyweightFactory()

        # 創建與獲取相應士兵類型實例
        # 弓箭手
        archer_type = soldier_type_factory.get_soldier_type("Archer", "Bow", "Leather")
        # 騎士
        knight_type = soldier_type_factory.get_soldier_type("Knight", "Sword", "Plate")

        # 創建士兵實例，重複使用相同類型的士兵。
        archer1 = Soldier(archer_type, 100, 50)
        archer2 = Soldier(archer_type, 120, 60)
        knight1 = Soldier(knight_type, 200, 100)
        knight2 = Soldier(knight_type, 250, 120)

        archer1.display()
        archer2.display()
        knight1.display()
        knight2.display()

if __name__ == "__main__":
    SoldierGame.main()
