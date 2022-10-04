#Queue
class Node:
    def __init__(self,key=None):
        self.key = key
        self.next = None
        
    def __str__(self):
        return str(self.key)
    

#한방향 리스트
class SinglyLinkedList:
    
    #처음 만들어졋을 때는 원소가 없으니까
    def __init__(self) -> None:
        self.head = None
        self.size = 0
        
    def pushfront(self,key):
        #입력된 값을 새로운 노드로 생성
        new_node = Node(key)
        
        #새노드의 다음값이, 기존 연결리스트 헤드(첫번째 인자임)
        #기존 헤드가 첫번째엿다가 새노드에 의해 밀려나서 새노드가 첫번째가 되고, 기존 헤드가 두번째가 되는 것
        new_node.next = self.head
        self.head = new_node
        self.size += 1
    
    #연결 리스트의 맨 뒤에 넣는 메서드  
    def pushBack(self,key):
        new_node = Node(key)
        
        #연결리스트의 원소가 하나도 없다면
        if self.size == 0:
            #첫번째값(head) = 마지막값이므로 그냥 넣어주면 됨
            self.head = new_node
        
        else:
            tail = self.head
            
            #tail.next == None이라면, tail이 마지막 원소라는 것
            #즉 tail이 마지막 원소가될 때까지 계속 이동
            while tail.next != None:
                tail = tail.next
            
            #이제 tail이 맨 마지막 원소니까, 맨 마지막 원소의 다음값으로 new_node를 넣어주면 원소가 하나 추가되는 것임
            tail.next = new_node
            
        self.size += 1
    
    #맨 앞에 있는 원소 pop
    def popFront(self):
        
        #만약 원소가 하나도 없다면
        if self.size == 0:
            print("LinkedList is empty!")
            return None
        #하나 이상의 노드가 존재
        else:
            x = self.head
            
            #일반적인 pop처럼, pop한 head의 값(key)를 리턴하기 위해 미리 다른 곳에 저장
            key = x.key
            
            #이제 헤드가 기존 헤드의 그 다음 노드를 가리킴. 즉 기존 헤드는 삭제
            self.head = x.next
            self.size -= 1
            
            #기존 헤드를 메모리에서 아예 삭제. 이때 x.key는 삭제되지 않는다. 왜냐하면 key가 x.key의 값이 저장되어 있던 곳을 가리키고 있으니까
            del x
            return key
    
    #맨 뒤에 있는 원소를 제거
    def popBack(self):
        #만약 원소가 하나도 없다면
        if self.size == 0:
            print("LinkedList is empty!")
            return None
        
        #만약 원소가 하나라면 > 헤드를 그냥 None으로 바꿔주면 됨
        if self.size == 1:
            self.head = None
        
        #하나 이상의 노드가 존재
        else:
            
            #prev가 tail을 따라가는 식
            #tail.next = None일 때, tail은 마지막 노드가 되고, prev는 마지막의 직전 노드가 됨
            prev, tail = None, self.head
            while tail.next != None:
                prev = tail
                tail = tail.next
                
            prev.next = tail.next
            key = tail.key
            del tail
            self.size -= 1
            return key
    
    #탐색: 인자로 받은 key값과 일치하는 key값을 가진 노드를 리턴, 없으면 None리터
    def search(self,key):
        present_node = self.head
        
        #present_node == Node이다 === 모든 노드를 검사했따
        while present_node != None:
            if present_node.key == key:
                return present_node
            
        #못찾았으니 None을 리턴
        return None
    
    #제너레이터 > 이터레이터가 되어야 할 때, 이 메서드가 호출되돼서 해당 메서드를 수행하는 이터레이턱 됨
    #예를 들어 for문의 iterable자리에 들어갔을 때, __iterator__메서드가 호출됨
    #for i in LinkedList: 에서 i에 present_node를 yield해주고 멈춤
    #그 후 메서드가 끝날때까지 yield문이 없으면 stopiteration이 발생
    #for문에서 stopiteration이 관측되면 for문은 종료됨
    def __iter__(self):
        present_node = self.head
        while present_node != None:
            yield present_node
            present_node = present_node.next
        

L = SinglyLinkedList()

#__iter__를 제외한 나머지 메서드들 테스트
# L.pushfront(1)
# L.pushfront(2)
# L.pushfront(3)
# L.pushfront(4)
# print(L.size)
# print(L.head)
# print(L.head.next)
# print(L.head.next.next)
# L.popFront()
# print(L.size)
# print(L.head)
# L.popBack()
# print(L.head)
# print(L.size)
# L.pushBack(4)
# print(L.head)
# print(L.size)

#__iter__ 테스트
L.pushfront(1)
L.pushfront(2)
L.pushfront(3)
L.pushfront(4)

for i in L:
    print(i)