//how to get the stock data of Tesla in python?
//https://www.youtube.com/watch?v=2BrpKpWwT2A

#include <iostream>
using namespace std;
int main()
{
    int a = 10;
    int *p = &a;
    cout << "The value of a is " << a << endl;
    cout << "The value of a is " << *p << endl;
    cout << "The address of a is " << &a << endl;
    cout << "The address of a is " << p << endl;
    cout << "The address of p is " << &p << endl;
    cout << "The value of p is " <<
        *(&p) << endl;
    return 0;
}
// Compare this snippet from tempCodeRunnerFile.cpp:
// #include <iostream>
// using namespace std;
// int main()
// {
//     int a = 10;
//     int *p = &a;
//     cout << "The value of a is " << a << endl;
