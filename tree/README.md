To solve a binary tree problem recursively:

***scheme:***
```bash
if not root:
  return True

if condition:
  return result

return (go left 
        and/or 
        go right)
```
 
 
 ***convert sorted array to BST***
 - inorder traversal will not work because it does not give unique solution
 => use preorder instead: mid, left, right
 - to get a balanced tree, we always choose the middle node, to break tie for even number, we chose the left node.

**convert sorted linked list to BST***
- use inorder
- Also, remember to move the head
