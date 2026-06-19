from collections import defaultdict

# ===================== 1. 定义题目中的无向带权图 =====================
# 每条边格式：(起点, 终点, 权重)
edges = [
    ("A", "B", 2),
    ("A", "D", 3),
    ("B", "C", 4),
    ("B", "E", 1),
    ("D", "E", 6),
    ("E", "F", 2),
    ("C", "F", 5)
]
vertices = ["A", "B", "C", "D", "E", "F"]

# ===================== 2. Kruskal算法所需：并查集类 =====================
class UnionFind:
    def __init__(self, node_list):
        # 初始化：每个节点的父节点是自己
        self.parent = {node: node for node in node_list}

    def find(self, x):
        # 查找根节点 + 路径压缩优化
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        # 合并两个集合，返回True代表不产生环，可以加入MST
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:
            # 两点已经连通，加边会形成环
            return False
        self.parent[root_y] = root_x
        return True

# ===================== 3. Kruskal算法实现 =====================
def kruskal_mst(edge_list, nodes):
    # 1. 将所有边按权重从小到大排序
    sorted_edges = sorted(edge_list, key=lambda item: item[2])
    uf = UnionFind(nodes)
    mst_edges = []
    total_weight = 0

    # 2. 从小到大遍历每条边
    for u, v, w in sorted_edges:
        if uf.union(u, v):
            mst_edges.append((u, v, w))
            total_weight += w
            # n个顶点只需要n-1条边，凑够直接退出循环
            if len(mst_edges) == len(nodes) - 1:
                break
    return mst_edges, total_weight

# ===================== 4. Prim算法实现（起点默认A） =====================
def prim_mst(edge_list, start="A"):
    # 构建邻接表存储图
    adj = defaultdict(list)
    all_nodes = set()
    for u, v, w in edge_list:
        adj[u].append((v, w))
        adj[v].append((u, w))
        all_nodes.add(u)
        all_nodes.add(v)

    visited = set()  # 已纳入MST的顶点集合
    mst_edges = []
    total_weight = 0
    visited.add(start)

    # 直到所有顶点都加入集合
    while len(visited) < len(all_nodes):
        min_w = float("inf")
        min_edge = None
        # 遍历所有已访问点的邻边，寻找连接未访问点的最小权重边
        for node in visited:
            for neighbor, weight in adj[node]:
                if neighbor not in visited and weight < min_w:
                    min_w = weight
                    min_edge = (node, neighbor, weight)
        # 将最小边加入最小生成树
        u, v, w = min_edge
        mst_edges.append(min_edge)
        total_weight += w
        visited.add(v)
    return mst_edges, total_weight

# ===================== 5. 程序入口，执行并打印结果 =====================
if __name__ == "__main__":
    # 运行Kruskal算法
    krus_edges, krus_sum = kruskal_mst(edges, vertices)
    print("===== Kruskal 最小生成树结果 =====")
    print("选中的边：", krus_edges)
    print("MST总权重：", krus_sum)

    print("\n===== Prim 最小生成树结果（起点A） =====")
    # 运行Prim算法
    prim_edges, prim_sum = prim_mst(edges, "A")
    print("选中的边：", prim_edges)
    print("MST总权重：", prim_sum)