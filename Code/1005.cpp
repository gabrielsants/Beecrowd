#include <iostream>
using namespace std;

/*
    @Author : Gabriel Santos - Federal University of Goiás;
*/

int main(void) {

	 std::cout.precision(5);

	double a, b, media;

	cin >> a >> b;

	media = ((a * 3.5) + (b * 7.5)) / (3.5 + 7.5) ;

	cout << "MEDIA = " << std::fixed << media << endl;



}