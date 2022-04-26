__author__ = "ChiangWei"
__date__ = "2022/04/21"

from typing import Tuple
from typing import overload

@overload
def account(name: str) -> Tuple[str, float]:
    pass

@overload
def account(name: str, balance: float) -> Tuple[str, float]:
    pass

def account(name, balance = 0):
    return (name, balance)

acct1 = account('Justin')
acct2 = account('Monica', 1000)

print(acct1)
print(acct2)