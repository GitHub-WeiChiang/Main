# 壞蛋接口，定義了所有壞蛋的行為
class BadCharacterSkill:
    def basicAttack(self):
        pass

    def magicAttack(self):
        pass

    def recover(self):
        pass

# 小壞蛋實作壞蛋接口，但並沒有使用所有壞蛋行為
class Monster(BadCharacterSkill):
    def basicAttack(self): 
        print('monster basic attack')

# 大壞蛋實作壞蛋接口，有使用所有壞蛋行為
class MonsterBoss(BadCharacterSkill):
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
