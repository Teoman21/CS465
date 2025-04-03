import unittest
from mission3 import Solution  # Importing the Solution class

class TestMission3(unittest.TestCase):
    def test_mission3(self):
        sol = Solution()
        grid = [[1,2,2],
                [3,8,2],
                [5,3,5]]
        self.assertEqual(sol.mission3(grid), 2)  # Expected output: 2
    
    def test_smooth_terrain(self):
        sol = Solution()
        grid = [
            [1, 2],
            [2, 3]
        ]
        
        # Both possible paths yield a maximum adjacent difference of 1.
        self.assertEqual(sol.mission3(grid), 1)

    def test_varied_terrain(self):
        sol = Solution()
        grid = [
            [5, 3, 6],
            [7, 8, 2],
            [4, 3, 1]
        ]
        # Expected maximum difference along the optimal path is 3.
        self.assertEqual(sol.mission3(grid), 3)
        
        
    def test_single_element_grid(self):
        sol = Solution()
        grid = [[5]]
        self.assertEqual(sol.mission3(grid), 0)

    def test_larger_grid(self):
        sol = Solution()
        grid = [
            [1, 2, 3, 4, 5],
            [6, 7, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 17, 18, 19, 20],
            [21, 22, 23, 24, 25]
        ]
        self.assertEqual(sol.mission3(grid), 5)

    def test_grid_with_same_values(self):
        sol = Solution()
        grid = [
            [5, 5, 5],
            [5, 5, 5],
            [5, 5, 5]
        ]
        self.assertEqual(sol.mission3(grid), 0)

    def test_grid_with_large_difference(self):
        sol = Solution()
        grid = [
            [1, 100, 1],
            [100, 1, 100],
            [1, 100, 1]
        ]
        self.assertEqual(sol.mission3(grid), 99)

    def test_complex_terrain(self):
        sol = Solution()
        grid = [
            [1, 5, 1, 5],
            [2, 6, 2, 6],
            [3, 7, 3, 7],
            [4, 8, 4, 8]
        ]
        self.assertEqual(sol.mission3(grid), 4)


    def test_case2(self):
        sol = Solution()
        grid = [
            [1, 2, 3],
            [3, 8, 4],
            [5, 3, 5]
        ]
        # Expected output: 1
        self.assertEqual(sol.mission3(grid), 1)

    def test_case3(self):
        sol = Solution()
        grid = [
            [1, 2, 1, 1, 1],
            [1, 2, 1, 2, 1],
            [1, 2, 1, 2, 1],
            [1, 2, 1, 2, 1],
            [1, 1, 1, 2, 1]
        ]
        # Expected output: 0 (path with zero maximum difference)
        self.assertEqual(sol.mission3(grid), 0)
        
    def test_case4(self):
        sol = Solution()
        grid = [
            [1, 2, 3],
            [3, 8, 4],
            [5, 3, 5]
        ]
        
        self.assertEqual(sol.mission3(grid), 1)
    
    
if __name__ == "__main__":
    unittest.main()
