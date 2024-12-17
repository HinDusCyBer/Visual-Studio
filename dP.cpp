#include <iostream>
#include <iomanip>
#include <cmath>

using namespace std;

double func(const double x)
{
    return x * x - 12;
}

void findRoot(const double left_bound, const double right_bound)
{
    const double tolerance = 1e-6;
    double a = left_bound;
    double b = right_bound;
    int iter_count = 0;

    while (fabs(b - a) > tolerance)
    {
        if (++iter_count > 1000)
        {
            throw std::runtime_error("Maximum iteration count reached.");
        }

        if (func(a) * func(b) > 0)
        {
            throw std::runtime_error("No root found within the given bounds.");
        }

        const double c = (a + b) / 2;
        if (func(c) == 0)
        {
            a = b = c;
            break;
        }

        if (func(a) * func(c) < 0)
        {
            b = c;
        }
        else
        {
            a = c;
        }
    }
    cout << "The root is " << setprecision(6) << (a + b) / 2 << endl;
}

int main()
{
    try
    {
        findRoot(,);
    }
    catch (const std::exception& ex)
    {
        cout << ex.what() << endl;
    }

    return 0;
}