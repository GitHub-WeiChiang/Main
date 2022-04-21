__author__ = "ChiangWei"
__date__ = "2022/04/21"

def accountNumber(name: str) -> int:
    users = [(1234, 'Justin'), (5678, 'Monica')]
    for acc_num, acc_name in users:
        if name == acc_name:
            return acc_num
    return None

