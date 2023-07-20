3 - 排序算法
=====
* ### 插入排序 Insertion Sort
    * ### ![image](https://raw.githubusercontent.com/GitHub-WeiChiang/main/master/DataStructuresAndAlgorithms/Basic/3/InsertionSort.gif)
    * ### 从前到后依次处理未排好序的元素，对于每个元素，将它与之前排好序的元素进行比较，找到对应的位置后并插入。
    * ### 本质上，对于每一个要被处理的元素，只关心它与之前元素的关系，当前元素之后的元素在下一轮才會被处理。
    ```
    def sort(arr: list):
        for i in range(len(arr)):
            for j in range(i, 0, -1):
                if arr[j] < arr[j - 1]:
                    arr[j], arr[j - 1] = arr[j - 1], arr[j]
                    continue
                break

    if __name__ == '__main__':
        array: list = [1, 5, 3, 8, 9, 6, 7, 2, 4, 0]

        sort(array)

        print(array)
    ```
    * ### 复杂度分析
        * ### 时间复杂度: O(n ^ 2)
        * ### 空间复杂度: O(1)
* ### 快排 QuickSort
    * ### ![image](https://raw.githubusercontent.com/GitHub-WeiChiang/main/master/DataStructuresAndAlgorithms/Basic/3/QuickSort.png)
    * ### 选取一个目标元素，将目标元素放到数组中正确的位置，根据排好序后的元素，将数组切分为两个子数组，用相同的方法，在没有排好序的范围使用相同的操作。
    ```
    def sort(arr: list) -> list:
        if (l := len(arr)) <= 1:
            return arr

        lef: list = list()
        rig: list = list()

        for i in range(1, l):
            if arr[i] < arr[0]:
                lef.append(arr[i])
            else:
                rig.append(arr[i])

        return sort(lef) + [arr[0]] + sort(rig)


    if __name__ == '__main__':
        array: list = [1, 5, 3, 8, 9, 6, 7, 2, 4, 0]

        array = sort(array)

        print(array)
    ```
    ```
    def partition(arr: list, s: int, e: int) -> int:
        piv_ind: int = s

        for i in range(s, e):
            if arr[i] < arr[e]:
                arr[i], arr[piv_ind] = arr[piv_ind], arr[i]
                piv_ind += 1

        arr[piv_ind], arr[e] = arr[e], arr[piv_ind]

        return piv_ind


    def sort(arr: list, s: int, e: int):
        if s < e:
            piv_ind: int = partition(arr, s, e)
            sort(arr, s, piv_ind - 1)
            sort(arr, piv_ind + 1, e)


    if __name__ == '__main__':
        array: list = [1, 5, 3, 8, 9, 6, 7, 2, 4, 0]

        sort(array, 0, len(array) - 1)

        print(array)
    ```
    * ### 复杂度分析
        * ### 时间复杂度: O(n ^ 2); 平均时间复杂度: O(n log n)。
        * ### 空间复杂度: O(n); 平均空间复杂度: O(log n)。
* ### 归并排序 MergeSort
    * ### ![image](https://raw.githubusercontent.com/GitHub-WeiChiang/main/master/DataStructuresAndAlgorithms/Basic/3/MergeSort.png)
    * ### 将一个数组分为两个子数组，通过递归重复将数组切分到只剩下一个元素为止。
    * ### 后将每个子数组中的元素排序后合并，通过不断合并子数组，最后取得一个排好序的数组。
    ```
    def merge(lef: list, rig: list) -> list:
        res: list = list()

        while lef and rig:
            res.append(lef.pop(0) if lef[0] < rig[0] else rig.pop(0))

        return res + (lef or rig)


    def sort(arr: list) -> list:
        if (l := len(arr)) <= 1:
            return arr

        mid_ind: int = l // 2

        return merge(sort(arr[:mid_ind]), sort(arr[mid_ind:]))


    if __name__ == '__main__':
        array: list = [1, 5, 3, 8, 9, 6, 7, 2, 4, 0]

        array = sort(array)

        print(array)
    ```
    * ### 复杂度分析
        * ### 时间复杂度: O(n log n)
        * ### 空间复杂度: O(n)
<br />
