# 員工類別
class Employee:
    def __init__(self, name):
        self.name = name

    def print_name(self):
        print(self.name)

# 組別類別
class Team:
    def __init__(self, name, employees=[]):
        self.name = name
        # 組別內有員工
        self.employees = employees

# 部門類別
class Department:
    def __init__(self, name, teams=[]):
        self.name = name
        # 部門內有組別
        self.teams = teams

# 管理者類別
class Manager:
    def __init__(self, name, departments=[]):
        self.name = name
        # 管理者可以管理部門
        self.departments = departments

# 顯示員工資訊
def print_team_names(team):
    print("Team:", team.name)
    for employee in team.employees:
        employee.print_name()

# 顯示部門資訊
def print_department_names(department):
    print("Department:", department.name)
    for team in department.teams:
        print_team_names(team)

# 顯示管理者資訊
def print_manager_names(manager):
    print("Manager:", manager.name)
    for department in manager.departments:
        print_department_names(department)

# 創建遞歸樹狀結構實例
employees = [Employee("John"), Employee("Jane"), Employee("Bob")]
team = Team("Engineering", employees)
department = Department("Product", [team])
manager = Manager("Alice", [department])

# 遞歸顯示樹狀結構
print_manager_names(manager)

# 如果要修改樹狀結構順序或是新增刪減新的結構，
# 會變得非常繁瑣複雜且難以維護。
