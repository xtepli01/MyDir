#include <iostream>
using namespace std;

int main(){

    int n;
    cin >> n;

    int h, m1, m2, s1, s2;

    h = ( n % 3600) / 24;

    cout << h;
    return 0;
}