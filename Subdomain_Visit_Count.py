from collections import defaultdict
class Solution(object):
    def subdomainVisits(self, cpdomains):
        cpdomains_dict = defaultdict(int)
        for word in cpdomains:
            index1 = word.index(" ")
            num = int(word[:index1])
            word = word[index1+1:]

            while("." in word):
                cpdomains_dict[word]+=num
                index2 = word.index(".")
                word = word[index2+1:]
            cpdomains_dict[word] += num

        ans = []

        for key in cpdomains_dict:
            word = ""
            word += str(cpdomains_dict[key])
            word += " "
            word += key
            ans.append(word)
        return ans
