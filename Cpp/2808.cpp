#include <iostream>
using namespace std;

/*
    @Author : Gabriel Santos - Federal University of Goiás;
*/

//Código com leitura de valores por string única.
int main()
{
    string _line;
    char pos[2];
    char num[2];
    int j = 0;
    int k = 0;

    getline(cin, _line);

    for (int i = 0; i < _line.length(); i++)
    {

        if (_line[i] >= 'a' && _line[i] <= 'h')
        {
            pos[j] = _line[i];
            j++;
        }
        else if (_line[i] >= '1' && _line[i] <= '8')
        {
            num[k] = _line[i];
            k++;
        }
    }

    if  (
                (pos[0] == (pos[1] - 2) || pos[0] == (pos[1] + 2))
            &&  (num[0] == (num[1] - 1) || num[0] == (num[1] + 1))
        ) 
    {
        cout << "VALIDO" << endl;
    }
    else if  (
                (pos[0] == (pos[1] - 1) || pos[0] == (pos[1] + 1)) 
            &&  (num[0] == (num[1] - 2) || num[0] == (num[1] + 2))
        )
    {
        cout << "VALIDO" << endl;
    }
    else
    {
        cout << "INVALIDO" << endl;
    }
}