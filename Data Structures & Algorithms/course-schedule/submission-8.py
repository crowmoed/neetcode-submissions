class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i:[] for i in range(numCourses)}

        for i in prerequisites:
            preMap[i[0]].append(i[1])



        visited = set()
        def dfs(crs):
            if crs in visited:
                return False
            if preMap[crs] == []:
                return True
            visited.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            visited.remove(crs)
            preMap[crs]= []
            return True
        

        for i in range(numCourses):
            if not dfs(i):
                return False
            

        return True
