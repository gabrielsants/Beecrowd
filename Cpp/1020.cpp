#include <iostream>
using namespace std;

/*
    @Author : Gabriel Santos - Federal University of Goiás;
*/

int main(void){

	int diasDeVida = 0, anos = 0, meses = 0, dias = 0;

	cin >> diasDeVida;

	while (diasDeVida != 0){
		if(diasDeVida >= 365){
			anos++;
			diasDeVida = diasDeVida  - 365;
		} else if(diasDeVida >= 30){
			meses++;
			diasDeVida = diasDeVida - 30;
		} else {
			dias++;
			diasDeVida = diasDeVida- 1;
		}
	}

	cout << anos << " ano(s)" << endl << meses  << " mes(es)" << endl << dias << " dia(s)" << endl;

	return 1;
}