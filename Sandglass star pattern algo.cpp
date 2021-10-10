#include<iostream>
using namespace std;

int main()
{
	int i, j, k, ro;
	// ro stants for Rows
	cout<< "WELCOME TO SANDGLASS PROGRAM\n";
	cout<< "Enter Number of Rows \n";
	cout<<"   => " ;
    cin >> ro;

    cout<< "Sandglass star Pattern\n";

    for(i = 0; i <=ro - 1; i++)
    {
    	for(j = 0; j < i; j++)
		{
            cout<< " ";
        }
        for(k = i; k<= ro - 1; k++)
        {
            cout<< "* ";
        }
        cout<< "\n";
    }

    for(i = ro - 1; i >= 0; i--)
    {
    	for(j = 0; j < i; j++)
		{
            cout<< " ";
        }
        for(k = i; k <= ro - 1; k++)
        {
            cout<< "* ";
        }
        cout<< "\n";
    }
 	return 0;
}

