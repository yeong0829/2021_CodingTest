# 1부터 nuber까지 총 몇번 박수를 치는지 반환
def solution(number):
   count = 0
   for i in range(1, number + 1):  # for(int i=1; i<number+1)
       current = i
       temp = count
       while current != 0:
           if  current % 10 ==3 or current % 10 ==6 or current %10 ==9:
               count += 1
               print("pair", end = '') # 디버깅을 위한 출력(없어도 무관)
           current = current // 10
       if temp == count:
           print(i, end = '') # 디버깅을 위한 출력(없어도 무관)
       print(" ", end = '') # 디버깅을 위한 출력(없어도 무관)
   print("") # 디버깅을 위한 출력(없어도 무관)
   return count
