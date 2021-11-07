def solution(sentence):
    str = ''
    for c in sentence:
        if c != '.' or c != ' ':
            str += c
    size = len(str)
    for i in range(size // 2):
        if str[i] != str[size - 1 - i]:
            return False
    return True


# The following is code to output testcase. The code below is correct and you shall correct solution function.
sentence1 = "never odd or even."
ret1 = solution(sentence1)

# Press Run button to receive output.
print("Solution: return value of the function is", ret1, ".")

sentence2 = "palindrome"
ret2 = solution(sentence2)

# Press Run button to receive output.
print("Solution: return value of the function is", ret2, ".")

#펠린드롬 간단하게 만들어보기
#a[0] 과 a[4]를 비교
#a[1]과 a[3]을 비교
#둘 다 참이어야만 함
#[2]는 비교 안함

a="neven"
a="seven"

#모든 조건을 만족해야만이 펠린드롬임
if (a[0] == a[4]) and (a[1] == a[3]):
    print("펠린드롬이다. ")
#g하나라도 만족하지 못하면 펠린드롬 아님
if a[0] != a[4]:
    print("펠린드롬이 아니다.")
if a[1] != a[3]:
    print("펠린드롬이 아니다.")
else:
    print("펠린드롬이다.")

a="enevene"
if (a[0] == a[4]) and (a[1] == a[3]):
    print("펠린드롬이다. ")
#g하나라도 만족하지 못하면 펠린드롬 아님
if a[0] != a[4]:
    print("펠린드롬이 아니다.")
if a[1] != a[3]:
    print("펠린드롬이 아니다.")
else:
    print("펠린드롬이다.")