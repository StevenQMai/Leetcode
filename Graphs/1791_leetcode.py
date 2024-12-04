class Solution:
    def findCenter(self, edges) -> int:
        # Since there is a guaranteed center (star graph), we can just check if the the first element in the first list in edges is the center by checking if its equal to one of the elements in the second list.
        # If not, we just return the second element in the first list in edges
        if edges[0][0] == edges[1][0] or edges[0][0] == edges[1][1]:
            return edges[0][0]
        else:
            return edges[0][1]