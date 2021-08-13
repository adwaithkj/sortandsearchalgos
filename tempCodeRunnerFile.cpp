#include <iostream>
using namespace std;

int display(int n)
{
    cout << n << "\n";
}

int add(int a, int b, int c)
{
    cout << "The addition sum is ";
    display(a + b + c);
}

int multiply(int a, int b, int c)
{
    cout << "The multiplications is ";
    display(a * b * c);
}
int main()

{
    cout << "Enter the three numbers ";
    int a, b, c;
    cin >> a >> b >> c;
    add(a, b, c);
    multiply(a, b, c);
}