import unittest
from mission4 import Solution  # Importing the Solution class

class TestMission4(unittest.TestCase):
    def test_already_solved(self):
        sol = Solution()
        grid = [
            [1, 2, 3],
            [4, 5, 0]
        ]
        # Already in target formation; expect 0 moves.
        self.assertEqual(sol.mission4(grid), 0)
    
    def test_one_move(self):
        sol = Solution()
        grid = [
            [1, 2, 3],
            [4, 0, 5]
        ]
        # One move (swapping 0 and 5) should lead to the target formation.
        self.assertEqual(sol.mission4(grid), 1)
    
    def test_two_moves(self):
        sol = Solution()
        grid = [
            [1, 2, 3],
            [0, 4, 5]
        ]
        # Two moves required (e.g., swap 0 with 1 then with 4) to achieve target.
        self.assertEqual(sol.mission4(grid), 2)
    
    def test_unsolvable(self):
        sol = Solution()
        grid = [
            [1, 2, 3],
            [5, 4, 0]
        ]
        # This configuration is unsolvable; expect -1.
        self.assertEqual(sol.mission4(grid), -1)
    
    def test_no_open_cell(self):
        sol = Solution()
        grid = [
            [1, 2, 3],
            [4, 5, 6]
        ]
        # No open water cell (0) exists; formation is impossible.
        self.assertEqual(sol.mission4(grid), -1)
    
    def test_complex_scramble(self):
        sol = Solution()
        grid = [
            [2, 3, 0],
            [1, 4, 5]
        ]
        # This scrambled configuration is solvable.
        # One possible solution sequence might require 5 moves to reach target formation.
        self.assertEqual(sol.mission4(grid), 5)

    
    def test_case2(self):
        sol = Solution()
        grid = [
            [1, 2, 3],
            [5, 4, 0]
        ]
        # Expected output: -1 (unsolvable configuration)
        self.assertEqual(sol.mission4(grid), -1)
    
    def test_case3(self):
        sol = Solution()
        grid = [
            [4, 1, 2],
            [5, 0, 3]
        ]
        # Expected output: 5 moves (complex scramble)
        self.assertEqual(sol.mission4(grid), 5)
    
    
if __name__ == "__main__":
    unittest.main()
