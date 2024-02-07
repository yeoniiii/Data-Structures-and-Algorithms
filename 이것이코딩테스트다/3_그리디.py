# 그리디
## : 현재 상황에서 지금 당장 좋은 것만 고르는 방법

# [예제] 거스름돈 --------------------------------
n = 1260
count = 0

coin_types = [500, 100, 50, 10] # 큰 단위의 화폐부터 차례대로 확인하기

for coin in coin_types:
    count += n // coin # 해당 화폐로 거슬러 줄 수 있는 동전의 개수 세기
    n %= coin

print(count)


# [실전문제] 큰 수의 법칙 --------------------------------
## 내 코드
N, M, K = map(int, input().split())
arr = sorted(list(map(int, input().split())), reverse=True)
a, b = arr[:2]
sum, n = a, 1
while n < M:
    if n != 1 and n % K == 1:
        sum += b
    else:
        sum += a
    n += 1
print(sum)

## 교재 코드
# N, M, K를 공백을 기준으로 구분하여 입력 받기
n, m, k = map(int, input().split())
# N개의 수를 공백을 기준으로 구분하여 입력 받기
data = list(map(int, input().split()))

data.sort() # 입력 받은 수들 정렬하기
first = data[n - 1] # 가장 큰 수
second = data[n - 2] # 두 번째로 큰 수

# 가장 큰 수가 더해지는 횟수 계산
count = int(m / (k + 1)) * k
count += m % (k + 1)

result = 0
result += (count) * first # 가장 큰 수 더하기
result += (m - count) * second # 두 번째로 큰 수 더하기

print(result) # 최종 답안 출력


# [실전문제] 숫자 카드 게임 --------------------------------
## 내 코드
N, M = map(int, input().split())
arr = []
for i in range(N):
    arr.append(sorted(list(map(int, input().split()))))
max_num = 0
for i in range(N):
    if max_num < arr[i][0]:
        max_num = arr[i][0]
print(i)

## 교재 코드1: min()
# N, M을 공백을 기준으로 구분하여 입력 받기
n, m = map(int, input().split())

result = 0
# 한 줄씩 입력 받아 확인하기
for i in range(n):
    data = list(map(int, input().split()))
    # 현재 줄에서 '가장 작은 수' 찾기
    min_value = min(data)
    # '가장 작은 수'들 중에서 가장 큰 수 찾기
    result = max(result, min_value)

print(result) # 최종 답안 출력

## 교재 코드2: 반복문
# N, M을 공백을 기준으로 구분하여 입력 받기
n, m = map(int, input().split())

result = 0
# 한 줄씩 입력 받아 확인하기
for i in range(n):
    data = list(map(int, input().split()))
    # 현재 줄에서 '가장 작은 수' 찾기
    min_value = 10001
    for a in data:
        min_value = min(min_value, a)
    # '가장 작은 수'들 중에서 가장 큰 수 찾기
    result = max(result, min_value)

print(result) # 최종 답안 출력


# [실전문제] 1이 될 때까지 --------------------------------
## 내 코드
N, K = map(int, input().split())
ans = 0
while True:
    if N % K == 0:
        N //= K 
    else:
        N -= 1
    ans += 1
    if N == 1:
        break
print(ans)

## 교재 코드1
# N, K을 공백을 기준으로 구분하여 입력 받기
n, k = map(int, input().split())
result = 0

# N이 K 이상이라면 K로 계속 나누기
while n >= k:
    # N이 K로 나누어 떨어지지 않는다면 N에서 1씩 빼기
    while n % k != 0:
        n -= 1
        result += 1
    # K로 나누기
    n //= k
    result += 1

# 마지막으로 남은 수에 대하여 1씩 빼기
while n > 1:
    n -= 1
    result += 1

print(result)

## 교재 코드2
# N, K공백을 기준으로 구분하여 입력 받기
n, k = map(int, input().split())

result = 0

while True:
    # N이 K로 나누어 떨어지는 수가 될 때까지만 1씩 빼기
    target = (n // k) * k
    result += (n - target)
    n = target
    # N이 K보다 작을 때 (더 이상 나눌 수 없을 때) 반복문 탈출
    if n < k:
        break
    # K로 나누기
    result += 1
    n //= k

# 마지막으로 남은 수에 대하여 1씩 빼기
result += (n - 1)
print(result)