//Include Header files
#include<bits/stdc++.h>
using namespace std;

//Function to return mid-point of two numbers
int getMid(int a,int b){
	return a + (b-a)/2;
}

//A recursive function that constructs Segment Tree for array[start_index,end_index]
int constructSTmain(vector<int> &ST,vector<int> &array,int start_index,int end_index,int current_index){
	if(start_index==end_index)
	{
		ST[current_index]=array[start_index];
		return array[start_index];
	}

	int mid = getMid(start_index,end_index);
	ST[current_index]= constructSTmain(ST,array,start_index,mid,current_index*2+1) + constructSTmain(ST,array,mid+1,end_index,current_index*2+2);
	return ST[current_index];
}

//A recursive function to get sum of values from index required_start to index required_end
int getSum(vector<int> &ST,int current_index,int current_index_start,int current_index_end,int required_start,int required_end){
	if(current_index_start>=required_start && current_index_end<=required_end)
		return ST[current_index];
	if(current_index_start>required_end || current_index_end<required_start)
		return 0;
	int mid = getMid(current_index_start,current_index_end);
	return getSum(ST,current_index*2+1,current_index_start,mid,required_start,required_end) + getSum(ST,current_index*2+2,mid+1,current_index_end,required_start,required_end);
}

//A recursive function to update values of nodes in the segment tree which contain the target_index in their range
void UpdateValue(vector<int> &ST,int current_index,int current_index_start,int current_index_end,int target_index,int difference){
	if(target_index<current_index_start || target_index>current_index_end)
		return;
	ST[current_index]+=difference;
	int mid=getMid(current_index_start,current_index_end);

	if(current_index_start!=current_index_end){
		UpdateValue(ST,current_index*2+1,current_index_start,mid,target_index,difference);
		UpdateValue(ST,current_index*2+2,mid+1,current_index_end,target_index,difference);
	}
}

//Function to be called to construct a segment tree for a given vector
//This function allocates memory for segment tree
//This function calls constructSTmain() function for value allocation to the nodes in the tree
vector<int> call_constructST(vector<int> &array,int array_size){
	int x = (int)(ceil(log2(array.size())));  
	int max_size = 2*(int)pow(2, x) - 1;

	vector<int> ST;
	ST.resize(max_size);

	constructSTmain(ST,array,0,array_size-1,0);
	return ST;
}

//Function to be called to get sum of numbers from array[required_start,required_end] using Segment Tree
//Function calls getSum() for implementation
int call_getSum(vector<int> &ST,int array_size,int required_start,int required_end){

	if(required_start < 0 || required_start > required_end || required_end > array_size-1){
		printf("Please enter valid values for starting and ending index\n");
		return -1;
	}

	return getSum(ST,0,0,array_size-1,required_start,required_end);
}

//Function to be called to update the values in segment tree to reflect the update in the original array at target_index
//Function calls UpdateValue() for implementation
void call_updateValue(vector<int> &ST,vector<int> &array,int array_size,int target_index,int value){

	if(target_index < 0 || target_index > array_size-1){
		printf("PLease enter valid value for target index\n");
		return ;
	}

	int difference = value - array[target_index] ;

	UpdateValue(ST,0,0,array_size-1,target_index,difference);
}

int main(){
	
	vector<int> array{1,2,3,4,5};

	vector<int> ST;
	ST = call_constructST(array,array.size());
	printf("%d\n",call_getSum(ST,array.size(),0,3));
	
	call_updateValue(ST,array,array.size(),2,0);
	printf("%d",call_getSum(ST,array.size(),0,3));
	
}