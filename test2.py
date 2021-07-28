class unionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1] * n
        self.count = n

    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])

        return self.parent[x]

    def union(self, u, v):

        root_u, root_v = self.find(u), self.find(v)
        if root_u == root_v:
            return 0  # Return False if u and v are already union
        if self.rank[root_u] < self.rank[root_v]:
            self.rank[root_v] += self.rank[root_u]
            self.parent[root_u] = root_v

        else:
            self.rank[root_u] += self.rank[root_v]
            self.parent[root_v] = root_u
        return 1


class Solution:
    def getId(r, c):
        return r * n + c
    def numIslands2(self, m, n, positions):
        numIslands=0
        numIsland_list=[]
        visitedPos=set()
        for i,j in positions:
            if (i,j) in visitedPos:
                numIsland_list.append(numIsland_list[-1])
            else:
                visitedPos.add((i,j))
                numIslands+=1
                X=self.getId(i,j)
                for x,y in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
                    if 0<=x<m and 0<=y<n and (x,y) in visitedPos:
                        Y=self.getId(x,y)
                        numIslands-=unionFind.union(X,Y)
                numIsland_list.append(numIslands)
        return numIsland_list


