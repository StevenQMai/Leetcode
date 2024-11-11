class Solution:
    def topKfrequent(self, nums, k):
        
        count = {}
        frequency = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0) #for each element 'n' in nums, increment the count of 'n' by 1 in the 'count' hashmap
            #the updated count is then stored back in the 'count' hashmap with 'n' as the key

        #Example illustration: 'nums' = [1, 1, 1, 2, 2, 3]
            #First iteration ('n' = 1):
                #count[1] = 1 + count.get(1, 0)
                #count = {1: 1}
            #Second iteration ('n' = 1):
                #count[1] = 1 + count.get(1, 0)
                #count = {1: 2}
            #Third iteration ('n' = 1):
                #count[1] = 1 + count.get(1, 0)
                #count = {1: 3}
            #Fourth iteration ('n' = 2):
                #count[2] = 1 + count.get(2, 0)
                #count = {1: 3, 2: 1}
            #Fifth iteration ('n' = 2):
                #count[2] = 1 + count.get(2, 0)
                #count = {1: 3, 2: 2}
            #Sixth iteration ('n' = 3):
                #count[3] = 1 + count.get(3, 0)
                #count = {1: 3, 2: 2, 3: 1}
        #Output: 1 occurs 3 times,  2 occurs 2 times,   3 occurs 1 time

        for n, c in count.items(): 
            #count.items() returns an object that lists the hashmap's key-value tuple pairs
            #Example: count.items() returns [(1,3) , (2,2) , (3,1)]
            # n is assigned the key (element from 'nums')
            # c is assigned the value (frequency/count of that element)

            frequency[c].append(n)
            #frequency[c] accesses the sublist in the frequency list at index 'c'. This sublist is intended to store all elements that appear 'c' times in the original 'nums' list
            #append[n] adds the element 'n' to this sublist

                #Example illustration:
                    #For n = 1 and c = 3:
                    #frequency[3].append(1):
                    #frequency becomes [[], [], [], [1], [], [], []].

                    #For n = 2 and c = 2:
                    #frequency[2].append(2):
                    #frequency becomes [[], [], [2], [1], [], [], []].

                    #For n = 3 and c = 1:
                    #frequency[1].append(3):
                    #frequency becomes [[], [3], [2], [1], [], [], []].

        result = [] #creates an empty array which stores the top K elements of 'nums'
        for i in range(len(frequency) - 1, 0, -1):
            #creates a sequence that starts from 'len(frequency) - 1' and goes down to '1'
            #this loop effectively iterates through frequency backwards in order to collect the most frequent elements first
            for n in frequency[i]:
                #iterates over each element 'n' in the sublist frequency[i] where i is the current frequency
                result.append(n)
                #appends the element 'n' to the result array
                if len(result) == k:
                    return result
                    #if the length of result matches k, then we have successfully found the most frequent k elements
