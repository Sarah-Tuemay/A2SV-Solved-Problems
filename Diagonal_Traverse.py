from collections import defaultdict
class Solution:
    def findDiagonalOrder(self, mat: list[list[int]]) -> list[int]:
        my_dict = defaultdict(list)

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                my_dict[i+j].append(mat[i][j])
        

        ans = []
        signal = 1
        for key in my_dict:
            if signal == 0:
                ans.extend(my_dict[key])
                signal = 1
            elif signal == 1:
                my_dict[key].reverse()
                ans.extend(my_dict[key])
                signal = 0
        
        return ans
