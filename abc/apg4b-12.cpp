#include <bits/stdc++.h>
using namespace std;
 
int main() {
  int N;
  string s;
  int i;
  int ans;
  char c;
  int n;
  cin >> s;
  N = s.size();
  i=1;
  ans = 1;
  while (i<N){
      c = s.at(i);
      i++;
      n = s.at(i);
      if (c=='+'){
          ans++;
      }else{
          ans--;
      }
      i++;
  }
  cout << ans <<endl;
}