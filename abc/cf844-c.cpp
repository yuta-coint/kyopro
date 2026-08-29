#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
#define rep2(i,k, n) for (int i = k; i < (int)(n); i++)
#define all(x) (x).begin(),(x).end()
typedef long long int64;
typedef vector<int> VI;
typedef string str;
#define fi first
#define se second
typedef pair<int,int> PII;
template<class T>bool chmax(T &a, const T &b) { if (a<b) { a=b; return 1; } return 0; }
template<class T>bool chmin(T &a, const T &b) { if (b<a) { a=b; return 1; } return 0; }
#define pb push_back
int main(){
    int t;cin>>t;
    rep(testcase,t){
        long n;cin >> n;
        vector<int> letter(26);
        rep(i,26){
            letter[i] = 0;
        }
        string s;cin >>s;
        rep(i,n){
            letter[s[i]-'a']+=1;
        }
        vector<pair<long,long>> letter2(26);
        rep(i,26){
            //tupleは{}で囲む
            letter2[i]={letter[i],i};
        }
        sort(letter2.begin(), letter2.end());
        //何種類の文字を使うかを調べ上げ
        long change = 1000000;
        long change_let;
        //iは後ろの何文字を切り取るのが良いか
        rep2(i,1,27){
            if(n%i!=0){continue;}
            long each = n/i;
            long cnt = 0;
            rep2(j,26-i,26){if(letter2[j].first>each){cnt+=letter2[j].first-each;}}
            rep(j,26-i){cnt+=letter2[j].first;}
            if (cnt<change){change = cnt;change_let = i;}
        }
        cout << change <<endl;
        long each = n/change_let;
        vector<int> ok(26);
        rep(j,26){
            ok[j]=0; 
        }
        rep2(j,26-change_let,26){
            ok[letter2[j].second]=1;   
        }
        //足りていない奴を枚挙
        vector<char> change_to;
        rep2(j,26-change_let,26){
            if (each>letter2[j].first){
                rep(_,each-letter2[j].first){change_to.push_back('a'+(letter2[j].second));}
            }
        }
        //rep(i,change){cout<<change_to[i]<<endl;}
        int key = 0;
        rep(i,n){
            //eachに揃えるべきやつら
            if (((ok[s[i]-'a']==0) && (letter[s[i]-'a']>0))||(letter[s[i]-'a']>each)){
                letter[s[i]-'a']-=1;
                s[i]=change_to[key];
                key++;
            }
        }
        cout << s << endl;
    }
}