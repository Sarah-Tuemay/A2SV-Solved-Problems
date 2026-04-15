class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:

        houses.sort()
        heaters.sort()

        def can_heat(r):
            p_house, p_heater = 0, 0
            
            while p_house < len(houses):

                if p_heater < len(heaters)-1 and heaters[p_heater] < houses[p_house]:
                    p_heater += 1
                    continue 

                dist_to_right = abs(houses[p_house] - heaters[p_heater])
                
                if p_heater > 0:
                    dist_to_left = abs(houses[p_house] - heaters[p_heater - 1])
                else:
                    dist_to_left = float('inf') 
                    
                min_dist = min(dist_to_right, dist_to_left)
                
                if min_dist > r:
                    return False
                    
                p_house += 1
                
            return True
        
        low = -1
        high = max(max(houses), max(heaters))

        while low + 1 < high:
            mid = (low+high)//2

            if can_heat(mid):
                high = mid
            else:
                low = mid
        
        return high



        