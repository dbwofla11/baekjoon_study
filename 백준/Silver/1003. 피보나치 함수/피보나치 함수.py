# int fibonacci(int n) {
#     if (n == 0) {
#         printf("0");
#         return 0;
#     } else if (n == 1) {
#         printf("1");
#         return 1;   
#     } else {
#         return fibonacci(n‐1) + fibonacci(n‐2);
#     }
# }
# oc zc 
# f(1) = 1 0
# f(0) = 0 1



# 1003 피보나치 함수
num = int(input())

for i in range(num):
    n = int(input())
    zero_cnt = 1 
    one_cnt = 0
    tmp = 0
    for k in range(n):
        tmp = one_cnt
        one_cnt = zero_cnt + one_cnt
        zero_cnt = tmp 
    print(zero_cnt , one_cnt)
