#include <iostream>
using namespace std;

/*
    @Author : Gabriel Santos - Federal University of Goiás;
*/

int main(void) {

	std::cout.precision(4);

    double area, raio;
	double n = 3.14159;

	cin >> raio;

	raio *= raio;
	area = n * raio;

	cout << "A=" << std::fixed << area << endl;
}