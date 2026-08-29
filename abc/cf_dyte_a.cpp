#include <bits/stdc++.h>
using namespace std;
int main(){
    int t;cin>>t;
    for(int ca;ca<t;ca++){
        int n;int k;
        cin >> n >> k;
        string s;
        cin >> s;
        vector<int> chara(26,0);
        //char t = 'a';
        //cout << int(t) << endl;
        for(int i=0;i<n;i++){
            chara[int(s[i])-int('a')]+=1;
        }
        int st = n/k;
        int amari = 0;
        for(int i=0;i<25;i++){
            if(chara[i]<chara[i+1]){
                amari+=chara[i+1]-chara[i];
                chara[i+1]=chara[i];
            }
        }
        for(int i=0;i<26;i++){
            if(i>=st){
                amari+=chara[i];
                chara[i]=0;
            }
        }
        //for(int i=0;i<25;i++){
        //    cout << chara[i];
        //}
        //cout << endl;
        vector<int> ans(k,0);
        for(int component=1;component<=k;component++){
            //役割を完遂できるか
            for(int i=0;i<26;i++){
                if(component>chara[i]){
                    ans[component-1]=i;
                    break;
                }
            }
        }
        for(int i=0;i<k;i++){
            cout << char(int('a')+ans[i]);
        }
        cout << endl;
    }
}