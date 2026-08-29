#include <bits/stdc++.h>
using namespace std;
 
int main() {
    vector<int> vec(3);
    cin >> vec.at(0) >> vec.at(1) >> vec.at(2);
    sort(vec.begin(),vec.end());
    int ans;
    ans = vec.at(2) -vec.at(0);
    cout << ans << endl;
}