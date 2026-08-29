#include <bits/stdc++.h>
using namespace std;
 
int main() {
  int N;
  cin >> N;
 
  vector<pair<int,int>> a(N);
  for (int i = 0; i < N; i++) {
    cin >> a.at(i).second >> a.at(i).first;
  }
  sort(a.begin(), a.end());
 
  // 各組織について、答えを出力
  for (int i = 0; i < N; i++) {
    cout << a.at(i).second << " " << a.at(i).first << endl;
  }
}