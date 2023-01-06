chess = [1,1,2,2,2,8] # 원래꺼
white = list(map(int , input().split())) # 내가 입력하는 체스 

for i in range(6): # 체스의 반복문 
  print( chess[i] - white[i] , end = " ") #출력 


### 원래 리스트를 읽어 오려면 for문을 돌려서 인덱스를 굴림 ( 0 ~ 5 ) 이 인덱스로 리스트에서 인덱스에 맞는 요소를 가져오는 거임
