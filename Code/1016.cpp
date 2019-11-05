#include <iostream>
#include <cmath>
using namespace std;

/*
    @Author : Gabriel Santos - Federal University of Goiás;
*/

int main(void){

	int v1 = 60, v2 = 90, percorrido = 0, min = 0, distancia;

	cin >> distancia;

	while(1){
		if(distancia == percorrido){
			break;
		}
		percorrido++;
		min+=2;
	}

	cout << min << " minutos" << endl;

	return 1;
}