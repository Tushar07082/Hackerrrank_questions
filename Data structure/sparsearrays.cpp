#include <iostream>
using namespace std;
int main(){
        int n;
        cin>>n;
        string a[n];
        for(int i=0;i<n;i++){
                cin>>a[i];
        }
        int q;
        cin>>q;
        string b[q];
        for(int i=0;i<q;i++){
                cin>>b[i];
        }
        int r[q]={0};
        for(int i=0;i<n;i++){
                for(int j=0;j<q;j++){
                        if(b[j]==a[i]){
                                r[j]++;
                        }
                }
        }
        for(int i=0;i<q;i++){
                cout<<r[i]<<endl;
        }

}