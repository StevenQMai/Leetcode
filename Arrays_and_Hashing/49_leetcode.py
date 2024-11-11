from collections import defaultdict #defaultdict(list) means "defining a dictionary with values as a list"

class Solution:
    def groupAnagrams(self, strs):

        resultingHashmap = defaultdict(list) #creates an empty list for each new key encountered in the iteration

        for strings in strs: #iterating over every string in the input list 'strs'
            count = [0] * 26 # a ... z
                             #Initializes a list called 'count' with 26 zeros, one for each letter in the English alphabet. 
                             #This list will be used to count the occurrences of each letter in the current string.

            for character in strings:
                count[ord(character) - ord("a")] += 1 #subtracts the ascii value of the current character by the ascii value of "a" in order to get its position/index from 0-25.
                                                      #Increments the value at this index in the count array to track the frequency of the character.
            #Example: 
            # ord("a") = 97   ->  count[ord("a") - ord("a")] = count[0]   
            # ord("b") = 98   ->  count[ord("b") - ord("a")] = count[1]   

            resultingHashmap[tuple(count)].append(strings)
            # Converts the count list to a tuple (because lists can't be used as dictionary keys, but tuples can). 
            # Uses this tuple as a key in resultingHashmap and appends the current string to the list of strings associated with this key. 
            # This effectively groups the anagrams together.

        return resultingHashmap.values()
        # Returns the values of resultingHashmap as a list. Each value is a list of anagrams.