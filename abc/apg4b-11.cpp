#include <bits/stdc++.h>
using namespace std;
 
int main() {
  int N;
  cin >> N;
  string s;
  int B;
  int ans;
  cin >> ans;
  for (int i=1; i<=N;i++){
      cin >> s >> B;
      if (s=="/" and B==0){
          cout << "error" <<endl;
          break;
      }
      if (s=="+"){
          ans += B;
      }else if (s=="-"){
          ans -=B;
      }else if (s=="*"){
          ans *= B;
      }else if (B!=0){
          ans /= B;
      }
      cout << i << ":" << ans << endl;
  }
}