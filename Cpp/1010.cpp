#include <iostream>
#include<string>
using namespace std;

/*
    @Author : Gabriel Santos - Federal University of Goiás;
*/

int main(void) {

	std::cout.precision(2);

	int codigo1, numero1, codigo2, numero2;
	double valor1, valor2, valor_final;

	cin >> codigo1 >> numero1 >> valor1;
	cin >> codigo2 >> numero2 >> valor2;

	valor_final = ((numero1 * valor1) + (numero2 * valor2));

	cout << "VALOR A PAGAR: R$ " << std::fixed << valor_final << endl;

}