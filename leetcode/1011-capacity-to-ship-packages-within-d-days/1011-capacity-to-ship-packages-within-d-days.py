class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def days_num(capacity):
            c = 0
            day = 0 
            for i in weights:
                c += i
                if c > capacity:
                    day += 1
                    c = i
            
            return day+1 <= days
    
        low = max(weights)-1
        high = sum(weights)

        day = 0
        while low+1 < high:
            mid = (low+high)//2


            if not days_num(mid):
                low = mid
            else:
                high = mid
        
        return high