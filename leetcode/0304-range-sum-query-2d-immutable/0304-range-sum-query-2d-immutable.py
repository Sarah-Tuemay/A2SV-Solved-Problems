class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        m = len(matrix[0])
        n = len(matrix)
        self.pre_sum = [[0] * (m + 1) for _ in range(n + 1)]

        for i in range(1, n+1):
            for j in range(1, m+1):
                self.pre_sum[i][j] = self.pre_sum[i-1][j] + self.pre_sum[i][j-1] - self.pre_sum[i-1][j-1] + self.matrix[i-1][j-1]



    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        r1 = row1+1
        c1 = col1+1
        r2 = row2+1
        c2 = col2+1

        return self.pre_sum[r2][c2] - self.pre_sum[r2][c1-1] - self.pre_sum[r1-1][c2] +self.pre_sum[r1-1][c1-1]  
