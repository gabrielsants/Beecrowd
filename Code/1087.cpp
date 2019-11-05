#include <iostream>
using namespace std;

/*
    @Author : Gabriel Santos - Federal University of Goiás;
*/

int main() {
    int x1, y1, x2, y2, movimentos = 0, x, y;

    while((cin >> x1 >> y1 >> x2 >> y2) && (x1 != 0 || y1 != 0 || x2 != 0 || y2 != 0)){
        if( x1 == 0 && x2 == 0 && y1 == 0 && y2 == 0){
            return 0;
        } else if ( x1 == x2 && y1 == y2 ) {
            cout << movimentos << endl;
        } else if ( (x2 - x1) == -(y2 - y1) || -(x2 -x1) == -(y2-y1) || -(x2 - x1) == (y2 - y1) || (x2 - x1) == (y2 - y1) ) {
            cout << movimentos+1 << endl;
        } else if( x1 == x2 || y1 == y2 ){
            cout << movimentos+1 << endl;
        } else{
            cout << movimentos+2 << endl;
        }
    }
    return 0;
}