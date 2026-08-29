#include <bits/stdc++.h>
using namespace std;
 
int main() {
    int N;
    cin >> N;
    vector<int> vec(N);
    int suma = 0;
    for (int i=0; i<N; i++){
        cin >> vec.at(i);
        suma += vec.at(i);
    }
    suma/=N;
    for (int i=0; i<N; i++){
        if (suma>vec.at(i)){
            cout << suma-vec.at(i) << endl;
        }else{
            cout << vec.at(i)-suma << endl;
        }
    }
}