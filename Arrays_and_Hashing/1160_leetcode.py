"""
1. does a string have to use ALL the characters?
2. can we use the same char in more than one word?
3. uppercase and lower case treated the same?
4. Are there duplicates in the word list? should we assume no or check?
5. no valid words

Edge-cases? special characters? character sets?


less helpful, depending on the interview level
1. how long can a word or char be? a billion characters?

"""

class Solution:
    def countCharacters(self, words, chars): #

        # Top bread, answer holder, to be modified - result 
        result = 0
        
        # Count how many instances of each char exist
        
        # loop words

            # state flag? set to good, then bail out of your loop if false
            
            # check if each char in the word (loop), is in our 
                # frequency count, if we "use" it in the word, decrement
                # bail out early if not possible, toggle state

            
            # If the char in the word loop finishes, then the word can be formed!
            # then we win! for that single word, 
            # increment our top bread

        return result
        # Finish the sandwich, return the bread