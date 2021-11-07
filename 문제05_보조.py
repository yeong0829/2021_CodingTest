# 해당하는 숫자는 박수를 몇 번 쳐야 하는가?

a = 313

카운터 = 0
문자열 = str(a)
for x in 문자열:
    if x in ['3', '6', '9']:
        카운터 += 1

#1부터 해당 숫자까지 박수를 몇 번 쳐야 하는가?
# 해당하는 숫자가 박수를 몇 번 치는지
for num in range(1, a+1):
    while num:
        if num % 10 ==3 or num%10==6 or num%10==9:
            카운트 += 1
        nums = num // 10 #몫 구하기
    
print(카운터)


b =13

카운터1=0