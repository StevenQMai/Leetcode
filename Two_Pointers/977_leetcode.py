
class Solution:
    def sortedSquares(self, nums):
        #BRUTE FORCE METHOD 

        """
        squared_list = []

        for i in range(len(nums)):
            nums[i] = nums[i] ** 2
            squared_list.append(nums[i])
        
        return sorted(squared_list)
        """

        #2 POINTERS METHOD
        left, right = 0, len(nums) - 1

        new_list = []

        while left <= right:
            if abs(nums[left]) > abs(nums[right]):
                new_list.append(nums[left] ** 2)
                left += 1
            else:
                new_list.append(nums[right] ** 2)
                right -= 1

        new_list.reverse()

        return new_list
        

        #Time: O(n)
        #Space: O(1)


nums = [-4,-1,0,3,10]
solution = Solution()
print(solution.sortedSquares(nums))