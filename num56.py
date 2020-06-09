class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        intervals.sort(key=lambda x: x[0])
        # print(intervals)
        index = 0
        while(index < len(intervals)-1):
            # print(intervals)
            if intervals[index][1]>=intervals[index+1][0]:
                left = max(intervals[index][1],intervals[index+1][1])
                intervals.insert(index + 2, [intervals[index][0],left])
                del intervals[index]
                del intervals[index]
            else:
                index+=1

        return intervals


if __name__ == '_main__':
    inp = [[1,3],[2,6],[8,10],[15,18]]
    S = Solution()
    S.merge(inp)
