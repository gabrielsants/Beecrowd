#include <iostream>
using namespace std;

/*
    @Author : Gabriel Santos - Federal University of Goiás;
*/

int main(void){

	std::cout.precision(3);

	int a, b, c, maior = 0;

	cin >> a >> b >> c;

	maior = a;
	if(b > maior)
		maior = b;
	if( c > maior)
		maior = c;
	cout << maior << " eh o maior" <<endl;

	return 1;
}