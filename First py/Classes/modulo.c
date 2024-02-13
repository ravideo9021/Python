#include <stdio.h>
int main(){
    int a = 5 % 2;
    int b = -5 % 2;
    int c = 5 % -2;
    int d = -5 % -2;
    printf("%d \n%d \n%d \n%d", a, b, c, d);
}