#include <iostream>
using namespace std;

/*
    @Author : Gabriel Santos - Federal University of Goiás;
*/

int main( void ) {
    
    int c = 0;
    int N = 0;

    cin >> c;

    while( c-- != 0 ){
        cin >> N;
        if(N > 8000){ cout << "Mais de 8000!" << endl; 
        } else { cout << "Inseto!" << endl; }  
    }   
    return 0;
}