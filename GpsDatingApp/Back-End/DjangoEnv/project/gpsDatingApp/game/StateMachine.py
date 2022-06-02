# Interface

'''
為了解決 circular import，
py 可以透過不設置型態提示解決 circular import，
但為了代碼可讀與一致性，
透過將 type 設置為 StateMachine Interface 解決。
'''

from abc import ABCMeta

class StateMachine(metaclass=ABCMeta):
    pass
