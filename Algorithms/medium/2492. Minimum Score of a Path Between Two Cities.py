class Solution(object):
    def minScore(self, n, roads):
        """
        :type n: int
        :type roads: List[List[int]]
        :rtype: int
        """
        graph = defaultdict(dict)
        for u, v, l in roads:
            graph[u][v] = graph[v][u] = l
        min_score = 10**4
        queue = deque([1])
        visited = {1}
        while queue:
            u = queue.popleft()
            for v, dist in graph[u].items():
                if v not in visited:
                    queue.append(v)
                    visited.add(v)
                min_score = min(min_score, dist)
        return min_score
