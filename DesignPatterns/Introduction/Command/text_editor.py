from abc import ABC, abstractmethod
from collections import UserList


# 命令接口: 定義命令抽象方法
class TextEditorCommand(ABC):
    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass

    @abstractmethod
    def redo(self):
        pass


# 抽象命令類別實現: 插入文本
class InsertTextCommand(TextEditorCommand):
    def __init__(self, text, text_editor, position):
        self.text = text
        self.text_editor = text_editor
        self.position = position

    def execute(self):
        self.text_editor.insert(self.position, self.text)

    def undo(self):
        self.text_editor.delete(self.position, self.position + len(self.text))

    def redo(self):
        self.execute()


# 抽象命令類別實現: 刪除文本
class DeleteTextCommand(TextEditorCommand):
    def __init__(self, text_editor, position, length):
        self.text_editor = text_editor
        self.position = position
        self.length = length
        self.deleted_text = None

    def execute(self):
        self.deleted_text = self.text_editor[self.position:self.position + self.length]
        self.text_editor.delete(self.position, self.position + self.length)

    def undo(self):
        if self.deleted_text is not None:
            self.text_editor.insert(self.position, self.deleted_text)

    def redo(self):
        self.execute()


# 命令控制器
class CommandInvoker:
    def __init__(self):
        self.history = []
        self.redo_history = []

    def execute(self, command):
        # 執行命令
        command.execute()
        # 加入操作歷史 (回上一步佇列)
        self.history.append(command)
        # 清空返回記錄 (撤銷取消佇列)
        self.redo_history.clear()

    def undo(self):
        if self.history:
            last_command = self.history.pop()
            last_command.undo()
            self.redo_history.append(last_command)

    def redo(self):
        if self.redo_history:
            last_redo_command = self.redo_history.pop()
            last_redo_command.redo()
            self.history.append(last_redo_command)


class TextEditor(UserList):
    def insert(self, index, text):
        for char in reversed(text):
            super().insert(index, char)

    def delete(self, start, end):
        del self[start:end]


if __name__ == "__main__":
    text_editor = TextEditor()
    invoker = CommandInvoker()

    invoker.execute(InsertTextCommand("Hello, ", text_editor, 0))
    invoker.execute(InsertTextCommand("world!", text_editor, 7))
    invoker.execute(DeleteTextCommand(text_editor, 5, 2))

    print("Current text: " + "".join(text_editor))

    invoker.undo()
    print("After undo: " + "".join(text_editor))

    invoker.undo()
    print("After undo: " + "".join(text_editor))

    invoker.redo()
    print("After redo: " + "".join(text_editor))
