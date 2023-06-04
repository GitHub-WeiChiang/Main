class TextEditor2:
    def __init__(self):
        # 舊有變量
        self.content = []

    # 舊有方法
    def write(self, text):
        self.content.append(text)
        print("Current content: " + ''.join(self.content))

    # 新方法: 返回 Memento 對象，其包含當前狀態。
    def save(self):
        return self.Memento(''.join(self.content))

    # 新方法: 接收 Memento 對象，並將狀態恢復成 Memento 對象所紀錄的狀態。
    def restore(self, memento):
        self.content = list(memento.get_content())

    # Memento 內部類別
    class Memento:
        def __init__(self, content):
            # 用於儲存當前狀態的變量
            self.content = content

        # 獲取當前存儲的狀態
        def get_content(self):
            return self.content


# main function
def main():
    # Create a text editor
    editor = TextEditor2()

    # Edit text
    editor.write("This is the first sentence.")

    # Save current state
    saved = editor.save()

    # Edit text
    editor.write(" This is the second sentence.")

    # Print current text
    print("Before restore: " + editor.save().get_content())

    # Restore to previous state
    editor.restore(saved)

    # Print current text
    print("After restore: " + editor.save().get_content())


if __name__ == "__main__":
    main()

    # 文本編輯器具備撤銷操作功能，
    # 只要透過創建 Memento 對象 (內部狀態獲取，並保存於該對象外)，
    # 在任何需要時間點進行恢復實作，
    # 且並不破壞現有代碼的封裝性。
