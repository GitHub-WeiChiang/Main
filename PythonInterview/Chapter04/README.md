Chapter04 Python 序列
=====
* ### 字典中的元素如何排序 ?
    ```
    # sorted 默認升冪排序，透過 reverse=True 可設定為降冪

    def sort_by_key(dt: dict) -> list:
        return sorted(dt.items(), key=lambda d: d[0])


    def sort_by_value(dt: dict) -> list:
        return sorted(dt.items(), key=lambda d: d[1])


    if __name__ == '__main__':
        print(sort_by_key({"a": 3, "b": 2, "c": 1}))
        print(sort_by_value({"a": 3, "b": 2, "c": 1}))
        # [('a', 3), ('b', 2), ('c', 1)]
        # [('c', 1), ('b', 2), ('a', 3)]
    ```
* ### 如何進行倒序排序 ?
    ```
    import operator


    class Member:
        def __init__(self, name, age):
            self.name = name
            self.age = age

        def __str__(self):
            return self.name + ", " + str(self.age)


    if __name__ == '__main__':
        member1 = Member("A", 3)
        member2 = Member("B", 2)
        member3 = Member("C", 1)

        mem_list = [member1, member2, member3]

        mem_list.sort(key=operator.attrgetter('age'), reverse=True)
        for i in mem_list:
            print(i)

        print()

        mem_list = sorted(mem_list, key=operator.attrgetter('name'), reverse=True)
        for i in mem_list:
            print(i)
    ```
* ### 列表如何進行升冪或是降冪排列 ?
    ```
    if __name__ == '__main__':
        member_list: list = [
            {"name": "A", "age": 3},
            {"name": "B", "age": 2},
            {"name": "C", "age": 1}
        ]

        # 升冪
        member_list.sort(key=lambda d: d["age"])
        print(member_list)
        # 降冪
        member_list.sort(key=lambda d: d["age"], reverse=True)
        print(member_list)

        # 升冪
        member_list = sorted(member_list, key=lambda d: d["name"])
        print(member_list)
        # 降冪
        member_list = sorted(member_list, key=lambda d: d["name"], reverse=True)
        print(member_list)
    ```
* ### 如何對列表元素進行隨機排序 ?
    ```
    import random

    if __name__ == '__main__':
        poker = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        random.shuffle(poker)
        print(poker)
    ```
* ### 如何快速調換字典中的 key 和 value ?
    ```
    if __name__ == '__main__':
        poker = {
            "A": 0,
            "B": 1,
            "C": 2
        }

        poker = {value: key for key, value in poker.items()}
        print(poker)
    ```
<br />
