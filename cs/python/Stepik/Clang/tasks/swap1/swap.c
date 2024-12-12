#include <stdio.h>
void swap(int *pa, int *pb) {
     int t = *pa;
     *pa = *pb;
     *pb = t; // pa → a: 21 pb → b: 17
// t: 21
// pa → a: 17 pb → b: 17
// pa → a: 17 pb → b: 21
}
int main(void) {
    int a = 21;
    int b = 17;
    swap(&a, &b);
    printf("a = %d, b = %d\n", a, b);
    return 0;
// a: 21
// b: 17
// a: 17 b: 21
}