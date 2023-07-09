9 - 图 Graph
=====
* ### 图的種類
    * ### 无向图 (Undirected Graph): 每个顶点和其它顶点通过相连线连接。
    * ### 有向图 (Directed Graph): 其相连线是有方向的。
    * ### 权重图 (Weighted Graph): 每条相连线有各自的权重。
* ### 有向图的实现 (Directed Graph)
    * ### 矩阵 (Matrix)
        * ### ![image](https://raw.githubusercontent.com/GitHub-WeiChiang/main/master/DataStructuresAndAlgorithms/Basic/9/Matrix.png)
        * ### 每行代表相应的顶点，若 M[i][j] = 1，就代表顶点 i 连向 j，其值若為 0，则表达顶点间没有联系。
        * ### 用矩阵的方式来实现图的优势是可以很快地判断两个顶点之间是否相连，但空间复杂度較高，需要 O(V ^ 2) 来记录所有的数据，不管顶点间是否相连线。
    * ### 链表 (List)
        * ### ![image](https://raw.githubusercontent.com/GitHub-WeiChiang/main/master/DataStructuresAndAlgorithms/Basic/9/List.png)
        * ### 链表实现中，实际上使用了储存链表的数组来表示图，图的左侧用数组来实现，代表所有顶点，而每个顶点含有一个链表，链表上储存了该顶点指向的顶点。
        ```
        from typing import List


        class ListGraph:
            def __init__(self, v: int):
                self.graphs: List[list] = [list()] * v

            def add_edge(self, start: int, end: int):
                self.graphs[start].append(end)

            def remove_edge(self, start: int, end: int):
                self.graphs[start].remove(end)
        ```
* ### 图的遍历 (Graph Traversal)
    * ### 深度优先搜索 (Depth-First Search)
    * ### 广度优先搜索 (Breadth-First Search)
* ### 深度优先搜索 (Depth-First Search)
    ```
    from typing import List, Optional


    class ListGraph:
        def __init__(self, v: int):
            self.graphs: List[list] = [list() for i in range(v)]

        def add_edge(self, start: int, end: int):
            self.graphs[start].append(end)

        def remove_edge(self, start: int, end: int):
            self.graphs[start].remove(end)


    class GraphTraversal:
        def __init__(self, graph: ListGraph):
            self.graph = graph
            self.visited: list[Optional[bool]] = [None] * len(self.graph.graphs)

        def dfs_traversal(self, v: int):
            if self.visited[v]:
                return

            self.visited[v] = True

            print(v)

            for i in self.graph.graphs[v]:
                if not self.visited[i]:
                    self.dfs_traversal(i)

        def dfs(self):
            self.dfs_traversal(0)


    if __name__ == '__main__':
        list_graph: ListGraph = ListGraph(5)
        list_graph.add_edge(0, 1)
        list_graph.add_edge(0, 2)
        list_graph.add_edge(1, 3)
        list_graph.add_edge(2, 3)
        list_graph.add_edge(3, 4)

        graph_traversal: GraphTraversal = GraphTraversal(list_graph)
        graph_traversal.dfs()
    ```
* ### 广度优先搜索 (Breadth-First Search)
    ```
    from queue import Queue
    from typing import List, Optional


    class ListGraph:
        def __init__(self, v: int):
            self.graphs: List[list] = [list() for i in range(v)]

        def add_edge(self, start: int, end: int):
            self.graphs[start].append(end)

        def remove_edge(self, start: int, end: int):
            self.graphs[start].remove(end)


    class GraphTraversal:
        def __init__(self, graph: ListGraph):
            self.graph = graph
            self.visited: list[Optional[bool]] = [None] * len(self.graph.graphs)

        def bfs_traversal(self, v: int):
            queue: Queue = Queue()
            queue.put(v)
            self.visited[v] = True

            while not queue.empty():
                cur: int = queue.get()

                print(cur)

                for i in self.graph.graphs[cur]:
                    if not self.visited[i]:
                        self.visited[i] = True
                        queue.put(i)

        def bfs(self):
            self.bfs_traversal(0)


    if __name__ == '__main__':
        list_graph: ListGraph = ListGraph(5)
        list_graph.add_edge(0, 1)
        list_graph.add_edge(0, 2)
        list_graph.add_edge(1, 4)
        list_graph.add_edge(2, 4)
        list_graph.add_edge(4, 3)

        graph_traversal: GraphTraversal = GraphTraversal(list_graph)
        graph_traversal.bfs()
    ```
<br />
