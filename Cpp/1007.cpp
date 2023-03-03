#include <iostream>
using namespace std;

/*
    @Author : Gabriel Santos - Federal University of Goiás;
*/

int main(void) {

	std::cout.precision(1);

	int a,b,c,d, diferenca;

	cin >> a >> b >> c >> d;

	diferenca = ((a * b) - (c * d));

	cout << "DIFERENCA = " << diferenca << endl;

}