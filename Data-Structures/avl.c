//Including Header Files
#include<stdio.h>
#include<stdlib.h>

//Data-Type of node for implementing AVL Tree
typedef struct node{
	int key;
	struct node *left;
	struct node *right;
	int height;
}node;

//Function to return maximum of two values
int max(int a, int b) 
{ 
    return (a > b)? a : b; 
}

//Function to get height parameter of a node
int height(node *N) 
{ 
    if (N == NULL) 
        return 0; 
    return N->height; 
}

//Function to get value of balance at a node
int getbalance(node* temp){
	return (height(temp->right) - height(temp->left));
}

//Function to update height of a node
void updateheight(node* temp){
	temp->height = max(height(temp->left),height(temp->right))+1; 
}

//Function to return a new node with key as given number
node* initalize(int key){
	node* temp = (node*)malloc(sizeof(node));
	temp->key = key;
	temp->left = NULL;
	temp->right = NULL;
	temp->height = 1;
	return temp;
}

//FUnction to left rotate about a node to mantain balance at that node
node* leftrotate(node* pivot){
	node* temp = pivot;
	pivot = pivot->right;
	temp->right = NULL;
	temp->right = pivot->left;
	pivot->left = temp;
	updateheight(temp);
	updateheight(pivot);
	return pivot;
}

//Function to right rotate about a node to maintain balance at that node
node* rightrotate(node* pivot){
	node* temp = pivot;
	pivot = pivot->left;
	temp->left = NULL;
	temp->left = pivot->right;
	pivot->right = temp;
	updateheight(temp);
	updateheight(pivot);
	return pivot;
}

//Function to insert a node into the AVL Tree by
//recursively balancing tree during back-tracking 
node* insert(int value,node* root){
	if (root == NULL)
	{
		root = initalize(value);
		return root;
	}

	if (value > root->key)
	{
		root->right = insert(value,root->right);
	}
	else if (value < root->key)
	{
		root->left = insert(value,root->left);
	}
	else
		return root;

	updateheight(root);

	int balance = getbalance(root);

	if (balance > 1 && value > root->right->key)
		return leftrotate(root);
	if (balance < -1 && value < root->left->key)
		return rightrotate(root);
	if (balance > 1 && value < root->right->key)
	{
		root->right = rightrotate(root->right);
		return leftrotate(root);
	}
	if (balance < -1 && value > root->right->key)
	{
		root->left = leftrotate(root->left);
		return rightrotate(root);
	}
	return root;


}

//Print Pre Order Traversal of the tree
void preOrder(node *root) 
{ 
    if(root != NULL) 
    { 
        printf("%d ", root->key); 
        preOrder(root->left); 
        preOrder(root->right); 
    }
} 

int main() 
{ 
  node *root = NULL; 
  
  /* Constructing tree given in the above figure */
  for (int i = 0; i <= 50; ++i)
  {
  	root = insert(i,root);
  	root = insert(100-i,root);
  }
  printf("%d\n",root->height);
  
  return 0; 
} 





