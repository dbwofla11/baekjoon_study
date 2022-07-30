#include<stdio.h>

int main(){
    int a ; int b ;
    scanf("%d %d",&a,&b);
    if (a == b) {
        printf("==");
    }
    if( a > b ){
        printf(">");
    }
    if( a < b ){
        printf("<");
    }
    
}