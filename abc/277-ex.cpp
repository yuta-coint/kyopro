#include <atcoder/twosat>
#include <iostream>
#include <vector>

using namespace std;
using namespace atcoder;
int main(){
    int n, m, q;
    cin >> n >> m >> q;
    two_sat ts(n*m);
    for (int i = 0; i < q; i++){
        int A, B, L, R;
        cin >> A >> B >> L >> R;
        A--; B--;
        for (int j = 0; j < m; j++){
            if (L - 1 - m < j && j <= L - 1){
                ts.add_clause(A*m + j, true, B*m + L - j - 1, true);
            }
            if (R - 1 - m < j && j <= R - 1){
                ts.add_clause(A*m + j, false, B*m + R - j - 1, false);
            }
        }
        if (L >= m + 1){
            ts.add_clause(A*m + L - m - 1, true, A*m + L - m - 1, true);
            ts.add_clause(B*m + L - m - 1, true, B*m + L - m - 1, true);
        }
        if (R < m){
            ts.add_clause(A*m + R, false, A*m + R, false);
            ts.add_clause(B*m + R, false, B*m + R, false);
        }
    }
    for (int i = 0; i < n; i++){
        for (int j = 0; j < m - 1; j++){
            ts.add_clause(i*m + j, true, i*m + j + 1, false);
        }
    }
    if (ts.satisfiable()){
        auto ans = ts.answer();
        for (int i = 0; i < n; i++){
            int cnt = m;
            for (int j = 0; j < m; j++){
                if (ans[i*m + j] == false){
                    cnt = j;
                    break;
                }
            }
            cout << cnt << " ";
        }
        cout << endl;
    }
    else{
        cout << "-1" << endl;
    }
}