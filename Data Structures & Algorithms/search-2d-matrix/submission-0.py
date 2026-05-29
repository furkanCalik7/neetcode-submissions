class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ## first find row
        ## then search in row
        m, n = len(matrix), len(matrix[0])
        
        l, r = 0, m - 1

        while l <= r:
            m = l + (r - l) // 2 

            if target < matrix[m][0]:
                r = m - 1
            elif target > matrix[m][-1]:
                l = m + 1
            else:
                break
        row = m
        
        l, r = 0, n - 1

        while l <= r:
            m = l + (r - l) // 2

            if matrix[row][m] == target:
                return True

            if target < matrix[row][m]:
                r  = m - 1
            else:
                l = m + 1
        


        return False