# 평균 구하기

def solution(arr):
    answer = 0
    answer = sum(arr) / len(arr)
    return answer

# 다른 풀이

def solution(arr):
    answer = 0
    
    for i in arr:
        answer += i
    
    return answer / len(arr)

# 짝수와 홀수

def solution(num):
    answer = ''
    if num % 2 == 0:
        answer += "Even"
    else:
        answer += "Odd"
    return answer

# 약수의 합 range!

def solution(n):
    answer = 0
    for i in range(1, n+1):
        if n % i == 0:
            answer += i
        
    return answer

# 자릿수 더하기

# n => 123
# str(n) => 123
# list(str(n)) => ['1', '2', '3']
# list(map(int, str(n))) => [1, 2, 3]

def solution(n):
    answer = 0
    input = list(map(int, str(n)))
    for i in input:
        answer += i
    return answer


# 나머지가 1이 되는 수 찾기 << 다시보기

def solution(n):
    answer = 0
    for i in range(1, n):
        if n % i == 1:        
            return i
        
# x만큼 간격이 있는 n개의 숫자 << 다시보기

def solution(x, n):
    answer = []
    for i in range(1, n+1):
        answer.append(i * x)
    return answer

# 문자열 내 p와 y의 개수

def solution(s):
    answer = True
    a = s.lower()
    if a.count('p') == a.count('y'):  
        return True
    else:
        return False
    
# 정수 제곱근 판별

from math import sqrt 

def solution(n):
    answer = 0
    x = sqrt(n)
    
    if int(x) == x:
        answer = (x + 1) * (x + 1)
    else:
        answer = -1
            
    return answer

# 자연수 뒤집어 배열로 만들기 << 다시 풀기

def solution(n):
    answer = []
    answer = list(map(int, reversed(str(n))))
    
    return answer

# 문자열을 정수로 바꾸기

def solution(s):
    # 문자열 숫자로 반환하기
    return int(s)
    
# 정수 내림차순으로 배치하기

def solution(n):
    answer = 0
    answer = sorted(list(str(n)), reverse=True)
    
    return int(''.join(answer))

# 하샤드 수

def solution(x):
    a = str(x)
    s = 0
    
    
    for i in a:
        s += int(i)
    
    if x % s == 0:
        return True
    else:
        return False
    
# 두 정수 사이의 합

def solution(a, b):
    answer = 0
    # swap
    # if a > b:
    #     a, b = b, a
    
    for i in range(min(a, b),max(a, b)+1):
        answer += i
        
        
    return answer

# 콜라츠 추측

def solution(num):
    answer = 0

    while num != 1:
        if num % 2 == 0:
            num /= 2 
        else:
            num = num * 3 + 1
        answer += 1
        if answer > 500:
            return -1
        
    return answer

# 서울에서 김서방 찾기

def solution(seoul):
    answer = ''
    a = seoul.index('Kim')
    
    return f'김서방은 {a}에 있다'

# 나누어 떨어지는 숫자 배열

def solution(arr, divisor):
    answer = []
    
    for i in arr:
        if i % divisor == 0:
            answer.append(i)
    if len(answer) == 0:
        answer.append(-1)
    
    return sorted(answer)

# 핸드폰 번호 가리기

def solution(phone_number):
    answer = ''
    for i in phone_number[:-4]:
        answer += '*'
    return answer + phone_number[-4:]

# 음양 더하기

def solution(absolutes, signs):
    answer = 123456789

    for i in range(len(signs)):
        if signs[i] == False:
            absolutes[i] *= -1
            
    return sum(absolutes)

# 제일 작은 수 제거하기

def solution(arr):
    answer = []
    
    arr.remove(min(arr))
    if len(arr) == 0:
        arr.append(-1)
            
    return arr