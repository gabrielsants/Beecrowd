#include <iostream>
using namespace std;

/*
    @Author : Gabriel Santos - Federal University of Goiás;
*/

int main() {

    int N, v[3], x, y, i, res;

    while(1){
        cin >> N;
        if(N == 0){ break;}
        
        res = 0;
        cin >> v[0];
        cin >> v[1];
        if( N == 2 ) {
            if(v[0] != v[1]) res = 2;
        } else {
            x = v[0];
            y = v[1];

            for( i = 2; i < N; i++ ) { 
                cin >> v[2];
                if( ((v[1] > v[0]) && (v[1] > v[2])) || ((v[1] < v[0] && (v[1] < v[2]))) ) 
                    res ++;
                v[0] = v[1];
                v[1] = v[2];
            }
            
            if( ((v[2] > v[0]) && (v[2] > x)) || ((v[2] < v[0]) && (v[2] < x)) )
                res++;
            
            if( ((x > y) && (x > v[2])) || ((x < y) && (x < v[2])) )
                res++;
        }
        cout << res << endl;
    }
    return 0;
}