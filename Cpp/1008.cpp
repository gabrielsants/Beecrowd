#include <iostream>
using namespace std;

/*
    @Author : Gabriel Santos - Federal University of Goiás;
*/

int main(void) {

	std::cout.precision(2);

	int num_funcionario, horas_trabalhadas;
	double valor_per_hora, salario;

	cin >> num_funcionario >> horas_trabalhadas >> valor_per_hora;

	salario = horas_trabalhadas * valor_per_hora;

	cout << "NUMBER = " << num_funcionario << endl << "SALARY = U$ " << std::fixed << salario << endl;


}