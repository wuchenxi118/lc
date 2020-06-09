
#暴力解
class Solution:
    def largestRectangleArea(self, heights):
        if not heights:
            return 0

        res_list = []

        for i in range(len(heights)):
            now_h = heights[i]
            r_j = i
            while(r_j+1<len(heights) and heights[r_j+1]>=now_h):
                r_j += 1
            l_j = i
            while(l_j-1>=0 and heights[l_j-1]>=now_h):
                l_j -= 1
            now_area = now_h*(r_j-l_j+1)
            res_list.append(now_area)

        return max(res_list)



if __name__ == '__main__':
    height = [2, 1, 5, 6, 2, 3]
    S = Solution()
    print(S.largestRectangleArea(height))