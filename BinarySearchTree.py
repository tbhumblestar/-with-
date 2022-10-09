#Binaray Search Tree
class Node:
    def __init__(self,key:int = None,parent = None,left =None,right = None) -> None:
        """
        각 노드는 키값,부모노드, 자식 왼쪽노드, 자식 오른쪽 노드를 가짐
        """
        self.key = key
        self.parent = parent
        self.left = left
        self.right = right
        
    def __str__(self):
        return self.key
    

class BST:
    def __init__(self) -> None:
        self.root = None
        self.size = 0
        self.height = 0
        
    def __len__(self) :
        return self.size
    
    def find_location(self, key):
        """
        key값을 가진 노드가 있다면, 해당 노드를 반환 \n
        없다면, 마지막 탐색 노드를 반환. 이 마지막 탐색노드는 새로운 값이 삽입될 경우, 삽입된 값의 부모노드가 된다
        """
        
        #비어있다면 아무것도 없음
        if self.size == 0: 
            return None 
        
        #p는 v의 부모노드
        p=None 
        #자식 노드
        v = self.root
        
        #while v == None > 키값을 가진 값이 존재하지 않는다
        while v != None: # 
            
            #z키를 가진 노드를 찾았다면 노드를 반환
            if v.key == key: 
                return v 
            
            #못찾았을 때, 찾으려면 key값이 현재노드의 키값보다 크다면
            elif v.key < key:
                
                p=v
                v = v.right
                
            #못찾았을 때, 찾으려면 key값이 현재노드의 키값보다 작다면
            else:
                
                p=v
                v = v.left
        
        #while문을 빠져나왔다면 키를 찾지 못한 것 > 마지막 탐색노드를 반환
        return p

    def search(self, key:int) -> (Node|None):
        """
        key와 일치하는 값이 있다면, 해당 키의 노드를 반환
        없으면 None 반환
        """
        p = self.find_location(key) 
        
        #찾았다면 p.key = key가 되므로
        if p and p.key==key: #key is in tree
            return p
        return None
        

    def insert(self, key) -> (Node|None):
        """
        키가 트리 내부에 있다면 아무것도 안함 \n
        키가 트리 내부에 없다면 이진탐색트리 구조에 맞게 키를 가진 노드를 배치하고 배치된 노드를 반환
        """
        p = self.find_loc(key)
        #트리가 비어있거나, 일치하는 값이 없다면 생성할 수 있음
        if p == None or p.key != key: 
            v = Node(key)

            #트리가 비어있다면 루트노드가 되어야 한다
            if p == None:
                self.root = v
            #트리가 비어있지 않았다면, 반환된 p노드의 아래로 들어가야 함
            if p != None:
                v.parent = p
                
                #v가 p보다 큰지 작은지에 따라
                if p.key >= key: # check if left/right p.left = v
                    p.left = v
                else:
                    p.right = v
            self.size += 1
            return v
        
        #이미 키값이 존재한다!
        else:
            print("key is already in tree!")
        
    def deleteByMerging(self, x:Node):
        """
        삭제할 노드를 받음\n
        1)
        삭제할 노드의 왼쪽 노드가 존재하지 않을 경우 오른쪽 노드가 고대로 올라옴
        삭제할 노드의 왼쪽 노드가 존재할 경우 왼쪽 노드가 고대로 삭제할 노드의 위치를 차지하고 삭제할 노드(x)의 오른쪽 노드들이 왼쪽 노드의 값들 중 가장 큰 값의 오른쪽 자식 노드로 들어감달라붙음
        
        2) 그 후, 삭제할 노드가 루트인지 아닌지를 판단하여 처리
        """
        
        
        # assume that x is not None
        l_child_node = x.left
        r_child_node = x.right
        partent_node = x.parent
        
        #지우려는 노드(x)의 왼쪽노드에 값이 있을 경우
        if l_child_node:
            #x_node : 이제 x의 자리를 차지하게 될 노드
            x_node = l_child_node
            #m_node : x.left트리 중에서 가장 큰 값
            biggest_left = l_child_node
            
            #오른쪽의 끝에 있는 게 제일 큰 값임
            while biggest_left.right:
                biggest_left = biggest_left.right
            
            #지우려는 노드(x)의 오른쪽 값이 있을 경우  
            if r_child_node:
                r_child_node.parent = biggest_left
        
        #지우려는 노드(x)의 왼쪽노드에 값이 없을 경우
        else:
            x_node = r_child_node
            
        
        #x가 root였다면
        if self.root == x:
            #새 노드(x_node)가 root_node가 되는 것 
            self.root = x_node
            
            #x_node가 없을 수도 있음(원래 루트 하나만 존재하던 트리엿다면)
            if x_node:
                x_node.parent = None
        
        #x가 root가 아니엿다면
        else:
            if partent_node.left == x:
                partent_node.left = x_node
            else:
                partent_node.right = x_node
            
            #x_node가 없을 수도 있음(원래 루트 하나만 존재하던 트리엿다면)    
            if x_node:
                x_node.parent = partent_node
                
        self.size -= 1