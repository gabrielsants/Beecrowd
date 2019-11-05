#include <iostream>
using namespace std;

/*
    @Author : Gabriel Santos - Federal University of Goiás;
*/


int main(void){

	std::cout.precision(3);

	double raio = 0, exp = 0, volume = 0, pi =  3.14159;
	
	cin >> raio;
	
	exp = raio; exp *= raio; exp *= raio;

	volume = (4/3.0) * pi * exp;

	cout << "VOLUME = " << std::fixed << volume << endl;

	return 1;
}