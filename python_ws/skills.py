


# 중복 제거, 순서 유지
C = list(dict.fromkeys(C))

# 오름차순 정렬
C.sort()

# A를 A[0]을 기준으로 정렬, 나머지는 원래 순서로
A.sort(key=lambda x: (x[0]))

# A를 A[0]을 기준으로 정렬하고, A[0]이 같으면 A[1]을 기준으로 정렬
A.sort(key=lambda x: (x[0], x[1]))
