/*
 * Author:
 * Date:
 * Name:
 */

#include <iostream>
using namespace std;
void Leap_year(){
    int year;
    cin << year;
    if (year%4 == 0){
        cout << "It's a leap year";
    }
    else {
        cout << "It's not a leap year";
    }
}
