#include <bits/stdc++.h>
using namespace std;
int call_num(){
    int x;
    x = 0;
    string ope;
    for (;;){
        cin >> ope;
        if (ope==";"){
            break;
        }
        int pm;
        pm = 1;
        if (ope == "-"){
            pm = -1;
        }
        char y;
        cin >> y;
        if (isdigit(y)){
            x+=(y-"0")*pm;
        }else{
            x+=var[y]*pm;
        }
    }
    return x;
}

int main() {
    int N;
    cin >> N;
    map<char,int> var;
    for (int i=0; i<N; i++){
        string order;
        if (order=="int"){
            char c;
            cin >> c;
            var[c]=call_num();
        }else if (order == "print_int"){
            char z;
            cin >> z;
            int zi;
            if (isdigit(y)){
                zi=stoi(y);
            }else{
                zi=var[y];
            }
            cout << zi+call_num() <<endl;            
        }else if (order == "vec"){
            vec()
        }else if (order == "print_vec"){
            print_vec()
        }      
    }
}