# 小壞蛋接口，定義了所有小壞蛋的行為
class BadCharacterSkill:
    def basicAttack(self):
        pass

# 大壞蛋接口，定義了所有大壞蛋的行為
class AdvancedBadCharacterSkill:
    def magicAttack(self):
        pass

    def recover(self):
        pass

# 小壞蛋只需要實作小壞蛋接口，不會造成類別 (接口) 臃腫
class Monster(BadCharacterSkill):
    def basicAttack(self): 
        print('monster basic attack')

# 大壞蛋需實作小壞蛋與大壞蛋接口
class MonsterBoss(BadCharacterSkill, AdvancedBadCharacterSkill):
    def basicAttack(self): 
        print('monsterboss basic attack')

    def magicAttack(self): 
        print('monsterboss magic attack')

    def recover(self): 
        print('monsterboss recover')

m = Monster()
m.basicAttack()

mb = MonsterBoss()
mb.magicAttack()
