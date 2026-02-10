class Solution(object):
    def romanToInt(self, s):
        roman_to_int = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
            "IV": 4,
            "IX": 9,
            "XL": 40,
            "XC": 90,
            "CD": 400,
            "CM": 900,
        }
        ans = 0
        i = 0
        while i < len(s):
            if i + 1 <= len(s) - 1 and s[i] + s[i + 1] == "IV":
                ans += 4
                i += 2
            elif i + 1 <= len(s) - 1 and s[i] + s[i + 1] == "IX":
                ans += 9
                i += 2
            elif i + 1 <= len(s) - 1 and s[i] + s[i + 1] == "XL":
                ans += 40
                i += 2
            elif i + 1 <= len(s) - 1 and s[i] + s[i + 1] == "XC":
                ans += 90
                i += 2
            elif i + 1 <= len(s) - 1 and s[i] + s[i + 1] == "CD":
                ans += 400
                i += 2
            elif i + 1 <= len(s) - 1 and s[i] + s[i + 1] == "CM":
                ans += 900
                i += 2
            else:
                ans += roman_to_int[s[i]]
                i += 1
        return ans
