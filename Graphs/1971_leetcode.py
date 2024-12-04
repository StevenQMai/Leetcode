class Solution:
    def validPath(self, n: int, edges, source: int, destination: int) -> bool:
        # Create an adjacency list representation of the graph.
        # Each node (from 0 to n-1) will have a list of its neighbors.
        graph = {i: [] for i in range(n)}

        # Populate the adjacency list with edges (bi-directional connections).
        for u, v in edges:
            graph[u].append(v)  # Add v to the list of neighbors for u
            graph[v].append(u)  # Add u to the list of neighbors for v
        
        # A set to keep track of visited nodes during the DFS traversal.
        visited = set()

        # Define the Depth-First Search (DFS) function.
        def dfs(node: int) -> bool:
            # Base case: if the current node is the destination, a valid path exists.
            if node == destination:
                return True

            # Mark the current node as visited to avoid revisiting it.
            visited.add(node)

            # Recursively visit all unvisited neighbors.
            for neighbor in graph[node]:
                if neighbor not in visited:  # Proceed only if the neighbor is not visited
                    # If any recursive DFS call finds a valid path, propagate True upwards.
                    if dfs(neighbor):
                        return True

            # If no path is found through this node, return False.
            return False

        # Initiate the DFS traversal starting from the source node.
        return dfs(source)
