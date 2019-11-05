#include <iostream>
#include <cmath>
using namespace std;

/*
    @Author : Gabriel Santos - Federal University of Goiás;
*/
int main(void){

	std::cout.precision(4);

	double x1, y1, x2, y2, e1, e2;

	cin >> x1 >> y1 >> x2 >> y2;

	e1 = x2 - x1;
	e1 *= e1;

	e2 = y2 - y1;
	e2 *= e2;
	
	cout << std::fixed << sqrt(e1 + e2) << endl;

	return 1;
}