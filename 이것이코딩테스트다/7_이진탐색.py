# 순차 탐색 Sequential Search
## : 리스트 안에 있는 특정한 데이터를 찾기 위해 앞에서부터 데이터를 하나씩 차례대로 확인하는 방법
def sequential_search(n, target, array):
    # 각 원소를 하나씩 확인하며
    for i in range(n):
        # 현재의 원소가 찾고자 하는 원소와 동일한 경우
        if array[i] == target:
            return i + 1 # 현재의 위치 반환 (인덱스는 0부터 시작하므로 1 더하기)
    return -1 # 원소를 찾지 못한 경우 -1 반환

print("생성할 원소 개수를 입력한 다음 한 칸 띄고 찾을 문자열을 입력하세요.")
input_data = input().split()
n = int(input_data[0]) # 원소의 개수
target = input_data[1] # 찾고자 하는 문자열

print("앞서 적은 원소 개수만큼 문자열을 입력하세요. 구분은 띄어쓰기 한 칸으로 합니다.")  
array = input().split()

# 순차 탐색 수행 결과 출력
print(sequential_search(n, target, array))


# 이진 탐색 Binary Search
## : 탐색 범위를 반으로 좁혀가며 빠르게 탐색하는 알고리즘
### 1. 재귀함수
def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    # 찾은 경우 중간점 인덱스 반환
    if array[mid] == target:
        return mid
    # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
    else:
        return binary_search(array, target, mid + 1, end)

# n(원소의 개수)과 target(찾고자 하는 값)을 입력 받기
n, target = list(map(int, input().split()))
# 전체 원소 입력 받기
array = list(map(int, input().split()))

# 이진 탐색 수행 결과 출력
result = binary_search(array, target, 0, n - 1)
if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print(result + 1)
    

### 2. 반복문
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        # 찾은 경우 중간점 인덱스 반환
        if array[mid] == target:
            return mid
        # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
        elif array[mid] > target:
            end = mid - 1
        # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
        else:
            start = mid + 1
    return None

# n(원소의 개수)과 target(찾고자 하는 값)을 입력 받기
n, target = list(map(int, input().split()))
# 전체 원소 입력 받기
array = list(map(int, input().split()))

# 이진 탐색 수행 결과 출력
result = binary_search(array, target, 0, n - 1)
if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print(result + 1)



# [실전 문제] 부품 찾기 --------------------------------
## 내 코드 (반복문)
N = int(input())
dong = sorted(list(map(int, input().split())))
M = int(input())
cust = list(map(int, input().split()))

def binary_search(arr, n):
    start, end = 0, len(arr)-1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == n:
            return 'yes'
        elif arr[mid] < n:
            start = mid + 1
        else: # arr[mid] > n
            end = mid - 1
    return 'no'

ans = []
for n in cust:
    yn = binary_search(dong, n)
    ans.append(yn)
    
print(' '.join(ans))


## 교재 코드 (계수 정렬)
N = int(input())
arr = [0] * 1000001

for i in input().split():
    arr[int(i)] = 1

M = int(input())
x = list(map(int, input().split()))

for i in x:
    if arr[i] == 1:
        print('yes', end = ' ')
    else:
        print('no', end = ' ')


## 교재 코드 (집합 자료형)
N = int(input())
dong = set(map(int, input().split()))
M = int(input())
cust = list(map(int, input().split()))

for i in cust:
    if i in dong:
        print('yes', end = ' ')
    else:
        print('no', end = ' ')


# [실전 문제] 떡볶이 떡 만들기 --------------------------------
## 내 코드
N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))

def ddug(arr, m):
    start, end = 0, max(arr)
    while start <= end:
        mid = (start + end) // 2
        dd = 0
        for i in arr:
            if i > mid:
                dd += (i-mid)
        if dd == m:
            return dd
        elif dd > m:
            start = mid + 1
        else: # dd < m
            end = mid - 1

ddug(arr, M)

## 교재 코드
# 떡의 개수(N)와 요청한 떡의 길이(M)을 입력
n, m = list(map(int, input().split(' ')))
# 각 떡의 개별 높이 정보를 입력
array = list(map(int, input().split()))

# 이진 탐색을 위한 시작점과 끝점 설정
start = 0
end = max(array)

# 이진 탐색 수행 (반복적)
result = 0
while(start <= end):
    total = 0
    mid = (start + end) // 2
    for x in array:
        # 잘랐을 때의 떡볶이 양 계산
        if x > mid:
            total += x - mid
    # 떡볶이 양이 부족한 경우 더 많이 자르기 (오른쪽 부분 탐색)
    if total < m:
        end = mid - 1
    # 떡볶이 양이 충분한 경우 덜 자르기 (왼쪽 부분 탐색)
    else:
        result = mid # 최대한 덜 잘랐을 때가 정답이므로, 여기에서 result에 기록
        start = mid + 1

# 정답 출력
print(result)


# [백준] 1920 수 찾기 --------------------------------
N = int(input())
A = sorted(list(map(int, input().split())))
M = int(input())
B = list(map(int, input().split()))

def binary_search(arr, n):
    start, end = 0, len(arr)-1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == n:
            return 1
        elif arr[mid] < n:
            start = mid + 1
        else:
            end = mid - 1
    return 0

for b in B:
    print(binary_search(A, b))


## [백준] 10816 숫자카드 2 --------------------------------
N = int(input())
sang = sorted(list(map(int, input().split())))
M = int(input())
card = list(map(int, input().split()))

sang_dict = {}
for s in sang:
    if s in sang_dict:
        sang_dict[s] += 1
    else:
        sang_dict[s] = 1

def num_card(arr, n, start, end):
    if start > end:
        return 0
    
    mid = (start + end) // 2
    if arr[mid] == n:
        return sang_dict[n]
    elif arr[mid] < n:
        return num_card(arr, n, mid+1, end)
    else: # arr_set[mid] > n
        return num_card(arr, n, start, mid-1)

ans = []
for c in card:
    ans.append(num_card(sang, c, 0, len(sang)-1))

print(*ans)


## [백준] 1654 랜선 자르기 --------------------------------
import sys
input = lambda: sys.stdin.readline().rstrip()

K, N = map(int, input().split())
arr = sorted([int(input()) for _ in range(K)])

def max_len(arr, n):
    start, end = 1, max(arr)      # 길이이므로 [1, max(arr)]
    
    while start <= end:           # start > end 되면 멈춤
        mid = (start + end) // 2
        num = 0
        for i in arr:
            num += i // mid       # i랑 mid 대소관계 체크할 필요 없음 (몫이니까)
                
        if num >= n:              # (1) 개수가 N개보다 많거나 같으면 최대 길이를 알아내기 위해 개수를 줄여야 함
            start = mid + 1       # -> 나눠주는 수인 mid를 키워야 함
        else: # num < n           # (2) 개수가 N개보다 적으면 개수를 늘려야 함
            end = mid - 1         # -> 나눠주는 수인 mid를 줄여야 함
    return end                    # ∴ end가 N개를 만들 수 있는 최대 길이

print(max_len(arr, N))


## [백준] 2805 나무 자르기 --------------------------------
N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))

def max_len(arr, n):
    start, end = 1, max(arr)
    
    while start <= end:
        mid = (start + end) // 2
        l = 0
   
        for a in arr:
            if a > mid:
                l += (a-mid)
        if l >= M:    
            start = mid + 1
        else:
            end = mid - 1

    return end

print(max_len(arr, M))