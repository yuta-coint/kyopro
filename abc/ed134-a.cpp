#include <bits/stdc++.h>
using namespace std;
int main(){
    int t;cin>>t;
    for (int i=0;i<t;i++){
        vector<char> input(4);
        string k;cin>>k;
        input[0]=k[0];
        input[1]=k[1];
        cin>>k;
        input[2]=k[0];
        input[3]=k[1];
        set<int> s;
        for (long unsigned int i = 0; i < input.size(); ++i) s.insert(input[i]);
        cout << s.size()-1 << endl;
        //string k;cin>>k;
        //input.at(0)=k.at(0);
        //input.at(1)=k.at(1);
        //string k;cin>>k;
        //input.at(2)=k.at(0);
        //input.at(3)=k.at(1);
    }
}
