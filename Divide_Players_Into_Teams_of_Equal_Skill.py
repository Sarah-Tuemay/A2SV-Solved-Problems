class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        players_skill = skill[0] + skill[len(skill)-1]
        left = 0
        right = len(skill)-1
        ans = 0

        while left < right:
            if skill[left] + skill[right] != players_skill:
                return -1
            else:
                ans += (skill[left] * skill[right])
            left += 1
            right -= 1

        return ans
