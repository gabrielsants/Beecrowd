#include <iostream>
using namespace std;

/*
    @Author : Gabriel Santos - Federal University of Goiás;
*/


int main(void){

	std::cout.precision(3);

	double a, b, c, pi =  3.14159;

	cin >> a >> b >> c;

	cout << "TRIANGULO: " << std::fixed << (a * c) / 2 << endl; //a = base c = altura
	cout << "CIRCULO: " << std::fixed << ((c*c)*pi) << endl; //raio c
	cout << "TRAPEZIO: " << std::fixed << (((a + b) /2) * c) << endl; // a e b sao base e c altura
	cout << "QUADRADO: " << std::fixed << b * b << endl; // b = lado
	cout << "RETANGULO: " << std::fixed << a * b << endl; // a e b sao lados

	return 1;
}