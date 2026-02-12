class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        left = 0
        right = len(matrix) - 1

        while left < right:
            matrix[left], matrix[right] = matrix[right], matrix[left]
            left += 1
            right -= 1
        changed = set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if (i, j) not in changed:
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
                    changed.add((i, j))
                    changed.add((j, i))
