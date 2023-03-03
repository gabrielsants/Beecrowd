#include <iostream>

using namespace std;

/*
    @Author : Gabriel Santos - Federal University of Goiás;
*/

int main(void)
{
    std::cout.precision(2);

	double preco[5] = {4, 4.5, 5, 2, 1.5};
	int code, amount;

    cin >> code >> amount;

	cout << "Total: R$ " << std::fixed << amount * preco[code -1] << endl;;
	
	return 1;
}