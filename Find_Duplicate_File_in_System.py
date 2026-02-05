from collections import defaultdict
class Solution(object):
    def findDuplicate(self, paths):
        path_dict = defaultdict(set)
        for path in paths:
            index1 = path.index(" ")
            root = path[:index1]
            path = path[index1+1:]
            while("(" in path):
                index2 = path.index("(")
                index3 = path.index(")")
                content = path[index2+1:index3]
                path_dict[content].add(root+"/"+path[:index2].strip())
                path = path[index3+1:]
            
        ans = []

        for path in path_dict:
            if len(path_dict[path]) >= 2:
                ans.append(list(path_dict[path]))
            
        return ans
