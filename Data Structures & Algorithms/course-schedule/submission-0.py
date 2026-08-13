class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
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
        cnt = 0
        while q:
            node = q.popleft()
            cnt += 1
            for dest in adj[node]:
                indegree[dest] -= 1
                if indegree[dest] == 0:
                    q.append(dest)
        
        if cnt == numCourses:
            return True
        else: 
            return False

