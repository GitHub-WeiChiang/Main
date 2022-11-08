__author__ = "ChiangWei"
__date__ = "2022/04/23"

# from abc import ABCMeta, abstractmethod

# class Water:
#     def __init__(self, state):
#         self.__temperature = 25
#         self.__state = state

#     def setState(self, state):
#         self.__state = state

#     def changeState(self, state):
#         if (self.__state):
#             print("由", self.__state.getName(), "變為", state.getName())
#         else:
#             print("初始化為", state.getName())

#         self.__state = state

#     def getTemperature(self):
#         return self.__temperature

#     def setTemperature(self, temperature):
#         self.__temperature = temperature

#         if (self.__temperature <= 0):
#             self.changeState(SolidState("固態"))
#         elif (self.__temperature <= 100):
#             self.changeState(LiquidState("液態"))
#         else:
#             self.changeState(GaseousState("氣態"))

#     def riseTemperature(self, step):
#         self.setTemperature(self.__temperature + step)

#     def reduceTemperature(self, step):
#         self.setTemperature(self.__temperature - step)

#     def behavior(self):
#         self.__state.behavior(self)

# class State(metaclass=ABCMeta):
#     def __init__(self, name):
#         self.__name = name

#     def getName(self):
#         return self.__name

#     @abstractmethod
#     def behavior(self, water):
#         pass

# class SolidState(State):
#     def __init__(self, name):
#         super().__init__(name)

#     def behavior(self, water):
#         print("我性格高冷，當前體溫" + str(water.getTemperature()) + "℃，我堅如鋼鐵，彷如一冷血動物，請用我砸人，嘿嘿……")

# class LiquidState(State):
#     def __init__(self, name):
#         super().__init__(name)

#     def behavior(self, water):
#         print("我性格溫和，當前體溫" + str(water.getTemperature()) + "℃，我可滋潤萬物，飲用我可讓你活力倍增……")

# class GaseousState(State):
#     def __init__(self, name):
#         super().__init__(name)

#     def behavior(self, water):
#         print("我性格熱烈，當前體溫" + str(water.getTemperature()) + "℃，飛向天空是我畢生的夢想，在這你將看不到我的存在，我將達到無我的境界……")

# water = Water(LiquidState("液态"))
# water.behavior()
# water.setTemperature(-4)
# water.behavior()
# water.riseTemperature(18)
# water.behavior()
# water.riseTemperature(110)
# water.behavior()

from abc import ABCMeta, abstractmethod

class Context(metaclass=ABCMeta):
    def __init__(self):
        self.__states = []
        self.__curState = None
        self.__stateInfo = 0

    def addState(self, state):
        if (state not in self.__states):
            self.__states.append(state)

    def changeState(self, state):
        if (state is None):
            return False
        if (self.__curState is None):
            print("初始化為", state.getName())
        else:
            print("由", self.__curState.getName(), "變為", state.getName())
        self.__curState = state
        self.addState(state)
        return True

    def getState(self):
        return self.__curState

    def _setStateInfo(self, stateInfo):
        self.__stateInfo = stateInfo
        for state in self.__states:
            if( state.isMatch(stateInfo) ):
                self.changeState(state)

    def _getStateInfo(self):
        return self.__stateInfo

class State:
    def __init__(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def isMatch(self, stateInfo):
        return False

    @abstractmethod
    def behavior(self, context):
        pass

class Water(Context):
    def __init__(self):
        super().__init__()
        self.addState(SolidState("固態"))
        self.addState(LiquidState("液態"))
        self.addState(GaseousState("氣態"))
        self.setTemperature(25)

    def getTemperature(self):
        return self._getStateInfo()

    def setTemperature(self, temperature):
        self._setStateInfo(temperature)

    def riseTemperature(self, step):
        self.setTemperature(self.getTemperature() + step)

    def reduceTemperature(self, step):
        self.setTemperature(self.getTemperature() - step)

    def behavior(self):
        state = self.getState()
        if(isinstance(state, State)):
            state.behavior(self)

def singleton(cls, *args, **kwargs):
    instance = {}

    def __singleton(*args, **kwargs):
        if cls not in instance:
            instance[cls] = cls(*args, **kwargs)
        return instance[cls]

    return __singleton

@singleton
class SolidState(State):
    def __init__(self, name):
        super().__init__(name)

    def isMatch(self, stateInfo):
        return stateInfo < 0

    def behavior(self, context):
        print("我性格高冷，當前體溫", context._getStateInfo(), "℃，我堅如鋼鐵，彷如一冷血動物，請用我砸人，嘿嘿……")

@singleton
class LiquidState(State):
    def __init__(self, name):
        super().__init__(name)

    def isMatch(self, stateInfo):
        return (stateInfo >= 0 and stateInfo < 100)

    def behavior(self, context):
        print("我性格溫和，當前體溫", context._getStateInfo(), "℃，我可滋潤萬物，飲用我可讓你活力倍增……")

@singleton
class GaseousState(State):
    def __init__(self, name):
        super().__init__(name)

    def isMatch(self, stateInfo):
        return stateInfo >= 100

    def behavior(self, context):
        print("我性格熱烈，當前體溫", context._getStateInfo(), "℃，飛向天空是我畢生的夢想，在這你將看不到我的存在，我將達到無我的境界……")

water = Water()
water.behavior()
water.setTemperature(-4)
water.behavior()
water.riseTemperature(18)
water.behavior()
water.riseTemperature(110)
water.behavior()
