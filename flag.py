leng = 5
if leng == 1:
    print(0)
num = [4,1,2,5,3]
num = sorted(num)
m = {}
for i in range(len(num)):
    m[num[i]] = i

loops = 0
flag = [[False] * leng]
for i in range(leng):
    if not flag[i]:
        j = i
        while not flag[j]:
            flag[j] = True
            j = m[num[j]]
        loops += 1

print(leng - loops)