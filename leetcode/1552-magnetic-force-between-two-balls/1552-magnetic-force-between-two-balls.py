class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:

        position.sort()
        def can_place(x):
            curr = position[0]
            cnt = 1
            for i in range(1, len(position)):
                if abs(position[i] - curr) >= x:
                    curr = position[i]
                    cnt+=1
            

            return cnt >= m
        
        low = 0
        high = max(position)

        while low+1 < high:
            mid = (low+high)//2

            if can_place(mid):
                low = mid
            else:
                high = mid

        return low  
