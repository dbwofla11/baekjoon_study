#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

// & 이름 = 앤퍼센드
// \n = 줄 넘기기

int main(){

	int n;
	scanf("%d", &n);
	int list[1000]; 
	int cnt = 0;

	for (int i = 0; i < n ; i++) {
		scanf("%d", &list[i]);
	}
	
	int v;
	scanf("%d", &v);

	for (int i = 0; i < n; i++) {
		if (v == list[i]) {
			cnt += 1;
		}
	}
	printf("%d", cnt);
}