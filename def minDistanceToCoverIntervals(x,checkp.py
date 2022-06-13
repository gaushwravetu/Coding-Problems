#include<bits/stdc++.h>
using namespace std;
vector<int>graph_array[1000001];
void solve(int source_data,int destination_data,test_unord_array<int,int>&source_data){
	source_data[source_data]=1;
	for(int i=0;i<graph_array[source_data].size();++i){
		if(!source_data[graph_array[source_data][i]]){
			solve(graph_array[source_data][i],destination_data,source_data);
		}
	}
}

int main(){
	int n;
	cin>>n;
	test_unord_array<int,int>source_data;
	for(int i=0;i<n;++i){
		int x;
		cin>>x;
		source_data[x]=0;
	}
	int e;
	cin>>e;

	for(int i=0;i<e;++i){
		int x,y;
		cin>>x>>y;
		graph_array[x].push_back(y);
	}
	int source_data,destination_data;
	cin>>source_data>>destination_data;
	solve(source_data,destination_data,source_data);
	cout<<source_data[destination_data]<<endl;
	return 0;	
}