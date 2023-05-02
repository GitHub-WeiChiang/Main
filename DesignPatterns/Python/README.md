設計模式
=====
* ### 監聽模式 (Observer Pattern)
* ### 狀態模式 (State Pattern)
* ### 仲介模式 (Mediator Pattern)
* ### 裝飾模式 (Decorator Pattern)
* ### 單例模式 (Singleton Pattern)
* ### 克隆模式 (Clone Pattern)
* ### 命令模式 (Command Pattern)
* ### 職責模式 (Chain of Responsibility Pattern)
* ### 代理模式 (Proxy Pattern)
* ### 面板模式 (Facade Pattern)
* ### 反覆運算模式 (Iterator Pattern)
* ### 組合模式 (Composite Pattern)
* ### 構建模式 (Builder Pattern)
* ### 適配模式 (Wrapper Pattern)
* ### 策略模式 (Strategy Pattern)
* ### 工廠模式 (Factory Pattern)
* ### 備忘模式 (Memento Pattern)
* ### 享元模式 (Flyweight Pattern)
* ### 存取模式 (Visitor Pattern)
* ### 範本模式 (Template Method Pattern)
* ### 橋接模式 (Bridge Pattern)
* ### 解釋模式 (Interpreter Pattern)
* ### 其它 (Other)
<br />

補充
=====
* ### 關聯 (Association): ClassA 中並沒有資料型態為 ClassB 的屬性，但有使用到 ClassB 的屬性或方法。
* ### 聚合 (Aggregation): ClassA 中有資料型態為 ClassB 的屬性，但其 ClassB 的實例是從外部取得，非內部生成。
* ### 組合 (Composition): ClassA 中有資料型態為 ClassB 的屬性，且為 ClassA 自己內部生成，也就是說，當 ClassA 消失時，ClassB 也會不見。
* ### Python3 中所有類別都繼承 object 類別。
* ### 存取權限
	* ### \_\_foo\_\_: 定義的是特殊方法，一般是系統定義名字，類似 \_\_init\_\_()。
	* ### \_foo: 以單底線開頭時表示的是 protected 類型的變數，即保護類型只允許其本身與子類別進行存取，不能用於 from module import *。
	* ### \_\_foo: 以雙底線開頭時，表示的是私有類型 (private) 的變數，即只允許這個類別本身進行存取。
* ### \_\_new\_\_: 負責物件的創建，是一個類別方法。
* ### \_\_init\_\_: 負責物件初始化，是一個物件方法。
* ### \_\_call\_\_: 聲明這個類別的物件是可呼叫的 (callable)，是一個物件方法。
* ### 創建物件時，先呼叫 \_\_new\_\_ 方法，才呼叫 \_\_init\_\_ 方法。
* ### \_\_new\_\_ 是構造函數，需要返回一個實例。
* ### \_\_init\_\_ 不允許有返回值。
* ### \_\_init\_\_ 的參數除 self 外需與 \_\_new\_\_ 除 cls 外其餘參數一致或等效。
* ### type()
	* ### 查看變數或物件的類型。
	* ### 創建一個 (class)。
		```
		ClassVaribale = type('ClassA', (object, ), dict(name = "type test"))
		a = ClassVaribale()
		print(type(a))
		print(a.name)
		```
* ### 在 Python 中一切都是物件，類是元類 metaclass 的一個實例。
	* ### obj (is instance of) class (is instance of) metaclass。
* ### type 與 object 的關係
	* ### type 是一個 metaclass，而且是一個默認的 metaclass。也就是說，type 是 object 的類型，object 是 type 的一個實例。
	* ### type 是 object 的一個子類，繼承 object 的所有屬性和行為。
	* ### type 還是一個 callable，即實現了 \_\_call\_\_ 方法，可以當成一個函數來使用。
	* ### ![image](https://raw.githubusercontent.com/GitHub-WeiChiang/main/master/DesignPatterns/Python/type%20%E8%88%87%20object%20%E7%9A%84%E9%97%9C%E4%BF%82.jpg)
