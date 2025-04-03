import unittest
from mission2 import Solution  # Importing the Solution class

class TestMission2(unittest.TestCase):
    def test_mission2(self):
        sol = Solution()
        grid = [[0,1],[1,0]]
        self.assertEqual(sol.mission2(grid), 2)  # Expected output: 2
    
    def test_obstacle_path(self):
        sol = Solution()
        grid = [
            [0, 1, 0],
            [0, 1, 0],
            [0, 0, 0]
        ]
        # With obstacles at (0,1) and (1,1), a likely optimal path is:
        # (0,0) -> (1,0) -> (2,1) -> (2,2), which is 3 moves.
        self.assertEqual(sol.mission2(grid), 4)
    
    def test_no_path(self):
        sol = Solution()
        grid = [
            [0, 1, 0],
            [0, 1, 0],
            [0, 1, 0]
        ]
        # With obstacles at (0,1) and (1,1), a likely optimal path is:
        # (0,0) -> (1,0) -> (2,1) -> (2,2), which is 3 moves.
        self.assertEqual(sol.mission2(grid), -1)
    
    def test_no_path(self):
        sol = Solution()
        grid = [
            [0, 0, 0],
            [0, 1, 1],
            [0, 0, 0]
        ]
        # With obstacles at (0,1) and (1,1), a likely optimal path is:
        # (0,0) -> (1,0) -> (2,1) -> (2,2), which is 3 moves.
        self.assertEqual(sol.mission2(grid), 4)
        
    def test_empty_grid(self):
        sol = Solution()
        grid = [[0]]
        self.assertEqual(sol.mission2(grid), 1)

    def test_single_obstacle(self):
        sol = Solution()
        grid = [[0, 0], [0, 1]]
        self.assertEqual(sol.mission2(grid), -1)
    def test_large_grid_with_path(self):
        sol = Solution()
        grid = [
            [0, 1, 0, 0, 0],
            [0, 1, 0, 1, 0],
            [0, 0, 0, 1, 0],
            [1, 1, 1, 1, 0],
            [0, 0, 0, 0, 0]
        ]
        self.assertEqual(sol.mission2(grid), 9)

    def test_start_blocked(self):
        sol = Solution()
        grid = [[1, 0], [0, 0]]
        self.assertEqual(sol.mission2(grid), -1)

    def test_end_blocked(self):
        sol = Solution()
        grid = [[0, 0], [0, 1]]
        self.assertEqual(sol.mission2(grid), -1)
    
    def test_case2(self):
        sol = Solution()
        grid = [
            [0, 0, 0],
            [1, 1, 0],
            [1, 1, 0]
        ]
        # Expected output: 4
        self.assertEqual(sol.mission2(grid), 4)

    def test_case3(self):
        sol = Solution()
        grid = [
            [1, 0, 0],
            [1, 1, 0],
            [1, 1, 0]
        ]
        # Expected output: -1 (since the start is blocked)
        self.assertEqual(sol.mission2(grid), -1)     
        
    def test_case4(self):
        
        sol = Solution()
        grid = [
            [0, 0, 0],
            [1, 0, 1],
            [1, 1, 0]
        ]
        # Expected output: 4
        self.assertEqual(sol.mission2(grid), 3)   
        
if __name__ == "__main__":
    unittest.main()
