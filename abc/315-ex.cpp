#include <iostream>
#include <vector>
#include <algorithm>
#include <math.h>
#include <atcoder/convolution>
#include <atcoder/modint>

using namespace std;
using namespace atcoder;

using mint = modint998244353;


int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int N;
    cin >> N;
    vector<mint> A(N);
    for (int i = 0; i < N; i++){
        int a;
        cin >> a;
        A[i] = mint(a);
    }
    vector<mint> F(N + 1,0);
    vector<mint> G(N + 1,0);
    vector<mint> G_Sum(N + 1);
    F[0] = 1;
    for (int i = 0; i <= N; i++){
        //G[i]の更新
        if (i > 0){
            G[i] += 2 * F[i];
        }else{
            G[i] += F[i];
        }
        int width = 1;
        while ((i + 1) % width == 0){
            //Fの[width, 2 * width)とFの[i + 1 - width, i + 1)の畳み込みをとる。
            vector<mint> F_next = convolution(vector<mint>(F.begin() + width, F.begin() + min(i + 1, width * 2)), vector<mint>(F.begin() + i + 1 - width, F.begin() + i + 1));

                for (int j = 0; j < (int)F_next.size(); j++){
                    if ((i + 1 + j) > N) break;
                    if (i + 1 == width * 2){
                        G[i + 1 + j] += F_next[j];
                    }else{
                        G[i + 1 + j] += 2 * F_next[j];
                    }
                }
            width *= 2;
        }
        //F[i + 1]の決定
        if (i == N) break;
        if (i > 0){
            G_Sum[i] = G_Sum[i - 1] + G[i];
        }else{
            G_Sum[i] = G[i];
        }
        F[i + 1] = G_Sum[i] * A[i];
    }
    for (int i = 1; i <= N; i++){
        cout << F[i].val();
        if (i == N) break;
        cout << " ";
    }
    return 0;
}