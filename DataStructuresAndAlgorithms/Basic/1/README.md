1 - 数据结构和算法简介: 二分查找
=====
* ### 二分查找應用
    * ### MySQL (InnoDB)
        * ### 在單頁中以主鍵尋找 (無建立索引): 二分搜尋定位槽，遍歷分組中記錄。
        * ### 在多頁中以主鍵尋找 (無建立索引): 二分搜尋定位頁，二分搜尋定位槽，遍歷分組中記錄。
* ### 優先佇列應用
    * ### 作業系統任務排程
* ### 二分搜索 (Binary Search)
    * ### 迴圈版
        ```
        def binary_search(arr: list, tar: int) -> int:
            lef_ind: int = 0
            rig_ind: int = len(arr) - 1

            while lef_ind <= rig_ind:
                mid_ind: int = (rig_ind - lef_ind) // 2 + lef_ind

                if arr[mid_ind] == tar:
                    return mid_ind

                if tar < arr[mid_ind]:
                    rig_ind = mid_ind - 1
                else:
                    lef_ind = mid_ind + 1

            return -1


        if __name__ == '__main__':
            array: list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

            print(binary_search(array, 2))
        ```
    * ### 遞迴版
        ```
        def binary_search(arr: list, tar: int, lef: int, rig: int) -> int:
            if lef > rig:
                return -1

            mid: int = lef + (rig - lef) // 2

            if arr[mid] == tar:
                return mid

            if tar < arr[mid]:
                return binary_search(arr, tar, lef, mid - 1)

            return binary_search(arr, tar, mid + 1, rig)


        if __name__ == '__main__':
            array: list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

            print(binary_search(array, 2, 0, 9))
        ```
* ### 算法复杂度分析
    * ### 最糟糕的情况下，需要将数组迭代切分到只有一个元素，假如数组有 n 个元素，切分的次数为 k，每次都切一半，也就是 n / (2 ^ k) = 1，转换公式为 2 ^ k = n，那么 k 就是 log n，所以时间复杂度为 O(log n)。
    * ### 註: log 以 2 為底。
    * ### 因为不需要额外的空间，所以空间复杂度为 O(1)。
<br />
