class Solution(object):
    def validPath(self, n, edges, source, destination):
        """
        :type n: int
        :type edges: List[List[int]]
        :type source: int
        :type destination: int
        :rtype: bool
        """
        W = [[] for _ in range(n)]
        for u, v in edges:
            W[u].append(v)
            W[v].append(u)

        visited = [False] * n

        def dfs(start, destination):
            if start == destination:
                return True
            visited[start] = True
            for u in W[start]:
                if not visited[u]:
                    if dfs(u, destination):
                        return True
            return False
        return dfs(source, destination)
