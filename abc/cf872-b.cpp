#include <bits/stdc++.h>
using namespace std;
int main(){
    int t;cin>>t;
    for (int ca=0;ca<t;ca++){
        int n,m;cin >> n >> m;
        if (n>m){
            swap(m,n);
        }
        vector<int> nums = {};
        for (int i=0;i<n*m;i++){
            int a;cin >> a;
            nums.push_back(a);
        }
        sort(nums.begin(), nums.end());
        long ans1,ans2;
        ans1 = nums[n*m-1]*(n*m-1)-nums[0]*(m-1)*n-nums[1]*(n-1);
        ans2 = nums[n*m-1]*(m-1)*n+nums[n*m-2]*(n-1)-nums[0]*(n*m-1);
        cout << max(ans1,ans2) << endl;
    }
}