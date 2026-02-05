class Solution(object):
    def countCharacters(self, words, chars):
        chars_dict =dict.fromkeys(chars,0)
        ans = 0
        for ch in chars:
            chars_dict[ch] += 1

        for word in words:
            inside_dict = chars_dict.copy()
            flag = True
            for ch in word:
                if ch not in inside_dict:
                    flag = False
                    break
                else:
                    inside_dict[ch] -= 1
                if inside_dict[ch] == 0:
                    del inside_dict[ch]
            
            if flag:
                ans += len(word)
        return ans
                    
