#include <bits/stdc++.h>
using namespace std;
 
int main() {
  int N;
  cin >> N;
  int a;
  map<int,int> score;
  for (int i = 0; i < N; i++) {
    cin >> a;
    if (score.count(a)){
        score[a] += 1;
    }else{
        score[a] = 1;
    }
  }
  int ans;
  int ans2;
  ans2 = 0;
  for (auto p:score){
    auto s = p.first;
    auto t = p.second;
    if (t>ans2){
        ans = s;
        ans2 = t;
    }
  }
  cout << ans << " " << ans2 << endl;
 }