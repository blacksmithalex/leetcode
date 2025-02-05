class Solution(object):
    def countPairs(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        W = [[] for _ in range(n)]
        for u, v in edges:
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
        
        res = 0
        for i in range(len(parts)):
            res += (parts[i]) * (n - parts[i])
        return res // 2