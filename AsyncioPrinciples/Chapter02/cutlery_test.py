import threading

from queue import Queue
from attr import attrs, attrib


# 繼承 Thread
class ThreadBot(threading.Thread):
    def __init__(self):
        # 設置 target 方法
        super().__init__(target=self.manage_table)

        # 該機器人用於儲存從廚房取的刀叉的物件
        self.cutlery = Cutlery(knives=0, forks=0)
        # 需執行作業佇列
        self.tasks = Queue()

    # 機器人的主要程序
    def manage_table(self):
        # 不讓機器人睡
        while True:
            # 取得任務
            task = self.tasks.get()

            # 執行準備桌桌作業 (從廚房拿刀叉放到自己這)
            if task == 'prepare table':
                kitchen.give(to=self.cutlery, knives=4, forks=4)
            # 執行整理著著作業 (將刀叉還給廚房)
            elif task == 'clear table':
                self.cutlery.give(to=kitchen, knives=4, forks=4)
            # 機器人想休息要等待關機作業的指令
            elif task == 'shutdown':
                return


@attrs
class Cutlery:
    knives = attrib(default=0)
    forks = attrib(default=0)
    # lock = attrib(threading.Lock())

    # 刀叉交換作業
    def give(self, to, knives, forks):
        self.change(-knives, -forks)
        to.change(knives, forks)

    # 刀叉交換作業輔助函式
    def change(self, knives, forks):
        # with self.lock:
        self.knives += knives
        self.forks += forks


if __name__ == '__main__':
    # 廚房刀叉庫存
    kitchen = Cutlery(knives=100, forks=100)
    # 機器人總數
    bots = [ThreadBot() for i in range(10)]

    # 塞入執行任務
    for bot in bots:
        for i in range(1000):
            bot.tasks.put('prepare table')
            bot.tasks.put('clear table')
        bot.tasks.put('shutdown')

    print('Kitchen inventory before service:', kitchen)

    for bot in bots:
        bot.start()

    for bot in bots:
        bot.join()

    print('Kitchen inventory after service:', kitchen)
