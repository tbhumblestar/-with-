#BinaryTree.py

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
    
    
    def preorder(self):
        """
        현재 노드를 먼저 방문(print)하고, 
        자식 노드를 확인하고 재귀적으로 preorder를 실행
        """
        
        if self != None:
            
            #방문
            print(self.key)
            
            #만약 왼쪽 노드가 있으면
            if self.left :
                self.left.preorder()
            
            #만약 오른쪽 노드가 있으면
            if self.right :
                self.right.preorder()