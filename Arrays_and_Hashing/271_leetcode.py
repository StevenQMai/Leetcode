from typing import List

class Solution:

    def encode(self, strs: List[str]) -> str:
        result = "" #initializes an empty string 'result' 
        for string in strs: #for each string in 'strs' ...
            result += str(len(string)) + "#" + string 
            #add the numerical length of the string, a hashtag, and the string itself to the 'result' string
        return result
        #return this new 'result' string to be decoded below

    def decode(self, string: str) -> List[str]:
        result, i = [], 0 #initialize an empty result list, and a pointer 'i' starting at index 0
        while i < len(string): #while i is still in bounds of the string...
            j = i #create a new pointer j at position i (0)
            while string[j] != "#": #while the position j is not at '#'...
                j += 1 #increment j's position by 1, which then guarantees it to be at the '#' position, marking the end of the length indicator
            length = int(string[i:j]) #converts the substring from 'i' to 'j' to an integer ('length'), which represents the length of the string
            result.append(string[j + 1 : j + 1 + length]) #extracts the substring starting right after '#' and up until the specified length and appends it to the 'result' list
            i = j + 1 + length #updates 'i' to the position right after the extracted substring
            #'j + 1': Moves i to the character immediately following the #.
            #'+ length': Adds the length of the extracted substring,
            #so now, 'i' is at the start of the next length indicator (or at the end of the string if all substrings are processed)
        return result 
        #returns the 'result' list, which now contains the original strings


