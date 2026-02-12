class Solution:
    def transpose(self, matrix: list[list[int]]) -> list[list[int]]:
        ans = []
        for i in range(len(matrix[0])):
            inside_matrix = []
            for j in range(len(matrix)):
                inside_matrix.append(matrix[j][i])
            
            ans.append(inside_matrix)
        
        return ans
