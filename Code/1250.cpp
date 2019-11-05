#include <iostream>
#include <string>
using namespace std;

/*
    @Author : Gabriel Santos - Federal University of Goiás;
*/

int main()
{
    int n;

    cin >> n;
    for (size_t i = 0; i < n; i++)
    {
        //Declaro variavel apenas para esta funcao
        int altura[50];
        int qtd_tiros = 0;
        string acao;
        int damaged = 0;

        cin >> qtd_tiros;
        cin.ignore();
        for (size_t j = 0; j < qtd_tiros; j++)
        {
            int num = 0;

            do
            {
                cin >> num;
                cin.ignore();
            } while (num > 7 || num < 1);

            altura[j] = num;
        }

        getline(cin, acao);

        for (size_t l = 0; l < qtd_tiros; l++)
        {

            if (acao.at(l) == 'S' && altura[l] <= 2)
            {
                damaged++;
            }
            else if (acao.at(l) == 'J' && altura[l] >= 3)
            {
                damaged++;
            }
        }

        cout << damaged << endl;
    }
}