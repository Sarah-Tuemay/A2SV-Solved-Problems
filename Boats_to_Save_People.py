class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        i = 0
        boat = 0
        left = 0
        right = len(people)-1
        people.sort()

        while left <= right:
            if people[left] + people[right] <= limit:
                boat += 1
                left += 1
                right -= 1
            elif people[left] + people[right] > limit:
                boat += 1
                right -= 1
            
        return boat
