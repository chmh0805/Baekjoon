C = int(input())
for _ in range (C):
    cnt = 0
    score = list(map(int,input().split()))
    N = int(score[0])
    avg = sum(score[1:])/N
    for i in range (1, N+1):
        if score[i] > avg :
            cnt += 1
    print("%.3f%%"%round(cnt/N*100,3))
