from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        hashset1 = set()
