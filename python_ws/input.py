# Description: 입력을 받는 방법을 정리한 파일

# 1개의 숫자 입력
# 13
N = int(input())

# 2개의 숫자 입력
# 13, 14
a, b = map(int, input().split())

# 리스트 입력
# [13, 14, 15 ...]
A = list(map(int, input().split()))

# 2차원 리스트 입력
A = []
for i in range(N):
    A.append(list(map(int, input().split())))

# 숫자 입력들
B = []
for i in range(N):
    B.append(int(input()))

# 문자 입력들
C = []
for i in range(N):
    C.append(input())