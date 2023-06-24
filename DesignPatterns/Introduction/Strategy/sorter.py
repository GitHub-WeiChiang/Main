from abc import ABC, abstractmethod

# 排序策略接口
class SortingStrategy(ABC):
    @abstractmethod
    def sort(self, data):
        pass

# 泡泡排序類別: 實作 SortingStrategy 接口
class BubbleSort(SortingStrategy):
    def sort(self, data):
        n = len(data)
        for i in range(n - 1):
            for j in range(n - i - 1):
                if data[j] > data[j + 1]:
                    data[j], data[j + 1] = data[j + 1], data[j]
        return data

# 快速排序類別: 實作 SortingStrategy 接口
class QuickSort(SortingStrategy):
    def sort(self, data):
        self.quick_sort(data, 0, len(data) - 1)
        return data

    def quick_sort(self, data, low, high):
        if low < high:
            pi = self.partition(data, low, high)
            self.quick_sort(data, low, pi - 1)
            self.quick_sort(data, pi + 1, high)

    def partition(self, data, low, high):
        pivot = data[high]
        i = (low - 1)
        for j in range(low, high):
            if data[j] < pivot:
                i += 1
                data[i], data[j] = data[j], data[i]
        data[i + 1], data[high] = data[high], data[i + 1]
        return i + 1

# 排序類別
class Sorter:
    def __init__(self, strategy):
        # 策略物件變數
        self.strategy = strategy

    def sort(self, data):
        return self.strategy.sort(data)

if __name__ == '__main__':
    # 待排序陣列
    data = [5, 2, 4, 1, 3]
    # 實例化排序類別: 傳入所需策略
    sorter = Sorter(BubbleSort())
    # 排序
    sorted_data = sorter.sort(data)
    # 打印
    print(f"BubbleSort result: {sorted_data}")

    # 示例 2
    data = [5, 2, 4, 1, 3]
    sorter = Sorter(QuickSort())
    sorted_data = sorter.sort(data)
    print(f"QuickSort result: {sorted_data}")
