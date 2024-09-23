n = int(input())
loca = list(map(int, input().split()))
time = list(map(int, input().split()))
lo_ti = [[0,0]]
time_ = 0
for i in range(n):
    lo_ti.append([time[i],loca[i]])
lo_ti.sort(key = lambda x:x[0])
lo_ti.append([0,lo_ti[-1][1]])
for i in range(n+1):
    if lo_ti[i][0] < lo_ti[i][1]:
        time_ += lo_ti[i][0]
    else:
        time_ += lo_ti[i][1]
print(time_)