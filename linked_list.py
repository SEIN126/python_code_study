class Node:
  '''
  Node for linked list
  '''
  def __init__(self, data, is_head=False):
    self.data = data
    self.next = None 
    self.is_head = False
    

  def add(self, node):
    if node.is_head: 
      self.is_head = node.is_head
      node.is_head = False

    if self.is_head == node.is_head:
      '''False-False case'''
      self.is_head = True
      node.is_head = False 
    
    tmp = self.next
    self.next = node
    node.next = tmp

  def delete(self, data):
    assert self.is_head , 'please use this function in first node'
    return self._delete(data)
  
  def _delete(self, data):
    assert self.is_head == True, 'please use in first node'
    
    if self.is_head :
       if self.data == data :
         self.next.is_head=True
         self.next = None
         return print(f'Delete the {str(data)}')

    if self.next is not None :
      if self.next.data == data :
        self.next = self.next.next
        return print(f'Delete the {str(data)}')
      
      else :
        self.next._delete(data)
        
    else :
      return print(f'Do not find the {str(data)}')
  
  def __str__(self):
    # return f'data : {str(self.data)}, next id : {str(self.next_id)}'
    return f'{str(self.data)}'
  
class bydirectionNode(Node):
  '''
  Node for linked list
  '''
  def __init__(self, data, is_head=False):
    super().__init__(data, is_head=is_head)
    self.prev = None
    
  def add(self, node):
    if node.is_head: 
      self.is_head = node.is_head
      node.is_head = False

    if self.is_head == node.is_head:
      '''False-False case'''
      self.is_head = True
      node.is_head = False 
    
    tmp_n = self.next
    self.next = node
    node.next = tmp_n

    if node.next is not None :
      node.next.prev = node
    node.prev = self
  
  def delete(self, data):
    assert self.is_head , 'please use this function in first node'
    return self._delete(data)

  def _delete(self, data):
    if self.is_head :
      # head인 경우
      if self.data == data :
        self.next.is_head=True
        self.next.prev=None
        self.next = None
        return print(f'Delete the {str(data)}')

    
    if self.next is not None :
      if self.next.data == data :
        self.next = self.next.next
        if self.next is not None : 
          self.next.prev = self 
        return print(f'Delete the {str(data)}')

      else :
        self.next._delete(data)
    
    else :
      return print(f'Do not find the {str(data)}')

if __name__ == '__main__':
    node1 = Node(1)
    node2 = Node(2)
    node1.add(node2)

    node3 = Node(3, True)
    node1.add(node3) # 1-3-2
    
    print(node3.is_head) # False
    print(node1.next, node3.next, node2.next) # 3 2 None
    
    node1.delete(1) # 3-2
    print(node1.next, node3.next, node2.next) # None 2 None

    print('-'*50)
    
    ''''bydirection linked list function test'''
    node1 = bydirectionNode(1)
    node2 = bydirectionNode(2)
    node1.add(node2)
    
    node3 = bydirectionNode(3, True)
    node1.add(node3) # 1-3-2
    
    print(node3.is_head) # False

    print(node1.prev, node3.prev, node2.prev) # None 1 3
    print(node1.next, node3.next, node2.next) # 3 2 None
    
    node1.delete(1) # 3-2
    print(node1.prev, node3.prev, node2.prev) # None None 3
    print(node1.next, node3.next, node2.next) # None 2 None
    
