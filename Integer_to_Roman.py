class Solution(object):
    def intToRoman(self, num):
        symbol_value = {
            1000: 'M',
            500: "D",
            100: "C",
            50: "L",
            10: "X",
            5: "V",
            1: "I",
        }
        ans = ""
        for key in symbol_value:
            if num == 0:
                break
            while num >= key:
                ans+=symbol_value[key]
                num -= key
            
            if str(num)[0] == "9":
                if num >= 900:
                    ans += symbol_value[100]
                    ans += symbol_value[1000]
                    num -= 900
                elif num >= 90:
                    ans += symbol_value[10]
                    ans += symbol_value[100]
                    num -= 90
                elif num == 9:
                    ans += symbol_value[1]     
                    ans += symbol_value[10]
                    num -= 9       
            elif str(num)[0] == "4":
                if num >= 400:
                    ans += symbol_value[100]
                    ans+= symbol_value[500]
                    num -= 400
                elif num >= 40:
                    ans += symbol_value[10]
                    ans += symbol_value[50]
                    num -= 40
                elif num == 4:
                    ans += symbol_value[1]
                    ans += symbol_value[5]
                    num -= 4
            else:
                continue
        return ans
