class Solution:

    def rotate90(self,  mat: List[List[int]]):
        for matrix in mat:
            matrix.reverse()
        
        new_row = len(mat)
        new_col = len(mat)

        transpose = []
        for j in range(new_col):
            inside =[]
            for i in range(new_row):
                inside.append(mat[i][j])            
            transpose.append(inside)        

        return transpose


    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:



        for i in range(4):
            mat_x = self.rotate90(mat)
            mat = mat_x
            if mat == target:
                return True
        
        return False
