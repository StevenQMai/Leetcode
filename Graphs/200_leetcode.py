from collections import deque  # Import deque for efficient queue operations

class Solution:
    def numIslands(self, grid) -> int:
        # If the grid is empty, there are no islands
        if not grid:
            return 0

        # Get the dimensions of the grid
        rows, cols = len(grid), len(grid[0])
        # A set to keep track of visited cells
        visit = set()
        # Counter to keep track of the number of islands
        islands = 0

        # Define the BFS function to explore an island starting from a specific cell
        def bfs(r, c):
            # Initialize a queue and add the starting cell
            q = deque()
            visit.add((r, c))  # Mark the starting cell as visited
            q.append((r, c))  # Add the starting cell to the queue

            # Perform BFS
            while q:
                # Pop the first element from the queue (breadth-first exploration)
                row, col = q.popleft() # If you change this popleft to just pop (popping from the right), it becomes an iterative DFS
                # Define the possible directions of movement (up, down, left, right)
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

                # Explore each neighboring cell
                for dr, dc in directions:
                    r, c = row + dr, col + dc  # Calculate the coordinates of the neighbor
                    # Check if the neighbor is within bounds, is land ("1"), and not yet visited
                    if (r in range(rows) and 
                        c in range(cols) and 
                        grid[r][c] == "1" and 
                        (r, c) not in visit):
                        # If valid, add the neighbor to the queue and mark it as visited
                        q.append((r, c))
                        visit.add((r, c))

        # Iterate through all cells in the grid
        for r in range(rows):
            for c in range(cols):
                # If the current cell is land ("1") and not visited, start a BFS from it
                if grid[r][c] == "1" and (r, c) not in visit:
                    bfs(r, c)  # Perform BFS to mark all connected land cells
                    islands += 1  # Increment the island count after exploring one island

        return islands  # Return the total number of islands
