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