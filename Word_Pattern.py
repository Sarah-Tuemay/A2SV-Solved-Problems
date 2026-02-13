class Solution(object):
    def wordPattern(self, pattern, s):
        s_list = s.split()
        my_dict = {}
        my_set = set()
        if len(pattern) != len(s_list):
            return False
        for i in range(len(pattern)):
            if pattern[i] in my_dict:
                if s_list[i] != my_dict[pattern[i]]:
                    return False
            else:
                if s_list[i] not in my_set:
                    my_dict[pattern[i]] = s_list[i]
                    my_set.add(s_list[i])
                else:
                    return False
        
        return True
