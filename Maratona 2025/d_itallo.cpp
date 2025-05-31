#include <bits/stdc++.h>
using namespace std;

int main(){
    int n; cin >> n;
    double conts = 0, contt = 0;

    string s, t; cin >> s >> t;

    for(int i = 0; i < n; i++){
        if(s[i] == '*'){
            conts++;
        }
        if(t[i] == '*'){
            contt++;
        }
    }


    int col = conts - contt;

    double res = col/conts;

    cout << fixed << setprecision(2);

    cout << res << endl;
}