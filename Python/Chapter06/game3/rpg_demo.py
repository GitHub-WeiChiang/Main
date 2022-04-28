__author__ = "ChiangWei"
__date__ = "2022/04/28"

import rpg

def draw_fight(role):
    print(role, end = '')
    role.fight()

swordsman = rpg.SwordsMan('Justin', 1, 200)
draw_fight(swordsman)

magician = rpg.Magician('Monica', 1, 100)
draw_fight(magician)

