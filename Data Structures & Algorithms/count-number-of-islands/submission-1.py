class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = {}
        count= 0
        visited = set()
        def create_island(x,y,origin):
            if (y <0) or (y>= len(grid)or x <0) or (x>= len(grid[y])) or ((str(x)+","+str(y)) in visited) or grid[y][x] ==  "0":
                return
            visited.add((str(x)+","+str(y)))
            islands[origin].append([x,y])
            create_island(x,y+1,origin)
            create_island(x+1,y,origin)

            create_island(x-1,y,origin)
            create_island(x,y-1,origin)
        

        for y,row in enumerate(grid):
            for x,col in enumerate(row):
                if grid[y][x] ==  "1" and (str(x)+","+str(y)) not in islands:
                    visited = set()
                    islands[str(x)+","+str(y)] = []
                    create_island(x,y,str(x)+","+str(y))
                    count+=1
                    for i in islands[str(x)+","+str(y)]:
                        islands[str(i[0])+","+str(i[1])] = islands[str(x)+","+str(y)]
        return count
