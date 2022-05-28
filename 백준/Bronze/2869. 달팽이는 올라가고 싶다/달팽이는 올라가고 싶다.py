#삼항연산자 예제
# 반환값 if 조건 else 반환값(else)
# 예시 
# a = 10
# b = 0
# c = ("맞습니다" if a > b else 0)
# print(c)
import sys
a , b , v = map(int , sys.stdin.readline().split())
result = (v-b)/(a-b)
print(int(result) if int(result) == result else int(result) + 1 ) # 올림처리 
