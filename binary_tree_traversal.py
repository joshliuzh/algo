# Iteratively traverse binary trees
class Traversal:
  def inorder(root):
        stack = []
        curr = root
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            output.append(curr.val)
            curr = curr.right
        return output
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
      if not root:
          return []
      output = []
        
      stack = [root]
        
      while stack:
            
          node = stack.pop()
          output.append(node.val)
            
          if node.left:
              stack.append(node.left)
            
          if node.right:
              stack.append(node.right)
      return output[::-1]
