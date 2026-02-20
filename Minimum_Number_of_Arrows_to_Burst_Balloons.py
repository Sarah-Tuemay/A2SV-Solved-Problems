class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:

        if len(points) == 1:
            return 1
        
        right = 1

        points.sort()

        min_point = points[0][0]
        max_point = points[0][1]
        num_arrows = 1

        while right < len(points):
            if points[right][0] <= max_point:
                min_point = points[right][0]
                if points[right][1] < max_point:
                    max_point = points[right][1]
            else:
                num_arrows += 1
                min_point = points[right][0]
                max_point = points[right][1]
                
            right += 1
        
        return num_arrows
