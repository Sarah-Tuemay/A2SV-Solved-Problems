class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        low = 0
        high = len(matrix)-1
        target_row = []
        while low <= high:
            mid = (low+high)//2
            if matrix[mid][0] <= target  <= matrix[mid][len(matrix[mid])-1]:
                ll = 0
                hh = len(matrix[mid])-1
                while ll <= hh:
                    mii= (ll+hh)//2
                    if matrix[mid][mii] == target:
                        return True
                    if matrix[mid][mii] < target:
                        ll = mii+1
                    else:
                        hh = mii-1
                    
                low = mid+1
                # print(target_row)
            elif matrix[mid][0] > target:
                high = mid-1
            else:
                low = mid + 1
        
        return False