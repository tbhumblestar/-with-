from typing import Union

#node
class Node:
    #생성된 노드는 처음에 자기자신을 다음노드와 직전노드로 가리키고 있음
    #양방향 원형 연결리스트 이므로 끝이 시작점과 연결되는 게 맞음!
    def __init__(self,key=None):
        self.key = key
        self.next = self
        self.prev = self
        
    def __str__(self):
        return str(self.key)
    

#(Circular) Doubly LinkedList
class DoublyLinkedList:
    
    #처음 만들때, 첫번째 시작원소를 표시하기 위한 더미노드를 하나 생성
    def __init__(self) -> None:
        
        #아무런 키값을 가지지 않는 더미원소 하나를 생성. 해당 더미원소가 링크드리스트의 시작점이 됨
        self.head = Node()
        
        self.size = 0
        
    def splice(self,a:Node,b:Node,x:Node):
        """
        기능 : a부터 b까지의 노드들을 떼서, x<>x.next사이에 집어넣는 것
        조건 : a,b사이에 헤드 노드가 존재해서는 안됨(헤드 노드가 이동하면 안되니까)
        """
        ap = a.prev
        bn = b.next
        xn = x.next
        
        #컷하고 컷된 부분을 이어줌
        ap.next = bn
        bn.prev = ap
        
        #컷된 부분을 x, xn에 붙여넣어줌
        x.next = a
        a.prev = x
        b.next = xn
        xn.prev = b
        
    def move_after(self,a:Node,x:Node)-> None:
        """
        노드 a를 노드 x 다음으로 이동
        """
        self.splice(a,a,x)
        
    def move_before(self,a:Node,x:Node)-> None:
        """
        노드 a를 x 앞으로 이동
        """
        self.splice(a,a,x.prev)
    
    def insert_after(self,x:Node,key : int)-> None:
        """
        key를 가진 노드를 생성하고, x 노드 뒤에 삽입
        """
        self.move_after(Node(key),x)
    
    def insert_before(self,x:Node,key : int):
        """
        key를 가진 노드를 생성하고, x 노드 앞에 삽입
        """
        self.move_before(Node(key),x)
    
    def push_front(self,key : int)-> None:
        """
        key를 가진 노드를 생성하고, 리스트 맨 앞에 삽입
        """
        self.insert_after(self.head,key)
    
    def push_back(self,x:Node,key : int)-> None:
        """
        key를 가진 노드를 생성하고, 리스트 맨 뒤에 삽입
        """
        self.insert_before(self.head,key)
        
        
    #탐색연산
    def search(self,key:int)->Union[Node,None]:
        """
        key와 일치하는 값을 가진 노드를 반환
        """
        present_node = self.node
        
        #한바퀴를 돌때까지
        while present_node.next != self.head:
            
            if present_node.key == key:
                return present_node
        return None
    
    def remove(self,del_node :Node) -> None:
        if del_node == None or del_node == self.head:
            return None
        
        del_node.prev.next = del_node.next
        del_node.next.prev = del_node.prev
        del del_node
        
    #삭제연산
    def remove_by_key(self,key :int) -> None:
        """
        특정 키를 가진 노드를 검색한 후, 해당 노드를 삭제 노드를 삭제
        """
        
        #삭제할 노드
        del_node = self.search(key)
        self.remove(del_node)

        
    def pop_front(self) -> None:
        """
        맨 앞에 있는 노드를 삭제
        """
        del_node = self.head.next
        self.remove(del_node)


    def pop_back(self) -> None:
        """
        맨 뒤에 있는 노드를 삭제
        """
        del_node = self.head.prev
        self.remove(del_node)


L = DoublyLinkedList()
L.push_front(1)
L.push_front(2)
L.push_front(3)
print(L.head.next,L.head.next.next,L.head.next.next.next)
L.pop_front()
print(L.head.next,L.head.next.next,L.head.next.next.next)
L.push_front(3)
print(L.head.next,L.head.next.next,L.head.next.next.next)
L.pop_back()
print(L.head.next,L.head.next.next,L.head.next.next.next,L.head.next.next.next.next)