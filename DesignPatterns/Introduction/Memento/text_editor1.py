class TextEditor1:
    def __init__(self):
        # 用於儲存編輯器當前內容的變量
        self.content = []

    # 用於加入文本的方法 (同時會印出當前內容)
    def write(self, text):
        self.content.append(text)
        print("Current content: " + ''.join(self.content))

# 沒有撤銷操作功能，主要是沒有保存前一狀態。
