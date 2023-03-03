#include <iostream>
using namespace std;

/*
    @Author : Gabriel Santos - Federal University of Goiás;
*/

int main(void){

	std::cout.precision(3);

	double x, y;
	
	cin >> x >> y;

	cout << std::fixed << x/y << " km/l" << endl;

	return 1;
}