* ### 物件的創建過程
	* ### metaclass.\_\_init\_\_ 進行一些初始化的操作 (如全域變數的初始化)。
	* ### metaclass.\_\_call\_\_ 創建實例，在創建的過程中會呼叫 class 的 \_\_new\_\_ 和 \_\_init\_\_ 方法。
	* ### class.\_\_new\_\_ 進行具體的產生實體操作，並返回一個實例物件 obj。
	* ### class.\_\_init\_\_ 對返回的實例物件 obj 進行初始化，如一些狀態和屬性的設置。
	* ### 返回一個使用者真正需要使用的物件 obj。
	* ### ![image](https://raw.githubusercontent.com/GitHub-WeiChiang/main/master/DesignPatterns/Python/%E7%89%A9%E4%BB%B6%E7%9A%84%E5%89%B5%E5%BB%BA%E9%81%8E%E7%A8%8B.jpg)
* ### 篩檢程式模式
* ### 物件集區技術
* ### 回檔機制
* ### MVC 模式
* ### SOLID 原則
	* ### 單一職責原則 Single Responsibility Principle: A class should have only one reason to change.
		```
		class TerrestrialAnimal():
			def __init__(self, name):
				self.__name = name

			def running(self):
				print(self.__name + "在路上跑...")

		class AquaticAnimal():
			def __init__(self, name):
				self.__name = name

			def swimming(self):
				print(self.__name + "在水裡游...")
		```
	* ### 開放封閉原則 Open Close Principle: Software entities (classes, modules, functions, etc.) should be open for extension, but closed for modification.
		```
		from abc import ABCMeta, abstractmethod

		class Animal(metaclass=ABCMeta):
			def __init__(self, name):
			self._name = name

			@abstractmethod
			def moving(self):
				pass

		class TerrestrialAnimal(Animal):
			def __init__(self, name):
				super().__init__(name)

			def moving(self):
				print(self._name + "在路上跑...")

		class AquaticAnimal(Animal):
			def __init__(self, name):
				super().__init__(name)

			def moving(self):
				print(self._name + "在水裡游...")

		class BirdAnimal(Animal):
			def __init__(self, name):
				super().__init__(name)

			def moving(self):
				print(self._name + "在天空飛...")

		class Zoo:
			def __init__(self):
				self.__animals =[]

			def addAnimal(self, animal):
				self.__animals.append(animal)

			def displayActivity(self):
				print("觀察每一種動物的活動方式:")
				for animal in self.__animals:
					animal.moving()
		```
	* ### 里氏替換原則 Liskov Substitution Principle: Functions that use pointers to base classes must be able to use objects of derived classes without knowing it.
		```
		class Monkey(TerrestrialAnimal):
			def __init__(self, name):
				super().__init__(name)

			def climbing(self):
				print(self._name + "在爬樹，動作靈活輕盈...")

		class Zoo:
			def __init__(self):
				self.__animals =[]

			def addAnimal(self, animal):
				self.__animals.append(animal)

			def displayActivity(self):
				print("觀察每一種動物的活動方式:")
				for animal in self.__animals:
					animal.moving()

			def monkeyClimbing(self, monkey):
				monkey.climbing()
		```
	* ### 介面隔離原則 Interface Segregation Principle: Clients should not be forced to depend upon interfaces that they don't use. Instead of one fat interface many small interfaces are preferred based on groups of methods, each one serving one submodule.
		```
		from abc import ABCMeta, abstractmethod
		
		class Animal(metaclass=ABCMeta):
			def __init__(self, name):
				self._name = name

			def getName(self):
				return self._name

			@abstractmethod
			def feature(self):
				pass

			@abstractmethod
			def moving(self):
				pass

		class IRunnable(metaclass=ABCMeta):
			@abstractmethod
			def running(self):
				pass

		class IFlyable(metaclass=ABCMeta):
			@abstractmethod
			def flying(self):
				pass

		class INatatory(metaclass=ABCMeta):
			@abstractmethod
			def swimming(self):
				pass

		class MammalAnimal(Animal, IRunnable):
			def __init__(self, name):
				super().__init__(name)

			def feature(self):
				print(self._name + "的生理特徵：恆溫，胎生，哺乳。")

			def running(self):
				print("在陸上跑...")

			def moving(self):
				print(self._name + "的活動方式：", end="")
				self.running()

		class BirdAnimal(Animal, IFlyable):
			def __init__(self, name):
				super().__init__(name)

			def feature(self):
				print(self._name + "的生理特徵：恆溫，卵生，前肢成翅。")

			def flying(self):
				print("在天空飛...")

			def moving(self):
				print(self._name + "的活動方式：", end="")
				self.flying()

		class FishAnimal(Animal, INatatory):
			def __init__(self, name):
				super().__init__(name)

			def feature(self):
				print(self._name + "的生理特徵：流線型體型，用鰓呼吸。")

			def swimming(self):
				print("在水里遊...")

			def moving(self):
				print(self._name + "的活動方式：", end="")
				self.swimming()

		class Bat(MammalAnimal, IFlyable):
			def __init__(self, name):
				super().__init__(name)

			def running(self):
				print("行走功能已經退化。")

			def flying(self):
				print("在天空飛...", end="")

			def moving(self):
				print(self._name + "的活動方式：", end="")
				self.flying()
				self.running()

		class Swan(BirdAnimal, IRunnable, INatatory):
			def __init__(self, name):
				super().__init__(name)

			def running(self):
				print("在陸上跑...", end="")

			def swimming(self):
				print("在水里游...", end="")

			def moving(self):
				print(self._name + "的活動方式：", end="")
				self.running()
				self.swimming()
				self.flying()

		class CrucianCarp(FishAnimal):
			def __init__(self, name):
				super().__init__(name)
		```
	* ### 依賴倒置原則 Dependence Inversion Principle: High level modules should not depend on low level modules; both should depend on abstractions. Abstractions should not depend on details. Details should depend upon abstractions.
		```
		from abc import ABCMeta, abstractmethod
		
		class Animal(metaclass=ABCMeta):
			def __init__(self, name):
				self._name = name

			def eat(self, food):
				if(self.checkFood(food)):
					print(self._name + "進食" + food.getName())
				else:
					print(self._name + "不吃" + food.getName())

			@abstractmethod
			def checkFood(self, food):
				pass

		class Dog(Animal):
			def __init__(self):
				super().__init__("狗")

			def checkFood(self, food):
				return food.category() == "肉類"

		class Swallow(Animal):
			def __init__(self):
				super().__init__("燕子")

			def checkFood(self, food):
				return food.category() == "昆蟲"

		class Food(metaclass=ABCMeta):
			def __init__(self, name):
				self._name = name

			def getName(self):
				return self._name

			@abstractmethod
			def category(self):
				pass

			@abstractmethod
			def nutrient(self):
				pass

		class Meat(Food):
			def __init__(self):
				super().__init__("肉")

			def category(self):
				return "肉類"

			def nutrient(self):
				return "蛋白質、脂肪"

		class Worm(Food):
			def __init__(self):
				super().__init__("蟲")

			def category(self):
				return "昆蟲"

			def nutrient(self):
				return "蛋白質、微量元素"
		```
