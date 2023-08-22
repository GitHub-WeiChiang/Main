"""
輸入格式:
1. 第一行包含一個唯一整數 n
2. 接下來的 3 * n 行，每行包含 n 個被空格分隔的整數 (代表三個 n * n 矩陣)

算法目的:
1. 測試矩陣 A * B 的結果是否等於矩陣 C

時間複雜度:
1. 矩陣乘法: O(n ^ 3)
2. Freivalds 算法: O(n ^ 2)

Freivalds 算法基本思想:
1. 假設要判斷矩陣 A、B、C 是否滿足 AB = C
2. 隨機生成一個向量 x，此向量的維度與矩陣 C 的列數相同
3. 計算向量 y = A(Bx) - Cx
4. 檢查向量 y 是否全為零，如果 y 全為零，則認為 AB = C，反之則認為 AB != C。
"""

from typing import Optional
from sys import stdin
from random import randint

n: Optional[int] = None


def read_int() -> int:
    return int(stdin.readline())


def read_array() -> list:
    return list(map(int, stdin.readline().split()))


def read_matrix() -> list:
    m: list = []

    for _ in range(n):
        row: list = read_array()
        assert len(row) == n
        m.append(row)

    return m


def mult(matrix: list, x: list) -> list:
    return [sum(matrix[i][j] * x[j] for j in range(n)) for i in range(n)]


def freivalds(matrix_0: list, matrix_1: list, matrix_2: list) -> bool:
    x: list = [randint(0, 9) for _ in range(n)]

    return mult(matrix_0, mult(matrix_1, x)) == mult(matrix_2, x)


if __name__ == '__main__':
    n = read_int()

    A: list = read_matrix()
    B: list = read_matrix()
    C: list = read_matrix()

    print(freivalds(A, B, C))
