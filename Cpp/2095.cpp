#include <iostream>
#include <algorithm>
#include <set>
using namespace std;

//10⁵
#define MAX 100000

/*
    @Author : Gabriel Santos - Federal University of Goiás;
*/

int main() {

    int S, negoliano[MAX], quadradolandia[MAX], i, res;

    cin >> S;

    for( i = 0; i < S; i++ ) {
        cin >> quadradolandia[i];
    }
    
    for( i = 0; i < S; i++ ) {
        cin >> negoliano[i];
    }
    
    sort( quadradolandia, quadradolandia + S );
    sort( negoliano, negoliano + S );
    for ( res = 0, i = 0; i < S; i++ ) { 
        if(quadradolandia[res] < negoliano[i])
            res++;
    }
    cout << res << endl;
    
    return 0;
}