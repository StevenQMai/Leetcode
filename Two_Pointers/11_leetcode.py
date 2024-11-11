class Solution:
    def maxArea(self, heights):
        #BRUTE FORCE
        """
        res = 0
        
        for l in range(len(heights)):
            for r in range(l + 1, len(heights)):
                area = (r-l) * (min(heights[l], heights[r]))
                res = max(res, area)

        return res
        """


        #2 pointers solution
        res = 0
        l, r = 0, len(heights) - 1

        while l < r:
            area = (r - l) * (min(heights[l], heights[r]))
            res = max(res, area)

            if heights[l] < heights[r]:
                l += 1
            elif heights[l] > heights[r]:
                r -= 1
            elif heights[l == heights[r]]:
                r -= 1

        return res


solution = Solution()
heights = [1,7,2,5,4,7,3,6]
print(solution.maxArea(heights))