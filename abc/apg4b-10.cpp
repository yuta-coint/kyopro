#include <bits/stdc++.h>
using namespace std;
 
int main() {
  int A, B;
  cin >> A >> B;
  string ans;
  ans = "A:";
  int i=0;
  while (i<A){
      ans+="]";
      i++;
  }
  cout << ans <<endl;
  ans = "B:";
  i=0;
  while (i<B){
      ans+="]";
      i++;
  }
  cout << ans <<endl;
}