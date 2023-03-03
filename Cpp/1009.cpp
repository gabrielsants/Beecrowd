#include <iostream>
#include<string>
using namespace std;

/*
    @Author : Gabriel Santos - Federal University of Goiás;
*/

int main(void) {

	std::cout.precision(2);

	string  nome_vendedor;
	double salario_fixo, total_vendas, res;
	
	getline(cin,nome_vendedor);
	cin >> salario_fixo >> total_vendas;

	res = total_vendas * 0.15;

	cout << "TOTAL = R$ " << std::fixed << salario_fixo+res << endl;

}