from typing import List

#BRUTE FORCE SOLUTION: O(n^2)
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = []

        #iterate through each element by index, which is essential for excluding the current element of each iteration
        for i in range(len(nums)):
            product = 1 #resets product to 1 for each iteration so that 'product' won't carry over values from previous iterations
            for j in range(len(nums)): #creates a second pointer j
                if i != j: 
                    product *= nums[j]
                    #computes the product of all elements of nums except the one at index 'i'
            answer.append(product) #add this new product to the answer array

        return answer




