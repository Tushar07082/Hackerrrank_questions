#include <iostream>
using namespace std;
int main(){
        int n,m;
        cin>>n>>m;
        int arr[n]={0},maxi=0;;
        for(int i=0;i<m;i++){
                int a,b,k;
                cin>>a>>b>>k;
                for(int j = a-1;j<b;j++){
                        arr[j] += k;
                        maxi = max(arr[j],maxi);
                }
        }
        cout<<maxi<<endl;
}