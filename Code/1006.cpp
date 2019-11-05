#include <iostream>
using namespace std;

/*
    @Author : Gabriel Santos - Federal University of Goiás;
*/

int main(void) {

	 std::cout.precision(1);

	double a, b, c, media;

	cin >> a >> b >> c;

	media = ((a * 0.2) + (b * 0.3)) + (c * 0.5) ;

	cout << "MEDIA = " << std::fixed << media << endl;

}