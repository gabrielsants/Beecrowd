#include <iostream>
#include <cmath>
using namespace std;

/*
    @Author : Gabriel Santos - Federal University of Goiás;
*/

int main(void){

	std::cout.precision(3);

	double kmPorLitro = 12, tempo = 0, velocidade;

	cin >> tempo >> velocidade;

	cout << std::fixed << (velocidade * tempo) / kmPorLitro << endl;

	return 1;
}