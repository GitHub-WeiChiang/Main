AsyncioPrinciples
=====
* ### 神器篇: Python 面向對象編程 OOP 寫類神器 attrs (好像懂了又好像不懂)
* ### 海象篇: 賦值表達式 Assignment Expressions 之海象運算符 (:= 像海象對吧 ?)
* ### Chapter01 簡介 Asyncio
* ### Chapter02 Thread 的真相
* ### Chapter03 盤點 Asyncio
* ### Chapter04 20 個沒用過的 Asyncio 程式庫
<br />

神器篇: Python 面向對象編程 OOP 寫類神器 attrs (好像懂了又好像不懂)
=====
* ### attrs 是这样的一个 Python 工具包，它能将你从繁综复杂的实现上解脱出来，享受编写 Python 类的快乐。它的目标就是在不减慢你编程速度的前提下，帮助你来编写简洁而又正确的代码。
    ```
    from attr import attrs, attrib, fields


    @attrs
    class Person:
        name = attrib(type=str, default="")
        age = attrib(type=int, default=0)
        sex = attrib(type=str, default="")


    if __name__ == '__main__':
        first_person = Person("John", 18, "M")
        print(first_person)


    # Person(name='John', age=18, sex='M')
    ```
* ### 主要作用
    * ### Person 这个类中三个属性都只写了一次，同时还指定了各个字段的类型和默认值，另外也不需要再定义 init 方法和 repr 方法，非常简洁。
    * ### 实际上，主要是 attrs 这个修饰符起了作用，然后根据定义的 attrib 属性自动帮我们实现了 init、repr、eq、ne、lt、le、gt、ge、hash 这几个方法。
* ### 深入了解
    ```
    if __name__ == '__main__':
        first_person = Person("John", 18, "M")
        second_person = Person("Nancy", 16, "F")

        print('Equal:', first_person == second_person)
        print('Not Equal(ne):', first_person != second_person)
        print('Less Than(lt):', first_person.age < second_person.age)
        print('Less or Equal(le):', first_person.age <= second_person.age)
        print('Greater Than(gt):', first_person.age > second_person.age)
        print('Greater or Equal(ge):', first_person.age >= second_person.age)
    
    # Equal: False
    # Not Equal(ne): True
    # Less Than(lt): False
    # Less or Equal(le): False
    # Greater Than(gt): True
    # Greater or Equal(ge): True
    ```
* ### 属性定义
    ```
    if __name__ == '__main__':
        # 查看可传入参数
        print(fields(Person))
    ```
    | 主要參數 | 解釋 |
    | --- | --- |
    | default | 属性的默认值 |
    | type | 类型 |
    | init | 是否参与初始化 |
    | kw_only | 是否为强制关键字参数 |
    | validator | 验证器 |
    | converter | 转换器 |
* ### 初始化 (默认是 True): 如果一个类的某些属性不想参与初始化，比如想直接设置一个初始值，一直固定不变，可以将属性的 init 参数设置为 False。
    ```
    from attr import attrs, attrib


    @attrs
    class Person:
        name = attrib(type=str)
        age = attrib(init=False)
        sex = attrib(type=str)


    first = Person("John", "M")
    second = Person(name="Mike", age=89, sex="M")


    # TypeError: Person.__init__() got an unexpected keyword argument 'age'
    ```
* ### 强制关键字 (默认为 False): 强制关键字是 Python 里面的一个特性，在传入的时候必须使用关键字的名字来传入，设置了强制关键字参数的属性必须要放在后面，之后面不能再有非强制关键字参数的属性。
    ```
    from attr import attrs, attrib


    @attrs
    class Person:
        name = attrib(type=str)
        age = attrib(type=int)
        sex = attrib(kw_only=True)


    first = Person("John", 18, sex="M")
    second = Person("John", 18, "M")


    # TypeError: Person.__init__() takes 3 positional arguments but 4 were given
    ```
