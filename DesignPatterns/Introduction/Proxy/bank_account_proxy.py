from abc import ABC, abstractmethod


# 接口，用於定義通用方法
class BankAccount(ABC):
    # 存錢
    @abstractmethod
    def deposit(self, amount):
        pass

    # 領錢
    @abstractmethod
    def withdraw(self, amount):
        pass


# 實際處理類別
class RealBankAccount(BankAccount):
    def __init__(self, initial_balance):
        # 當前餘額
        self.balance = initial_balance

    # 實現存錢方法
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited: {amount}, new balance: {self.balance}")

    # 實現領錢方法
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrew: {amount}, new balance: {self.balance}")
        else:
            print("Insufficient balance")


# 代理處理類別
class BankAccountProxy(BankAccount):
    def __init__(self, user_role, initial_balance):
        # 用戶角色
        self.user_role = user_role
        # 實際處理類別實例
        self.real_bank_account = RealBankAccount(initial_balance)

    def deposit(self, amount):
        # 攔截指向實際處理類別實例的請求並進行相關檢查
        if self.user_role == "Admin" or self.user_role == "User":
            self.real_bank_account.deposit(amount)
        else:
            print("Unauthorized access")

    def withdraw(self, amount):
        # 攔截指向實際處理類別實例的請求並進行相關檢查
        if self.user_role == "Admin":
            self.real_bank_account.withdraw(amount)
        else:
            print("Unauthorized access")


def main():
    admin_account = BankAccountProxy("Admin", 1000)
    admin_account.deposit(500)
    admin_account.withdraw(200)

    user_account = BankAccountProxy("User", 1000)
    user_account.deposit(500)
    # 這個請求會被攔截
    user_account.withdraw(200)


if __name__ == "__main__":
    main()
