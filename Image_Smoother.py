class Solution:
    def valid_indices(self,mat: list[list[int]],i, j):
        if i < 0  or j < 0 or j >= len(mat[0]) or i >= len(mat):
            return -1
        return mat[i][j]
    def sum_of_neghbours(self,mat: list[list[int]], i, j):
        sum = mat[i][j]
        count = 1
        if self.valid_indices(mat,i-1, j-1)!=-1:
            count += 1
            sum += self.valid_indices(mat,i-1, j-1)
        if self.valid_indices(mat,i-1, j)!=-1:
            count += 1
            sum += self.valid_indices(mat,i-1, j)
        if self.valid_indices(mat,i-1, j+1)!=-1:
            count += 1
            sum += self.valid_indices(mat,i-1, j+1)
        if self.valid_indices(mat,i, j+1)!=-1:
            count+=1
            sum += self.valid_indices(mat,i, j+1)
        if self.valid_indices(mat,i+1, j+1)!=-1:
            count+=1
            sum += self.valid_indices(mat,i+1, j+1)
        if self.valid_indices(mat,i+1, j)!=-1:
            count+=1
            sum += self.valid_indices(mat,i+1, j)
        if self.valid_indices(mat,i+1, j-1)!=-1:
            count += 1
            sum += self.valid_indices(mat,i+1, j-1)
        if self.valid_indices(mat,i, j-1)!=-1:
            count += 1
            sum += self.valid_indices(mat,i, j-1)

        return [sum, count]


    def imageSmoother(self, img: list[list[int]]) -> list[list[int]]:

        ans = deepcopy(img)
        for i in range(len(img)):
            for j in range(len(img[0])):
                ans[i][j] = self.sum_of_neghbours(img,i, j)[0] // self.sum_of_neghbours(img,i, j)[1]
        
        return ans