* ### 验证器: 有时在设置一个属性必须满足某个条件，对于这种情况，可以使用验证器来控制某些属性不能为非法值。
    ```
    from attr import attrs, attrib


    def is_valid_gender(instance, attribute, value):
        """
        :param instance:
            类对象
        :param attribute:
            属性名
        :param value:
            属性值
        """

        if value not in ('M', 'F'):
            #  Validator 里面不應該是返回 True 或 False，一定要在 Validator 里面 raise 某个错误。
            raise ValueError(f'gender {value} is not valid')


    @attrs
    class Person:
        name = attrib(type=str)
        age = attrib(type=int)
        sex = attrib(validator=is_valid_gender)


    if __name__ == '__main__':
        first = Person("John", 18, "M")
        second = Person("Ann", 29, "X")

    
    # ValueError: gender X is not valid
    ```
    * ### attrs 库里中内置了許多 Validator，比如类型判断，當规定 age 必须为 int 类型時:
        ```
        age = attrib(validator=validators.instance_of(int))
        ```
    * ### validator 参数支持多个 Validator 設定:
        ```
        from attr import attrs, attrib, validators


        def is_valid_gender(instance, attribute, value):
            if value not in ('M', 'F'):
                raise ValueError(f'gender {value} is not valid')


        def is_less_than_100(instance, attribute, value):
            if value > 100:
                raise ValueError(f'age {value} must less than 100')


        @attrs
        class Person:
            name = attrib(type=str)
            age = attrib(validator=[validators.instance_of(int), is_less_than_100])
            sex = attrib(validator=[validators.instance_of(str), is_valid_gender])
        ```
* ### 转换器: 很多时候会不小心传入一些形式不太标准的參數型態，比如本来是 int 类型的 100 卻传入了字符串类型的 "100"，為了避免噴錯，可以设置一些转换器来增强容错机制。
    ```
    from attr import attrs, attrib, validators


    def to_int(value):
        try:
            return int(value)
        except ValueError:
            return 0


    @attrs
    class Person:
        name = attrib(type=str)
        age = attrib(converter=to_int)
        sex = attrib(validator=validators.instance_of(str))


    last_person = Person("haha", "35", "M")
    ```
<br />

海象篇: 賦值表達式 Assignment Expressions 之海象運算符 (:= 像海象對吧 ?)
=====
```
import re
import io

# Example 1:
a = [0] * 100
if len(a) > 10:
  print(f"List is too long ({len(a)} elements, expected <= 10)")
 
n = len(a)
if n > 10:
  print(f"List is too long ({n} elements, expected <= 10)")
 
if (x := len(a)) > 10:
  print(f"List is too long ({x} elements, expected <= 10)")
 
# Example 2, bad
ads = "Now 20% off till 6/18"
 
m1 = re.search(r'(\d+)% off', ads)
discount1 = float(m1.group(1)) / 100 if m1 else 0.0
 
discount2 = float(m2.group(1)) / 100 if (m2 := re.search(r'(\d+)% off', ads)) else 0.0
 
print(f'{discount1 = }, {discount2 = }')
 
# Example 3
f1 = io.StringIO("123456789")
x1 = f1.read(4)
while x1 != '':
  print(x1)
  x1 = f1.read(4)
 
f2 = io.StringIO("123456789")
while (x2 := f2.read(4)) != '':
  print(x2)
 
# Example 4
prog_langs = {'c++', 'python', 'java'}
langs = ['C++', 'Java', 'PYthon', 'English', '中文']
 
l1 = [lang.lower() for lang in langs if lang.lower() in prog_langs]
print(l1)
 
l2 = [l for lang in langs if (l := lang.lower()) in prog_langs]
print(l2)
```
* ### 海象运算符 ```:=``` 作为一项新奇的 python 语法，在最新发布的 python3.8 中被首次提出来。
* ### 海象运算符即一个变量名后跟一个表达式或者一个值，这个和赋值运算符 = 类似，可以看作是一种新的赋值运算符。
* ### 在合适的场景中使用海象运算符可以降低程序复杂性，简化代码。一方面，可以写出优雅而简洁的 Python 代码；另一方面，可以看懂他人的代码。在一些实例中，甚至可以提高程序的性能。
```
a = 0
if a < 15:
　　print("hello, walrus operator！")

# vs.

if a := 15 > 10:
    print("hello, walrus operator！")
```
```
count = 5
while count:
　　print("hello, walrus operator！")
　　count -= 1

# vs.

count = 5
# 需要加 1 是因为执行输出前 count 就减 1 了
while (count := count - 1) + 1:
　　print("hello, walrus operator！")
```
```
nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
count = 1
def f(x):
　　global count
　　print(f"f(x)函数运行了{count}次")
　　count += 1
　　return x ** 2
nums2 = [f(i) for i in nums1 if f(i) > 50]
print(nums2)

# vs.

nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
count = 1
def f(x):
　　global count
　　print(f"f(x)函数运行了{count}次")
　　count += 1
　　return x ** 2
nums2 = [j for i in nums1 if (j := f(i)) > 50]
print(nums2)
```
* ### 使用海象运算符时: 三个数字满足列表推导式的条件，节省 3 次的函数调用。当程序数据巨大的时候，这将起到提升性能的作用。
<br />

Reference
=====
* ### Python 非同步設計：使用 Asyncio
