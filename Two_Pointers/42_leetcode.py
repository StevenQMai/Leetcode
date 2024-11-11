class Solution:
    def trap(self, height):
        l, r = 0, len(height) - 1

        while l < r:
            for i in range(len(height)):
                area = min(height[l], height[r]) - height[i]


