import heapq

class Solution(object):
    def mission4(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        target = ((1, 2, 3), (4, 5, 0))  # Goal state for a 2x3 grid
        rows, cols = 2, 3  # fixed grid dimensions for Mission 4

        # Convert grid to a tuple for state representation
        start = tuple(map(tuple, grid))
        if start == target:
            return 0  # Already in correct formation

        # Locate the position of the zero (open cell)
        zeros = [(r, c) for r in range(rows) for c in range(cols) if grid[r][c] == 0]
        if not zeros:
            return -1  # No open water cell; unsolvable.
        row_zero, col_zero = zeros[0]

        # Priority queue using Manhattan distance as heuristic.
        priority = [(self.get_manhattan_distance(start, target), 0, start, row_zero, col_zero)]
        visited = {start: 0}  # {state: g_score}

        while priority:
            f_score, g_score, state, row_zero, col_zero = heapq.heappop(priority)

            if state == target:
                return g_score  # number of moves

            # Try all valid moves (up, down, left, right)
            for new_state, new_r, new_c in self.get_neighbors(state, row_zero, col_zero, rows, cols):
                new_g_score = g_score + 1
                if new_state not in visited or new_g_score < visited[new_state]:
                    visited[new_state] = new_g_score
                    f_score = new_g_score + self.get_manhattan_distance(new_state, target)
                    heapq.heappush(priority, (f_score, new_g_score, new_state, new_r, new_c))

        return -1  # if no solution found

    def get_manhattan_distance(self, state, target):
        goal_positions = {target[r][c]: (r, c) for r in range(2) for c in range(3)}
        distance = 0
        for r in range(2):
            for c in range(3):
                val = state[r][c]
                goal_r, goal_c = goal_positions[val]
                distance += abs(r - goal_r) + abs(c - goal_c)
        return distance

    def get_neighbors(self, state, row_zero, col_zero, rows, cols):
        neighbors = []
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right

        for dr, dc in directions:
            new_r, new_c = row_zero + dr, col_zero + dc
            if 0 <= new_r < rows and 0 <= new_c < cols:
                # Swap zero with the adjacent cell.
                new_state = [list(row) for row in state]  # Convert tuple state to mutable list.
                new_state[row_zero][col_zero], new_state[new_r][new_c] = new_state[new_r][new_c], new_state[row_zero][col_zero]
                neighbors.append((tuple(map(tuple, new_state)), new_r, new_c))
        return neighbors
