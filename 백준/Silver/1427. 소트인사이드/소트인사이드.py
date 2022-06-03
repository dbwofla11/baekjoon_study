def select(list):
    
    for i in range(len(list)):
        min_idx = i # 탐색 범위를 좁히기 위해서 인덱스를 재설정     #ex)  2 1 4 3 
        for k in range(i+1 , len(list)):    # 재설정한 것 부터 끝까지 
            if list[min_idx] < list[k]:      # 여기서 min_idx는 i 그니까 처음 부터 비교함 
                min_idx = k # min_idx를 업데이트 이는 최소값 업데이트고 list[min_idx] < list[k]는 최대값 업데이트 
        
        list[i] , list[min_idx] = list[min_idx] , list[i] # c나 다른 언어에서는 저장소가 필요하지만 파이썬은 없어도 됨 




# 함수에 대한 설명 : 바깥쪽 for문에서는 배열을 배열길이 만큼 읽고 스와핑 
# 안쪽 for문에서는 정렬할 인덱스를 탐색하고 업데이트 이게 오름차순 내림차순 다 가능   

a = input()
numlst = [int(i) for i in a] # 문자열을 리스트로 변환하는거 1 

select(numlst)
for k in numlst:
    print(k, end='')
# numlst2 = []  # 문자열을 리스트로 변환하는거 2 
# for i in a :

#     numlst2.append(i)

