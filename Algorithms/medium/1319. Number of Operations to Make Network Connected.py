class Solution(object):
    def makeConnected(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: int
        """
        if len(connections) < n - 1:
            return -1
        W = [[] for _ in range(n)]
        for u, v in connections:
            W[u].append(v)
            W[v].append(u)
        visited = [False] * n
        def dfs(start):
            visited[start] = True
            for u in W[start]:
                if not visited[u]:
                    visited[u] = True
                    dfs(u)
        ncomp = 0
        for i in range(n):
            if not visited[i]:
                ncomp += 1
                dfs(i)
        return ncomp - 1