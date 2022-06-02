class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        t=[[0 for i in range(len(matrix))] for j in range(len(matrix[0]))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                t[j][i]=matrix[i][j]
        return t
