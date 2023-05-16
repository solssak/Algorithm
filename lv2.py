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
    