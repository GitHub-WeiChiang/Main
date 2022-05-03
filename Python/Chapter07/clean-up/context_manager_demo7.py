__author__ = "ChiangWei"
__date__ = "2022/05/03"

from contextlib import closing

class Some:
    def __init__(self, name: str) -> None:
        self.name = name

    def close(self):
        print(self.name, 'is closed.')

with closing(Some('Resource')) as res:
    print(res.name)
