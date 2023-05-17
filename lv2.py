# 이진 변환 반복하기

def solution(s):
    answer = []
    cnt_1 = 0
    cnt_2 = 0
    
    while s != '1':
        cnt_2 += s.count('0')
        s = s.replace('0', '')
        s = bin(len(s))[2:]
        cnt_1 += 1
    
    answer = [cnt_1, cnt_2]
    
    return answer


# 올바른 괄호

def solution(s):
    Stack = []
    
    for bracket in s:
        if bracket == "(":
            Stack.append(bracket)
        elif bracket == ')':
            if Stack and Stack[-1] == '(':
                del Stack[-1]
            else:
                Stack.append(bracket)
    print(Stack)
    return False if Stack else True

# 최솟값 만들기

def solution(A,B):
    answer = 0
    
    A_sort = sorted(A)
    B_sort = sorted(B, reverse=True)
    
    for i in range(len(A)):
        answer += A_sort[i] * B_sort[i]
        
    return answer
    
# 다음 큰 숫자
# while
def solution(n):
    answer = 0
    
    count_one = bin(n)[2:].count('1')
    
    while True:
        n = n + 1
        i_count_one = bin(n)[2:].count('1')
        if count_one == i_count_one:
            answer += n
            break
    return answer
# for
def solution(n):
    answer = 0
    
    count_one = bin(n)[2:].count('1')
    
    for i in range(n+1, 1000001):
        i_count_one = bin(i)[2:].count('1')
        if count_one == i_count_one:
            answer += i
            break

    return answer

# 숫자의 표현

def solution(n):
    answer = 0

    for i in range(1, n+1):
        result = 0
        for j in range(i, n+1):
            result += j
            if result == n:
                answer += 1
            elif result > n:
                break
    
    return answer