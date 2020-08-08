from typing import *
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        first_time = []
        last_time = []
        for pair in intervals:
            first_time.append(pair[0])
            last_time.append(pair[1])
        first_time.sort()
        last_time.sort()
        begin_point = 0
        end_point = 0
        used_room = 0
        while(begin_point<len(first_time)):
            if first_time[begin_point]<last_time[end_point]:
                used_room+=1
            else:
                end_point+=1
            begin_point += 1
        return used_room




if __name__ == '__main__':
    inp = [[0, 30],[5, 10],[15, 20],[16,30]]
    S = Solution()
    print(S.minMeetingRooms(inp))
