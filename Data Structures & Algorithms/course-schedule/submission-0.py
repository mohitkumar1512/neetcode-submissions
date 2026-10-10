class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # kahn's algorithm

        # adj_list 
        adj_list = defaultdict(list)
        indegree = [0] * numCourses
        for item in prerequisites:
            crs = item[0]
            pre = item[1]
            adj_list[pre].append(crs)
            indegree[crs] += 1
        
        q = deque()
        for i, crs in enumerate(indegree): 
            if crs == 0:
                q.append(i)
        
        seen = 0
        while q: 
            for _ in range(len(q)):
                crs = q.popleft()
                courses = adj_list[crs]
                for val in courses: 
                    indegree[val] -= 1
                    if indegree[val] == 0:
                        q.append(val)
                
                seen += 1
        return seen == numCourses

        
        