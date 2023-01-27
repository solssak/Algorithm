# 중앙값 구하기
def solution(a):
    a.sort() # 오름차순
    center_idx = len(a)//2 # 리스트 개수를 2로 나누어줌 (중간 값)
    return a[center_idx] # 중간 값을 리턴

    # 위 코드는 리스트가 홀수일 때만 적용되는 경우


# 문자열 안에 문자열
def solution(str1, str2):
    return 1 if str2 in str1 else 2

#    if str2 in str1:
#       return 1
#    else: return 2
    