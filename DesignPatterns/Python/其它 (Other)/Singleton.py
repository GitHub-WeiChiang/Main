__author__ = "ChiangWei"
__date__ = "2022/04/25"

import threading

# # Create singleton class with a decorator
# def singleton(cls, *args, **kwargs):
#     instance = None

#     def __singleton(*args, **kwargs):
#         nonlocal instance
#         if instance == None:
#             instance = cls(*args, **kwargs)
#         return instance

#     return __singleton

# Create singleton class with a decorator
def singleton(cls):
    lock = threading.Lock()
    instance = None

    def __singleton(*args, **kwargs):
        nonlocal lock
        nonlocal instance

        if instance is None:
            with lock:
                if instance is None:
                    instance = cls(*args, **kwargs)

        return instance
    return __singleton
   
@singleton
class Singleton:
    pass

SingletonA = Singleton()
SingletonB = Singleton()
print(SingletonA)
print(SingletonB)
print(SingletonA == SingletonB)
print(type(Singleton()))
