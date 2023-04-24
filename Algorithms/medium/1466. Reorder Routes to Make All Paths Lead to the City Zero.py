class Solution(object):
    def minReorder(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: int
        """
        self.nreverse = 0
        non_orient = [[] for _ in range(n)]
        orient = [set() for _ in range(n)]
        for u, v in connections:
            non_orient[u].append(v)
            non_orient[v].append(u)
            orient[u].add(v)

        visited = [False] * n

        def dfs(start):
            visited[start] = True
            for u in non_orient[start]:
                if not visited[u]:
                    if u in orient[start]:
                        self.nreverse += 1
                    dfs(u)

        dfs(0)
        return self.nreverse