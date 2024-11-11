class Solution:
    def two_sum(self, nums, target):
        hashMap = {} #value : index
        for index, number in enumerate(nums): #enumerate function provides both the index and value (in that order) from an interable (nums)
            #this allows for enumerate(nums) to be looped through with two variables, with index as the current index and number as the current element
            difference = target - number #for each number, the difference is calculated
            if difference in hashMap: #if difference is already in hashMap, it means that we have previously encountered a number that adds up to the target when adding the current 'number' variable
                return [hashMap[difference], index] 
            hashMap[number] = index #if the difference isn't in the hashMap, store the current number as the key and its index as the value in hashMap
            #value : index
        return


# Solution Breakdown:
    # Initialize a HashMap: 
        # We start by creating an empty dictionary (hashmap). 
        # This dictionary will store the numbers we have seen so far as keys and their corresponding indices as values.
    # Iterate through the List: 
        # We loop through the list (nums) using enumerate to get both the index and the number at each iteration.
    # Calculate the Difference: 
        # For each number, we calculate difference = target - number. This difference represents the value we need to find in the list to reach the target sum.
    # Check the HashMap: 
        # We check if the difference is already in the hashmap. 
        # If it is, it means we have found the two numbers that add up to the target (the current number and the number corresponding to difference which we have seen before). We return their indices.
        # If it is not, we store the current number and its index in the hashmap.
    # Return the Result: 
        # The function will return the indices of the two numbers that add up to the target.


