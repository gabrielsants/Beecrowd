#include <iostream>
#include <cmath>

using namespace std;

/*
    @Author : Gabriel Santos - Federal University of Goiás;
*/


int main(void)
{

	std::cout.precision(5);

	double a, b, c, raiz = 0, x1 = 0, x2 = 0, delta = 0;

	cin >> a >> b >> c;
	// delta = b^2 - 4.a.c
	delta = ((pow(b, 2)) + (-4 * a * c));

	raiz = sqrt(delta);

	if (raiz >= 0 || raiz <= 0)
	{
		if ((2 * a) != 0)
		{
			x1 = ((b * -1) + raiz) / (2 * a);
			x2 = ((b * -1) - raiz) / (2 * a);

			cout << "R1 = " << std::fixed << x1 << endl
				 << "R2 = " << std::fixed << x2 << endl;
		}
		else
		{
			cout << "Impossivel calcular" << endl;
		}
	}
	else
	{
		cout << "Impossivel calcular" << endl;
	}

	return 1;
}