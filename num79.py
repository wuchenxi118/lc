class Solution:
    def __init__(self):
        self.used = []
        self.flag = False
        self.directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]

    def exist(self, board, word):
        m = len(board)
        n = len(board[0])
        self.used = [[False]*len(board[0]) for _ in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]==word[0]:
                    if self.backtrack(i,j,m,n,0,word,board):
                        return True

        return False


    def backtrack(self,now_x,now_y,m,n,word_index,word,board):
        # print(self.used)
        # print(now_x,now_y,word_index,len(word))

        if word_index == len(word)-1:
            if board[now_x][now_y]==word[word_index]:
                return True

        if board[now_x][now_y] == word[word_index]:
            self.used[now_x][now_y] = True
            for dir in self.directions:
                next_x = now_x + dir[0]
                next_y = now_y + dir[1]
                if self.index_inlegal(next_x,next_y,m,n) \
                    and self.used[next_x][next_y]==False \
                    and self.backtrack(next_x,next_y,m,n,word_index+1,word,board):
                    return True
            self.used[now_x][now_y] = False

        return False

    def index_inlegal(self,next_x,next_y,m,n):
        if 0<=next_x<m and 0<=next_y<n:
            return True
        else:
            return False




if __name__ == '__main__':
    board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]

    word = "ABCB"
    S = Solution()
    print(S.exist(board,word))