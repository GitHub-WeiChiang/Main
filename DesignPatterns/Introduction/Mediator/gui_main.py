from abc import ABC, abstractmethod

# 抽象接口
class Mediator(ABC):
    # 定義抽象方法: 通知
    @abstractmethod
    def notify(self, sender, event):
        pass

# 具體中介類
class ConcreteMediator(Mediator):
    def __init__(self, button, text_box, label):
        # UI 引用與中介者參考取得: 按鈕、文字域、標籤
        self.button = button
        self.button.set_mediator(self)
        self.text_box = text_box
        self.text_box.set_mediator(self)
        self.label = label
        self.label.set_mediator(self)

    def notify(self, sender, event):
        # 具體交互邏輯處理: 當事件啟動對象為按鈕且事件行為為點擊
        if sender == self.button and event == 'clicked':
            # 交互邏輯處理
            self.text_box.clear()
            self.label.show('Button was clicked')

# 抽象類別: GUI 組建基類
class Component(ABC):
    def __init__(self):
        self.mediator = None

    # 取得中介引用
    def set_mediator(self, mediator):
        self.mediator = mediator

    # 通知中介事件發生
    def changed(self, event):
        self.mediator.notify(self, event)

# 具體同事類別: 按鈕
class Button(Component):
    def click(self):
        print('Button clicked')
        # 事件觸發
        self.changed('clicked')

# 具體同事類別: 文字域
class TextBox(Component):
    def clear(self):
        print('TextBox cleared')

# 具體同事類別: 標籤
class Label(Component):
    def show(self, message):
        print(f'Label shows: {message}')

if __name__ == '__main__':
    # 創建 GUI 對象
    button = Button()
    text_box = TextBox()
    label = Label()

    # 註冊至中介
    ConcreteMediator(button, text_box, label)

    # Simulate a button click
    button.click()
