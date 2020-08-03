# import sys
# n = int(sys.stdin.readline())
# course = []
# for line in sys.stdin:
#     line = line.split()
#     line = list(map(int,line))
#     course.append(line)

course = [[1, 4],[1 ,2],[2, 3],[3, 4]]


def count(course):
    ans = 1
    max_a = -float('inf')
    min_a = float('inf')
    for i in course:
        if i[0]<min_a:
            min_a = i[0]
        if i[1]>min_a:
            max_a = i[1]

    time = 0
    while(time<max_a+0.1):
        temp_ans = 0
        time+=0.5
        for x in course:
            if x[0] < time < x[1]:
                temp_ans += 1
        if temp_ans > ans:
            ans = temp_ans

    # for time in range(min_a,max_a+1,0.5):
    #     temp_ans = 0
    #     for x in course:
    #         if x[0]<time<x[1]:
    #             temp_ans+=1
    #     if temp_ans>ans:
    #         ans = temp_ans

    return ans

def count_2(course):

    course.sort(key=lambda x:x[0])
    print(course)

    merged = []
    for c in course:
        if not merged or merged[-1][1] <= c[0]:
            merged.append(c)
        else:
            merged[-1][1] = max(merged[-1][1],c[1])

    return merged

print(count_2(course))







print(count(course))

