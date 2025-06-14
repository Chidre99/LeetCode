class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        self.parent[self.find(x)] = self.find(y)

class Solution:
    def minSwapsCouples(self, row):
        N = len(row) // 2
        uf = UnionFind(N)
        for i in range(0, len(row), 2):
            a, b = row[i] // 2, row[i+1] // 2
            uf.union(a, b)
        
        roots = set(uf.find(x) for x in range(N))
        return N - len(roots)
