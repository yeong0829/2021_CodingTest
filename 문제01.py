# "S":5%/ "G":10%/ "V":15%

def solution(price, grade):
    if grade == "S":
        return price - price*0.05
    elif grade == "G":
        return price - price * 0.10
    elif grade == "V":
        return price - price*0.15

price1 = 2500
grade1 = "V"
ret1 = solution(price1, grade1)
print("ret1의 값은? ", ret1, ".")

price2 = 96900
grade2 = "S"
ret2 = solution(price2, grade2)
print("ret2의 값은?", ret2, ".")