# 1.길이가 n개인 리스트의 요소(element/item)들을 0으로 초기화하기
#
# n = 7
# result1 = [0]*n
# print(result1)
#
# result2 = [0 for _ in rang(n)]
# print(result2)


#2.원소의 갯수를 카운터하기
#ex) [1, 2, 2, 2, 3, 1, 1, 3, 2] 에서  2의 갯수를 카운팅

# arr = [1, 2, 2, 2, 3, 1, 1, 3, 2]
# # count 변수를 0으로 초기화
# count = 0
# # arr의 모든 요소들에 대해서
# for x in arr:
# # 각각의 원소가 2이면
#     if x == 2:
# # count에 1을 증가
#     count += 1
#
# print(count)



#4. Bubble Sort 구현(버블소트가 무엇인지 말할 수 있어야 함)

arr = [8, 5, 6, 3, 4]

for i in range(0, 4):
    for j in range(len(arr) -i -2):
        if arr[j]>arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]



# 6. 어떤 문자열에 해당 단어가 몇개 있는지 카운팅
# ex) "ILOVKEFLOVEE" 에서 "LOV"가 몇개 있는지 카운팅

string = "ILOVKEFLOVEE"

print(string.count(find))
find="LOV"
count = 0
for i in range(len(string)):
    #첫 글자가 "L"인 경우 and 찾아야하는 끝 글자의 범위체크
    if string[i] == find[0] and i+len(find) <= len(string):
        # 첫 글자가 "O"인 경우
        if string[i+1] == find[1]:
            # 첫 글자가 "V"인 경우
            if string[i+2] == find[2]:
                count += 1



# 7. 리스트에서 특정 원소만 추출하기
# ex) [1,2,2,2,3,1,1,3,2]에서  2를 제외한 나머지만 추출하기
