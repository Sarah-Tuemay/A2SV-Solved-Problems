class Solution(object):
    def longestCommonPrefix(self, strs):
        firstWord = strs[0]
        prefix = ""
        for i in range(len(firstWord)):
            found = True
            for j in range(len(strs)):
                if i < len(strs[j]):
                    if firstWord[i] != strs[j][i]:
                        found = False
                        break
                else:
                    found = False

            if found:
                prefix += firstWord[i]
            else:
                break

        return prefix
