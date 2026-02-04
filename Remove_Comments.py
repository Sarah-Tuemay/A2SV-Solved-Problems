class Solution(object):
    def removeComments(self, source):
        ans = []
        comment = False
        s = ""
        for word in source:
            i = 0
            while i < len(word):
                if not comment and i+1 < len(word) and word[i] + word[i+1] == "//":
                    break
                elif i+1 < len(word) and word[i] + word[i+1] == "/*" and not comment:
                    comment = True
                    i+=2
                elif i+1 < len(word) and word[i] + word[i+1] == "*/" and comment:
                    comment = False
                    i+=2
                elif not comment:
                    s+=word[i]
                    i+=1
                else:
                    i+=1
  
            if s != "" and not comment:
                ans.append(s)
                s = ""
        return ans
