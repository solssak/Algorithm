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

# 약수의 개수와 덧셈

def solution(left, right):
    answer = 0
    
    for i in range(left, right +1):
        cnt = 0
        for j in range(1, i + 1):
            if i % j == 0:
                cnt += 1
        if cnt % 2 == 0:
            answer += i
        else: 
            answer -= i
    
    return answer

# 부족한 금액 계산하기

def solution(price, money, count):
    result = 0
    
    
    for i in range(1, count + 1):
        result += price * i
        
    if money > result:
        return 0
    else:
        return result - money

# 문자열 다루기 기본

def solution(s):
    
    if len(s) == 4 or len(s) == 6:
        if s.isdigit() == True:
            return True
        else:
            return False
    else:
            return False

# 가운데 글자 가져오기

def solution(s):
    answer = ''
    
    if len(s) % 2 == 0:
        answer += s[len(s) // 2-1: len(s) // 2+1]
    if len(s) % 2 != 0:
        answer += s[len(s) // 2]
    
    return answer

# 내적

def solution(a, b):
    answer = 0
    
    for i in range(len(b)):
        answer += a[i]*b[i]
    
    return answer

# 이상한 문자 만들기

def solution(s):
    answer = ''
    a = s.split(' ')
    
    for i in a:
        for j in range(len(i)):
            if j % 2 == 0:
                answer += i[j].upper()
            else:
                answer += i[j].lower()
        answer += ' '
        
    return answer[0: -1]

# 같은 숫자는 싫어

def solution(arr):
    answer = [arr[0]]
    
    for i in range(1, len(arr)):
        if arr[i] != arr[i-1]:
            answer.append(arr[i])
    
    return answer

def solution(arr):
    answer = []

  for i in arr:
      if len(answer) ==0 or answer[-1] != i:
          answer.append(i)

    return answer
            
# 3진법 뒤집기

def solution(n):
    answer = []
    result = 0
    
    # n을 3으로 나눈 나머지 값을 []에 차례로 넣어주고? (3진법)
    while n != 0:
        answer.append(n % 3)
        n //= 3
        
    # 다시 10진법으로 전환
    for i in range(len(answer)):
        result += answer[i]*3**(len(answer) - i - 1)
                  # 전체 answer의 길이 - 현재 index - 1= 
        
    return result
# 다른 풀이 (int)
def solution(n):
    answer = ''
    result = 0
    
    # n을 3으로 나눈 나머지 값을 []에 차례로 넣어주고? (3진법)
    while n != 0:
        answer += str(n % 3)
        n //= 3
        
    # 다시 10진법으로 전환
    return  int(answer, 3)

# K번쨰 수
def solution(array, commands):
    answer = []
    
    for i in commands:
        new_list = array[i[0]-1:i[1]]
        new_list.sort()
        answer.append(new_list[i[2]-1])
        
    return answer

# 두개 뽑아서 더하기

def solution(numbers):
    answer = []

    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            if numbers[i] + numbers[j] not in answer:
                answer.append(numbers[i] + numbers[j])
    answer.sort()

    return answer

# 콜라 문제

def solution(a, b, n):
    answer = 0
    
    while n >= a:
        answer += n//a*b
        n = (n//a*b + n % a)
        
    return answer

# 푸드 파이트 대회

def solution(food):
    answer = ''
    
    for i in range(1, len(food)):
        answer += food[i] // 2 * str(i)
        
    return answer + '0' + answer[::-1]

# 가장 가까운 글자

def solution(s):
    answer = []
    new_list = {}
    
    for i in range(len(s)):
        
        if s[i] in new_list:
            answer.append(i - new_list[s[i]])
        else:
            answer.append(-1)
            
        new_list[s[i]]=i                        # 최신화
        
    return answer

# 2016년 

def solution(a, b):
    month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day = ['FRI','SAT','SUN','MON','TUE','WED','THU']
    
    return day[(sum(month[:a-1]) + b-1) % 7]
    

# 소수 만들기 

from itertools import combinations as cb

def solution(nums):
    answer = 0
    
    for i in cb(nums, 3):
        cand = sum(i)
        for j in range(2, cand):
            if cand % j == 0:
                break
        else:
            answer += 1
    return answer
    
    
# 모의고사

def solution(answers):
    answer = []
    a = [1, 2, 3, 4, 5]
    b = [2, 1, 2, 3, 2, 4, 2, 5]
    c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    scoreA = 0
    scoreB = 0
    scoreC = 0
    
    for i in range(len(answers)):
        if answers[i] == a[i%len(a)]:
            scoreA += 1
        if answers[i] == b[i%len(b)]:
            scoreB += 1
        if answers[i] == c[i%len(c)]:
            scoreC += 1
    max(scoreA, scoreB, scoreC)
    if max(scoreA, scoreB, scoreC) == scoreA:
        answer.append(1)
    if max(scoreA, scoreB, scoreC) == scoreB:
        answer.append(2)
    if max(scoreA, scoreB, scoreC) == scoreC:
        answer.append(3)
    
    return answer
    
        
        