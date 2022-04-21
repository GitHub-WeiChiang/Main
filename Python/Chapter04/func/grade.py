__author__ = "ChiangWei"
__date__ = "2022/04/21"

score = int(input('請輸入分數：'))
level = score // 10
{
    10: lambda: print('Perfect'),
    9: lambda: print('A'),
    8: lambda: print('B'),
    7: lambda: print('C'),
    6: lambda: print('D')
}.get(level, lambda: print('E'))()
# 最後的 () 表示為立即執行
