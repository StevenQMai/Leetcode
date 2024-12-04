class Solution:
    def maxAreaOfIsland(self, grid) -> int:
        # Get the dimensions of the grid
        rows, cols = len(grid), len(grid[0])
        # Set to keep track of visited cells to avoid revisiting them
        visit = set()

        # Define a Depth-First Search (DFS) function to calculate the area of an island
        def dfs(r, c):
            # Base case: if the cell is out of bounds, water (0), or already visited
            if (r < 0 or r == rows or c < 0 or c == cols or
                grid[r][c] == 0 or (r, c) in visit):
                return 0
            
            # Mark the current cell as visited
            visit.add((r, c))
            
            # Return the area of this cell (1) plus the area of its connected neighbors
            return (1 + dfs(r + 1, c) +  # Down
                        dfs(r - 1, c) +  # Up
                        dfs(r, c + 1) +  # Right
                        dfs(r, c - 1))   # Left

        # Variable to track the maximum area of any island found
        area = 0

        # Iterate through all cells in the grid
        for r in range(rows):
            for c in range(cols):
                # If the current cell is part of an island and not visited, calculate its area
                area = max(area, dfs(r, c))  # Update the maximum area

        return area  # Return the largest area found
