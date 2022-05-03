__author__ = "ChiangWei"
__date__ = "2022/05/03"

def a():
    text = None
    return text.upper()

def b():
    a()

def c():
    b()

try:
    c()
except:
    import traceback
    traceback.print_exc()
