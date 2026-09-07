class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n_rows = len(matrix)
        n_cols = len(matrix[0])
        top = 0
        bottom = n_rows - 1 

        while top <= bottom:
            mid_row = (top + bottom) // 2

            if target > matrix[mid_row][-1]:
                top = mid_row + 1

            elif target < matrix[mid_row][0]:
                bottom = mid_row - 1
            
            else : 
                break
        
        if(top > bottom): 
            return False 
        
        
        
        mid_row = (top + bottom) // 2
        left = 0 
        right = n_cols - 1 

        while left <= right: 
            mid = (left + right) // 2

            if target > matrix[mid_row][mid]: 
                left = mid + 1 
            
            elif target <  matrix[mid_row][mid]: 
                right = mid - 1  
            
            else: 
                return True 
        
        if (left > right): 
            return False 
      
      