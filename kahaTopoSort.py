class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegrees = [0] * numCourses
        graph = collections.defaultdict(set)
        for a, b in prerequisites:
            graph[b].add(a)
            indegrees[a] += 1
        
        
        queue = [i for i, indegree in enumerate(indegrees) if indegree == 0]
        result = queue[:]

        while queue:
            node = queue.pop()
            for next_node in graph[node]:
                indegrees[next_node] -= 1
                if indegrees[next_node] == 0:
                    queue.append(next_node)
                    result.append(next_node)
        if len(result) == numCourses:
            return result
        return []

