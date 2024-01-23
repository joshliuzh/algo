# Solution 1: DFS with an array storing 3 different states of a vertex

class Solution:
    	def buildAdjacencyList(self, n, edgesList):
    		...
    		
        def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
            # build Adjacency list from Edges list
            adjList = self.buildAdjacencyList(numCourses, prerequisites)
    
            # Each vertex can have 3 different states:
            # state 0   : vertex is not visited. It's a default state.
            # state -1  : vertex is being processed. Either all of its descendants
            #             are not processed or it's still in the function call stack.
            # state 1   : vertex and all its descendants are processed.
            state = [0] * numCourses
    
            def hasCycle(v):
                if state[v] == 1:
                    # This vertex is processed so we pass.
                    return False
                if state[v] == -1:
                    # This vertex is being processed and it means we have a cycle.
                    return True
    
                # Set state to -1
                state[v] = -1
    
                for i in adjList[v]:
                    if hasCycle(i):
                        return True
    
                state[v] = 1
                return False
    
            # we traverse each vertex using DFS, if we find a cycle, stop and return
            for v in range(numCourses):
                if hasCycle(v):
                    return False
    
            return True

# Solution 2: DFS with a stack storing all decendants being processed
    class Solution:
        def buildAdjacencyList(self, n, edgesList):
            ...
    
        def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
            # build Adjacency list from Edges list
            adjList = self.buildAdjacencyList(numCourses, prerequisites)
            visited = set()
    
            def hasCycle(v, stack):
                if v in visited:
                    if v in stack:
                        # This vertex is being processed and it means we have a cycle.
                        return True
                    # This vertex is processed so we pass
                    return False
    
                # mark this vertex as visited
                visited.add(v)
                # add it to the current stack
                stack.append(v)
    
                for i in adjList[v]:
                    if hasCycle(i, stack):
                        return True
    
                # once processed, we pop it out of the stack
                stack.pop()
                return False
    
            # we traverse each vertex using DFS, if we find a cycle, stop and return
            for v in range(numCourses):
                if hasCycle(v, []):
                    return False
    
            return True

