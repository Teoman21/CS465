class Solution(object):
    def mission1(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        # if grid is empty retur 0 because no ships
        if not grid:
            return 0
        
        #assign rows and columns inside the matrix  
        grid_rows = len(grid)
        grid_cols = len(grid[0])
        
        battleship_count = 0
        
        print("rows ",grid_rows)
        print("cols ",grid_cols)
        
        def dfs(row, col):
            
            #check if its out of bounds here or cell = 0
            
            if row < 0 or  col < 0 or row >= grid_rows or col >= grid_cols or grid[row][col] == "0":
                return 0
            
            #if visited change to 0
            grid[row][col] = "0"
            
            dfs(row +1, col) #to move down
            dfs(row-1, col) #to move up
            dfs(row,col-1) # to move left
            dfs(row,col+1) #to move right
            
        # looping the grid for count the battleships
        for row in range(grid_rows):
            for col in range(grid_cols):
                    
                if grid[row][col] == "1": #means there is ship
                    battleship_count += 1
                    dfs(row,col)
            
            
        return battleship_count
                
        
        
        
        