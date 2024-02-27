# 다이나믹 프로그래밍 Dynamic Programming
# [이코테] 피보나치 수열 --------------------------------
## Top-Down (메모이제이션)
d = [0] * 100

def Fibonacci(x):
    if x == 1 or x == 2:
        1
    if d[x] != 0:
        return d[x]
    d[x] = Fibonacci(x-1) + Fibonacci(x-2)
    return d[x]

print(Fibonacci(99))

## Bottom-Up (반복)
n = 99
d = [0] * (n+1)
d[1] = d[2] = 1

for i in range(3, n+1):
    d[i] = d[i-1] + d[i-2]

print(d[n])


# [실전 문제] 1로 만들기 --------------------------------
x = int(input())

d = [0] * 30001

for i in range(2, x+1):
    d[i] = d[i - 1] + 1
    if i % 2 == 0:
        d[i] = min(d[i], d[i//2] + 1)
    if i % 3 == 0:
        d[i] = min(d[i], d[i//3] + 1)
    if i % 5 == 0:
        d[i] = min(d[i], d[i//5] + 1)

print(d[x])


# [실전 문제] 개미 전사 --------------------------------
N = int(input())
arr = list(map(int, input().split()))

d = [0] * 100
d[0] = arr[0]
d[1] = max(arr[0], arr[1])

for i in range(2, N):
    d[i] = max(d[i-1], d[i-2] + arr[i])

print(d[N-1])


# [실전 문제] 바닥 공사 --------------------------------
N = int(input())

d = [0] * 1001
d[0] = 1
d[1] = d[0] + 2

for i in range(2, N):
    d[i] = (d[i-1] + d[i-2] * 2) % 796796

print(d[N])


# [실전 문제] 효율적인 화폐 구성 --------------------------------
n, m = map(int, input().split())

array = []
for i in range(n):
    array.append(int(input()))

d = [10001] * (m + 1)
d[0] = 0
for i in range(n):
    for j in range(array[i], m + 1):
        if d[j - array[i]] != 10001: # (i - k)원을 만드는 방법이 존재하는 경우
            d[j] = min(d[j], d[j - array[i]] + 1)

if d[m] == 10001: # 최종적으로 M원을 만드는 방법이 없는 경우
    print(-1)
else:
    print(d[m])

    
## [백준] 9461 파도반 수열 --------------------------------
P = [0] * 101
P[1] = 1
P[2] = 1
P[3] = 1
for i in range(4, 101):
    P[i] = max(P[i-3] + P[i-2], P[i-1])
    
T = int(input())
for t in range(T):
    print(P[int(input())])

    
## [백준] 1904 01타일 --------------------------------
N = int(input())
d = [0] * (N+1)
d[0] = 1
d[1] = 1

if 2 <= N+1:
    for i in range(2, N+1):
        d[i] = (d[i-2] + d[i-1]) % 15746
    
print(d[N])

    
## [백준] 9184 신나는 함수 실행 --------------------------------
d = [[[0]*(21) for _ in range(21)] for _ in range(21)]

for i in range(21):
    for j in range(21):
        for k in range(21):
            if i<=0 or j<=0 or k<=0:
                d[i][j][k] = 1
            elif i<j<k:
                d[i][j][k] = d[i][j][k-1] + d[i][j-1][k-1] - d[i][j-1][k]
            else:
                d[i][j][k] = d[i-1][j][k] + d[i-1][j-1][k] + d[i-1][j][k-1] - d[i-1][j-1][k-1]
                
while True:
    a, b, c = map(int, input().split())
    if a==b==c==-1:
        break
    if a<=0 or b<=0 or c<=0:
        ans = 1
    elif a>20 or b>20 or c>20:
        ans = d[20][20][20]
    else:
        ans = d[a][b][c]
    print('w(', a, ', ', b, ', ', c, ') = ', ans, sep='')