/*

Each node in a binary tree contains an integer value and two pointers to next-level nodes: “left” and “right”. 
We call a tree sorted if for each node the following statement is correct:
“All values in the left subtree are less than or equal to the value of the node, and all values in the right subtree are greater than the value of the node.”

Write a function that takes a pointer to a root of a tree and checks whether the tree is sorted.
You may create more than one method, if necessary.

*/

struct Node {
public:
  Node(int val) : value(val), pLeft(nullptr), pRight(nullptr) {};
  
  ~Node() {
    if (pLeft)
      delete pLeft;
    if (pRight)
      delete pRight;
  };
  
  int value;
  Node * pLeft, * pRight;
};

// ******************** YOUR CODE HERE ********************
// Returns value indicating whether binary tree passed by a pointer to the root node is sorted
bool IsSorted(Node * pRoot) {
  if (pRoot == nullptr) 
    return true;
  if (pRoot->pLeft != nullptr && pRoot->pLeft->value > pRoot->value) 
    return false;
  if (pRoot->pRight != nullptr && pRoot->pRight->value < pRoot->value) 
    return false;
  return IsSorted(pRoot->pLeft) && IsSorted(pRoot->pRight);
}
// ********************************************************


#include <iostream>
using namespace std;

int main() {
  
  // This is only simple example.
  // Solution must handle all cases.
  
  Node* pRoot = new Node(1);
  pRoot->pLeft = new Node(1);
  pRoot->pLeft->pLeft = new Node(0);
  pRoot->pRight = new Node(2);
  
  if (IsSorted(pRoot)) cout << "Tree is sorted" << endl;
  else cout << "Tree is not sorted" << endl;
  
  delete pRoot;
  return 0;
}
