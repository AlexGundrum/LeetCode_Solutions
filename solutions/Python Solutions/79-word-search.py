'''
https://leetcode.com/problems/word-search/description/
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.
'''


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        ROW, COL = len(board), len(board[0])

        usable = [[True for _ in range(COL)] for _ in range(ROW)]
        haveFound = False
        def dfs(curWord, r, c):
            
            if (not (0 <= r < ROW)) or (not (0 <= c < COL)):
                return False
            
            curWord += board[r][c]
            
            if curWord == word:
                nonlocal haveFound
                haveFound = True
            
            if curWord != word[0:len(curWord)]:
                return False
            
            usable[r][c] = False
            if (0 <= c-1 < COL) and (usable[r][c-1]):
                dfs(curWord, r, c-1)
            if ((0 <= c+1 < COL)) and (usable[r][c+1]):
                dfs(curWord, r, c+1)
            if ((0 <= r-1 < ROW)) and (usable[r-1][c]):
                dfs(curWord, r-1, c)
            if ((0 <= r+1 < ROW)) and (usable[r+1][c]):
                dfs(curWord, r+1, c)
            
            usable[r][c] = True
            
            
        
        
        
        for r in range(ROW):
            for c in range(COL):
                if board[r][c] == word[0]:
                    usable[r][c] = False
                    dfs("", r, c)
                    usable[r][c] = True
        
        return haveFound

            
        
