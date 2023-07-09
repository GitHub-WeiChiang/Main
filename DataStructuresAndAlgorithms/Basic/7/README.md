7 - 树和二分查找树 (Tree & Binary Search Tree)
=====
* ### 树的基本概念
    * ### ![image](https://raw.githubusercontent.com/GitHub-WeiChiang/main/master/DataStructuresAndAlgorithms/Basic/7/Tree.jpg)
    * ### 节点的高度 (height): 意味着此节点到尾节点之间相连线的数量，B 的高度就是 2，因为 B 到尾节点 H 之间的 edge 数量为 2。
    * ### 节点的深度 (depth)，意味着此节点到根节点的 edge 数量，D 的深度是 2，因为 D 到根节点 A 之间的 edge 数量是 2。
* ### 树的种类
    * ### 二叉树 (Binary Tree): 每个节点最多含有两个子节点，上面图示中的树就是二叉树。
    * ### 满二叉树 (Full Binary Tee): 在满二叉树中，每个不是尾节点的节点都有两个子节点。
    * ### 完全二叉树 (Complete Binary Tree): 假设一个二叉树深度 (depth) 为d (d > 1)，除了第 d 层外，其它各层的节点数量均已达到最大值，且第 d 层所有节点从左向右紧密排列，这样的二叉树就是完全二叉树。
    * ### 排序二叉树 (Binary Search Tree): 在此树中，每个节点的数值比左子树上的每个节点都大，比所有右子树上的节点都小。
    * ### 平衡二叉树 (AVL Tree): 任何节点的两颗子树的高度差不大于 1 的二叉树。
    * ### B 树 (B - Tree): B 树和平衡二插树一样，只不过它是一种多叉树 (一个节点的子节点数量可以超过二)。
    * ### 红黑树 (Red — Black Tree): 是一种自平衡二叉寻找树。
* ### 二分查找树 (Binary Search Tree) 的实现
    * ### 每个节点都比自己左子树上的节点大，并比右子树上的节点小。
    * ### 若想要寻找一个特定的元素，只需要依赖其特性，顺着特定的路径就能找到目标。
    * ### 在此树中，搜索、插入和删除的复杂度等于树高，往往就是 O(log n)，非常合适用来存储数据。
    ```
    from typing import Optional


    class TreeNode:
        def __init__(self, value: int):
            self.value: int = value
            self.left: Optional[TreeNode] = None
            self.right: Optional[TreeNode] = None


    class BST:
        def __init__(self):
            self.root: Optional[TreeNode] = None

        def get(self, key: int) -> TreeNode:
            current: TreeNode = self.root

            while current is not None and current.value != key:
                if key < current.value:
                    current = current.left
                    continue

                if key > current.value:
                    current = current.right
                    continue

            return None if current is None else current

        def insert(self, key: int):
            if self.root is None:
                self.root = TreeNode(key)
                return

            parent: TreeNode = self.root

            while True:
                if key < parent.value:
                    if parent.left is None:
                        parent.left = TreeNode(key)
                        return

                    parent = parent.left
                elif key > parent.value:
                    if parent.right is None:
                        parent.right = TreeNode(key)
                        return

                    parent = parent.right
                else:
                    # BTS does not allow nodes with the same value.
                    return

        def delete(self, key: int) -> bool:
            parent: TreeNode = self.root
            current: TreeNode = self.root

            is_left_child: bool = False

            while current is not None and current.value != key:
                parent = current

                if key < current.value:
                    current = current.left
                    is_left_child = True
                    continue

                if key > current.value:
                    current = current.right
                    is_left_child = False
                    continue

            if current is None:
                return False

            # Case 1: If node to be deleted has only one child.
            if current.left is None and current.right is None:
                if current == self.root:
                    self.root = None
                elif is_left_child:
                    parent.left = None
                else:
                    parent.right = None
            # Case 2: If node to be deleted has only one child.
            elif current.right is None:
                if current is self.root:
                    self.root = current.left
                elif is_left_child:
                    parent.left = current.left
                else:
                    parent.right = current.left
            elif current.left is None:
                if current is self.root:
                    self.root = current.right
                elif is_left_child:
                    parent.left = current.right
                else:
                    parent.right = current.right
            # Case 3: If current.left is not None and current.right is not None.
            else:
                successor: TreeNode = self.get_successor(current)

                if current is self.root:
                    self.root = successor
                elif is_left_child:
                    parent.left = successor
                else:
                    parent.right = successor

                successor.left = current.left

            return True

        @staticmethod
        def get_successor(node: TreeNode) -> TreeNode:
            successor: Optional[TreeNode] = None
            successor_parent: Optional[TreeNode] = None

            current: TreeNode = node.right

            while current is not None:
                successor_parent = successor
                successor = current
                current = current.left

            if successor != node.right:
                successor_parent.left = successor.right
                successor.right = node.right

            return successor


    if __name__ == '__main__':
        bst: BST = BST()
        bst.insert(10)
        bst.insert(5)
        bst.insert(15)
        bst.insert(4)
        bst.insert(6)
        bst.insert(14)
        bst.insert(16)

        bst.delete(14)
    ```
* ### 树的遍历 Tree Traversal
    * ### 前序遍历 (Pre-order Traversal): 先访问节点自己，后访问左子树，再访问右子树。
    * ### 中序遍历 (In-order Traversal): 先访问左子树上的节点，再访问自己，后访问右子树上的节点。
    * ### 后序遍历 (Post-order Traversal): 先访问左右子树，后访问自己。
    * ### 註: 以自己為主，前序 (自 | 左右)、中序 (左 | 自 | 右)、后序 (左右 | 自)。
* ### 树的遍历实现
    ```
    def pre_order_traversal(root: TreeNode):
        if root is None:
            return

        print(root.value)
        pre_order_traversal(root.left)
        pre_order_traversal(root.right)


    def in_order_traversal(root: TreeNode):
        if root is None:
            return

        in_order_traversal(root.left)
        print(root.value)
        in_order_traversal(root.right)


    def post_order_traversal(root: TreeNode):
        if root is None:
            return

        post_order_traversal(root.left)
        post_order_traversal(root.right)
        print(root.value)
    ```
<br />
