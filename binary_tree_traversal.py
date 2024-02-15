# Iteratively traverse binary trees
class Traversal:
  def inorder(root):
    if not root:
      return None
      while stack or root:
          while root:
              stack.append(root)
              root = root.left
          root = stack.pop()
          print(root.val)
          root = root.right

  def preorder(root):
    if root is None:
        return []
        
    stack = [root]
    output = []
    while stack:
      node = stack.pop()
      output.append(node.val)
      if node.right:
        stack.append(node.right)
      if node.left:
        stack.append(node.left)
            
    return output
  
  def postorder(root):
    if root is None:
        return []
        
    stack = [root]
    output = []
    while stack or root:
        root = stack.pop()
        if root is not None:
            output.append(root.val)
            if root.left is not None:
                stack.append(root.left)
            if root.right is not None:
                stack.append(root.right)
        
        return output      
