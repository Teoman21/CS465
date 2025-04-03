import unittest
from mission1 import Solution  # Importing the Solution class

class TestMission1(unittest.TestCase):
    def test_mission1(self):
        sol = Solution()
        grid = [["1","1","1","1","0"],
                ["1","1","0","1","0"],
                ["1","1","0","0","0"],
                ["0","0","0","0","0"]]
        self.assertEqual(sol.mission1(grid), 1)  # Expected output: 1
    
    def test_multiple_clusters(self):
        sol = Solution()
        grid = [
            ["1", "0", "1"],
            ["0", "0", "0"],
            ["1", "1", "0"]
        ]
        # Three clusters: one at (0,0), one at (0,2), and one by (2,0)-(2,1).
        self.assertEqual(sol.mission1(grid), 3)
    
    def test_single_cluster(self):
        sol = Solution()
        grid = [
            ["1", "1", "1", "1", "0"],
            ["1", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "1", "1", "0"]
        ]
        
        self.assertEqual(sol.mission1(grid), 2)
        
    def test_case2(self):
        sol = Solution()
        grid = [
            ["1", "1", "0", "0", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"]
        ]
        # Expected output: 3
        self.assertEqual(sol.mission1(grid), 3)
        
    def test_case3(self):
        sol = Solution()
        grid = [
            ["1", "1", "1"],
            ["0", "0", "0"],
            ["1", "1", "1"]
        ]
        # Expected output: 1
        self.assertEqual(sol.mission1(grid), 2)
        
    def test_empty_grid(self):
        sol = Solution()
        grid = []
        self.assertEqual(sol.mission1(grid), 0)

    def test_empty_row(self):
        sol = Solution()
        grid = [[]]
        self.assertEqual(sol.mission1(grid), 0)

    def test_all_water(self):
        sol = Solution()
        grid = [
            ["0", "0"],
            ["0", "0"]
        ]
        self.assertEqual(sol.mission1(grid), 0)

    def test_single_cell_land(self):
        sol = Solution()
        grid = [["1"]]
        self.assertEqual(sol.mission1(grid), 1)

    def test_single_cell_water(self):
        sol = Solution()
        grid = [["0"]]
        self.assertEqual(sol.mission1(grid), 0)


if __name__ == "__main__":
    unittest.main()
