max = 0 # 맥스값 잡기
temp = 0 # 저장소
temp2 = 0
for i in range(4): # 4번 반복하기
    a , b = map(int, input().split(" "))# a , b 4번 반복해서 받기 
    temp = temp - a + b # 0 - 빠지는 사람 수 + 들어온(새로 탑승한 사람 수) 사람 수 = 저장소 값
    if max < temp: # 만약 맥스값이(0) 저장소 값보다 작다면
        max = temp # 맥스값 = 저장소 값

print(max)# 맥스값(저장소 값) 출력하기
