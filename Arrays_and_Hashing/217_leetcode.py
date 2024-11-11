class Solution:
    def containsDuplicate(self, nums):
        hashSet = set() #creates a set
        #a hashset stores unique elements, like a math set. Does not allow duplicates

        for number in nums: #for every number in the input array...
            if number in hashSet: #if the number already exists in the hashset:
                return True #return true since this indicates that the list contains a duplicate
            hashSet.add(number) #if the hashset doesnt already contain a duplicate, add every number to our hashset, 
                                #then iterate through the rest of the array of nums
        return False #indicates that there were no duplicates found in the input array
            