// Task1: Input quantity of seconds. Targer- calculate how many hours, minutes, seconds.

#include <iostream>
using namespace std;

int main(){

    int seconds;
    cin >> seconds;
    
    int hour = (seconds / 3600) % 24;
    int min1 = ((seconds % 3600) / 600);
    int min2 = ((seconds % 3600) % 600) / 60;
    int sec1 = ((seconds % 60) / 10);
    int sec2 = ((seconds % 60) % 10);
    
    cout << hour << ":" << min1 << min2 << ":"  << sec1 << sec2;
    
    return 0;
}