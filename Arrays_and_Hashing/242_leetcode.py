class Solution:
    def valid_anagram(self, s, t):
        if len(s) != len(t): #base case: checks if the two strings are equal in length to begin with
            return False

        countS, countT = {}, {} #creates two hashMaps to count the characters in both strings

        for character in range(len(s)): #we only need to iterate through the length of S since we know by this point that S and T must be equal in length
            countS[s[character]] = 1 + countS.get(s[character], 0) #everytime we see a character in s or t, we want to increment the count of that character by 1
            countT[t[character]] = 1 + countT.get(t[character], 0) #the purpose of the get function is to avoid scenarios where the character doesn't exist in the hashMap yet
            #0 is the default value. In other words, if the key s[i] does not exist in the hashmap, then the default value that the get function will return is 0.
        for character in countS: #iterate through the hashmaps and make sure the counts are the same
            if countS[character] != countT.get(character, 0): #if the key doesn't exist in the countT map yet, use the get function to avoid this!
                return False #if the counts are not the same, return false immediately

        return True #if the code exits, return True
 


