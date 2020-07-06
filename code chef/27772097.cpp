#include <iostream>
using namespace std;

int main() {
	int T; cin>>T;
    while(T--)
    {
        int type[1000] , arr[1000];
        int N,H,Y1,Y2,L; cin>>N>>H>>Y1>>Y2>>L;
        int count = 0;
        for(int i=0;i<N;i++)
            cin>>type[i]>>arr[i];
        for(int i=0;i<N;i++)
        {
            if(type[i]==1 && arr[i]<H-Y1)
                L = L - 1;
            else if(type[i]==2 && arr[i]>Y2 )
                L = L -1;
            if(L==0)
                break;
            ++count;
        }
        cout<<count<<endl;
    }
	return 0;
}
