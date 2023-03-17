#include <iostream>
#include <cmath>
 
using namespace std;
 
int main() {
    
    std::cout.precision(2);
    
    int value = 0;
    int bills[7] = {100, 50, 20, 10, 5, 2, 1};
    
    cin >> value;
    
    cout << value << endl;
    
    for (int i = 0; i <= sizeof(bills); i++) {
        value %= bills[i];
        cout << std::fixed << floor(value/bills[i]) << " nota(s) de R$ " << std::fixed << bills[i] << ",00" << endl;
    }
 
    return 0;
}