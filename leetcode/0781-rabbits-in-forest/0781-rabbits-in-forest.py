class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        answers_c = Counter(answers)
        ans = 0
        for key in answers_c:
            ans += key+1 if answers_c[key] <= key+1 else ceil(answers_c[key]/(key+1))*(key+1)
        
        return ans