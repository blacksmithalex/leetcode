class Solution(object):
    def countPairs(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        W = [[] for _ in range(n)]
        for i in range(len(edges)):
            u, v = edges[i][0], edges[i][1]
            W[u].append(v)
            W[v].append(u)

        visited = [False] * n
        parts = []

        def dfs(start):
            visited[start] = True
            cur_vert.append(start)
            for u in W[start]:
                if not visited[u]:
                    dfs(u)

        for i in range(n):
            if not visited[i]:
                cur_vert = []
                dfs(i)
                parts.append(len(cur_vert))
        s = 0
        for i in range(len(parts)):
            s += (parts[i] * (n - parts[i]))
        return s // 2
