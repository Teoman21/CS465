import heapq

class Solution(object):
    def mission3(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        n = len(grid)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        #to use priority queue heap
        heap = [(0,0,0)]
        
        #to track the minimum effort
        efforts = [[float('inf')] * n for _ in range(n)]
        efforts[0][0] = 0
        
        while heap:
            
            
            #pick the element with least effort
            cost, row, col = heapq.heappop(heap)
            
            #if reached the target return the effort
            if row == n-1 and col == n-1:
                return cost
            
            for dr, dc in directions:
                #check all position
                nr = row + dr
                nc = col + dc
                
                if 0 <= nr < n and 0 <= nc < n:
                    effort = abs(grid[nr][nc] - grid[row][col])
                    #check the new cost
                    new_cost = max(cost, effort)
                    
                    #if this way less effort than previous
                    if new_cost < efforts[nr][nc]:
                        #print("effort ", efforts[nr][nc])
                        efforts[nr][nc] = new_cost
                        heapq.heappush(heap, (new_cost, nr, nc)) #add to the heap
                       
        return -1
                    