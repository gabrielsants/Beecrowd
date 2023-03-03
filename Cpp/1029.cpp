#include <iostream>
using namespace std;

/*
    @Author : Gabriel Santos - Federal University of Goiás;
*/

int calls = 0;

int fib(int n) {
        calls++;
    if( n < 2 ) {
        return n;
    } else {
        return fib(n - 1) + fib(n - 2);
    }
}


int main() {
    int n = 0, x = 0, k;
    
    cin >> n;
    
    while(n >= 1){
        calls = 0;
        cin >> x;
        k = fib(x);
        cout << "fib(" << x <<") = " << calls - 1 << " calls = " << k << endl;
        n--;
    }
}