* ### LoD (Law of Demeter) 原則: Each unit should have only limited knowledge about other units: only units "closely" related to the current unit. Only talk to your immediate friends, don't talk to strangers.
* ### KISS (Keep It Simple and Stupid) 原則: Keep It Simple and Stupid.
* ### DRY (Don't Repeat Yourself) 原則: .
* ### YAGNI (You Aren't Gonna Need It) 原則: You aren't gonna need it, don't implement something until it is necessary.
* ### Rule Of Three 原則。
* ### CQS (Command - Query Separation) 原則。
* ### 重構與重寫不同。
* ### 重構原因: 程式碼重複、結構混亂、無擴展性、強耦合、性能低。
* ### 重構時機: 新增功能與錯誤修補時。
* ### 重構方式: 重命名、函數重構、重新組織資料結構、設計模式導入。
* ### 開發軟體最怕的不是 "寫程式" 或是 "不會寫程式 (寫不出程式)"，最怕的是 "改程式 (改那些原本已經寫好測試過可以動的程式)"。
* ### 最害怕 "A single change to a program results in a cascade of changes to dependent modules."
* ### 功能的新增，應該是通過添加新的程式碼實現，而不是透過改變正在運行的程式碼來達成。
<br />

Reference
=====
* ### Python 設計模式
