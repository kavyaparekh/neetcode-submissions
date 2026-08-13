class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0]*numCourses
        adj = defaultdict(list)
        for prereq in prerequisites:
            dest, source = prereq
            adj[source].append(dest)
            indegree[dest] += 1
        
        q = deque()
        
        for i in range(len(indegree)):
            if indegree[i] == 0:
                q.append(i)
        print(q)
        topo = []
        while q:
            node = q.popleft()
            topo.append(node)
            for dest in adj[node]:
                indegree[dest] -= 1
                if indegree[dest] == 0:
                    q.append(dest)

        print (topo)
        if len(topo) == numCourses:
            return topo
        else:
            return []
