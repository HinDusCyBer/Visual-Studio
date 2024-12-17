#include <iostream>
#include <algorithm>
#include <cmath>
using namespace std;

int main() {
    int t;
    cin >> t;

    while(t--) {
        int n;
        cin >> n;

        int a[n];
        for(int i=0; i<n; i++)
            cin >> a[i];

        int moves = 0;
        for(int i=0; i<n/2; i++) {
            int diff = abs(a[i] - a[n-i-1]);
            moves += diff;
            a[i] = a[i] + diff;
            a[n-i-1] = a[n-i-1] + diff;
        }

        cout << moves << endl;
    }

    return 0;
}