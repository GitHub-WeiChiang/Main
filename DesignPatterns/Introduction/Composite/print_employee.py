# 員工類別
class Employee:
    def __init__(self, name):
        self.name = name

    def print_name(self):
        print(self.name)

# 建立員工實例
employees = [Employee("John"), Employee("Jane"), Employee("Bob")]

# 顯示員工資訊
for employee in employees:
    employee.print_name()
