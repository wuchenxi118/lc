import sys
for line in sys.stdin:
    a = line.split()
    n = int(a[0])
    color_num = int(a[1])
    ans = 0
    for i in range(n+1):
        if i==0:
            ans+=1
        elif i!=n:
            ans+=n*(color_num**i)
        elif i==n:
            ans+=color_num**n
    if ans>1e9:
        print('yes')

    print(int(ans%(1e9+7)))

