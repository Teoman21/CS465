from collections import deque

class Solution(object):
    def mission2(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        
        
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1 
        
        n = len(grid)
        
        #init 8 directions
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1),  (-1, -1), (-1, 1), (1, -1), (1, 1)]
        
        #deque for bfs  row col step
        queue = deque([(0, 0, 1)]) 
        
        grid[0][0] = 1
        
        #while queue is not empty
        while queue:
            
            #remove the element and get the position of row and col
            row, col, step = queue.popleft()
            
            #found the shortest path
            if row == n-1 and col == n-1:
                return step
            
            for dr, dc in directions:
                #check every position
                nr = row + dr
                nc = col + dc
                
                
                #check if its nout out of bounds and cell is 0
                if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 0:
                    queue.append((nr, nc, step + 1))# move to next step
                    grid[nr][nc] = 1 #visited
                    
        return -1 #if not exist path
    
            
        
        