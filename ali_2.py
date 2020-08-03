import sys
if __name__ == "__main__":
    # 读取第一行的n
    text = sys.stdin.readline().strip()
    m=0
    n=0
    q=0
    cs_map = []
    begin_end_command = []
    for indx,i in enumerate(range(text)):
        # 读取每一行
        line = sys.stdin.readline().strip()
        if indx==0:
            values = list(map(int, line.split()))
            m,n,q = values[0],values[1],values[2]
        elif 0<indx<=n:
            values = list(map(int, line.split()))
            cs_map.append(values)
        elif indx>n:
            values = list(map(int, line.split()))
            begin_end_command.append(values)


        # 把每一行的数字分隔后转化成int列表

    print(m,n,q)