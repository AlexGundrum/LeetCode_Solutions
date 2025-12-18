'''
https://leetcode.com/problems/search-a-2d-matrix/description/
You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.
'''


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        '''
        plan: find row, then find column i think
        '''
        rowL, rowR = 0, len(matrix) - 1
        foundRow = False
        mid = (rowL + rowR) // 2
        while rowL <= rowR: 
            mid = (rowL + rowR) // 2
            if matrix[mid][0] > target:
                #we need to update rowR to be less
                rowR = mid - 1
            elif matrix[mid][-1] < target:
                #we are too small, lets get rowL to be greater
                rowL = mid + 1
            else:
                #our mid value is good!
                break
       
        #mid now holds row that it could be in    
        colL, colR = 0, len(matrix[0]) - 1
        
        while colL <= colR:
            colMid = (colL + colR) // 2
            
            if matrix[mid][colMid] == target:
                return True
            elif matrix[mid][colMid] > target:
                #we are too great, need to decrease colR
                colR = colMid - 1
            else:
                #we are too small, we need to increase colL
                colL = colMid + 1
        return False
