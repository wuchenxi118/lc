import copy
class Solution:
    def rotate(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        if len(matrix)==0:
            return matrix
        temp = copy.deepcopy(matrix)
        size = len(matrix)

        for i in range(size):
            for j in range(size):
                matrix[i][j] = temp[size-j-1][i]

        print(matrix)

    def rotate_inplace(self,matrix):
        if len(matrix)==0:
            return matrix
        size = len(matrix)
        for i in range(size):
            for j in range(i,size):
                temp = matrix[j][i]
                matrix[j][i] = matrix[i][j]
                matrix[i][j] = temp

        for i in range(size):
            for j in range(size//2):
                temp = matrix[i][j]
                matrix[i][j] = matrix[i][size-j-1]
                matrix[i][size - j - 1] = temp

        print(matrix)

if __name__ == '__main__':
    m = [[1,2,3],[4,5,6],[7,8,9]]
    S = Solution()
    S.rotate_inplace(m)
