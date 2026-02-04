class Solution:
    def isSubset(self, a, b):
        b_dict = dict.fromkeys(b, 0)
        a_dict = dict.fromkeys(a, 0)

        for num in b:
            b_dict[num] += 1
        for num in a:
            a_dict[num] += 1
        
        a = set(a)
        b = set(b)

        for num in b:
            if num in a:
                if b_dict[num] > a_dict[num]:
                    return False
            else:
                return False
        return True
