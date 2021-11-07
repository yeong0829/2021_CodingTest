#문제 1
def solution1(scores):
    a = sum(scores) - max(scores) - min(scores)
    #전제 객수 -2 만큼 나눈다(나머지 제거_
    answer = a // (len(scores)-2)
    return answer

scores1 = [35, 28, 98, 34, 20, 50, 85, 74, 71, 7]
ret1 = solution1(scores1)

#문제 2
def soluction2(a, b):
    answer = 0
    for i in range(1, b+1):
        if a * i % b == 0:
            answer = a * i
            break
    return answer

a = 4
b = 6
ret = soluction2(a, b)