class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        pre_sum = [0] * len(s)

        for shift in shifts:
            if shift[2] == 0:
                pre_sum[shift[0]] -= 1
                if shift[1] != len(s)-1:
                    pre_sum[shift[1]+1] +=1
            else:
                pre_sum[shift[0]] += 1
                if shift[1] != len(s)-1:
                    pre_sum[shift[1]+1] -= 1
        
        sum1 = 0
        for i in range(len(pre_sum)):
            sum1+=pre_sum[i]
            pre_sum[i] = sum1

        ans = ""

        for i in range(len(s)):
            ans += chr(ord('a') + ((ord(s[i]) - ord('a') + pre_sum[i])%26))
        
        return ans