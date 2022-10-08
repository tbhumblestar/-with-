#Max Heap

class Heap:
    def __init__(self,lst:list = []):
        self.H = lst
        self.make_heap()
        
    def __str__(self):
        return str(self.H)
    
    def heapify_down(self,k:int,n:int):
        """
        k : 검사가 진행되는 현재 노드의 인덱스 \n
        n : 힙의 전체 노드 수 \n
        시간복잡도 : O(log2n) \n
        
        인덱스로 받은 노드를 자식노드와 비교함. 만약 자식 노드 보다 작을 경우 해당 자식노드와 자리를 바꾸고, 자리가 바뀔 경우 바뀐자리에서도 자식노드와 비교하여 동일한 작업을 반복
        """
        
        #2*k + 1 == 현재 노드의 왼쪽 자식 노드. 만약 현재 노드의 왼쪽노드가 전체 리스트 길이 n보다 같거나 크다면, 왼쪽 노드가 존재하지 않는 것. 당연히 2*k+2인 오른쪽 자식노드도 존재하지 않는다
        while 2*k + 1 < n : 
            
            #왼쪽, 오른쪽 인덱스 번호
            L,R = 2*k +1, 2*k+2
            
            #왼쪽 먼저 비교
            if self.H[L] > self.H[k]:
                max_index = L
            else:
                max_index = k
            
            #오른쪽 비교. index Error를 피하기 위해 R<n도 해줘야 함
            if R < n and self.H[R] > self.H[max_index]:
                
                #이제 max_index는 L,R,k중 값이 가장 큰 노드의 인덱스
                max_index = R
            
            #H[k]가 최대값이 아니라면 힙의 조건에 부합하기 위해 자리를 바꿔준다.
            if max_index != k:
                
                #값들의 자리를 바꿔준다
                self.H[k], self.H[max_index] = self.H[max_index], self.H[k] 
            
                #자리를 바꿨으면 , 바뀐자리에서 자식노드와 비교해야 하므로
                k = max_index
            
            #현재 노드가 자식노드들보다 크므로 이 노드에서는 더이상 비교할 필요X
            else:
                break

    
    def make_heap(self):
        """
        일반적인 리스트를 힙 자료구조로 만들어줌
        시간복잡도 : O(Nlog2N)
        """
        
        n = len(self.H)
        
        #가장 뒤에 있는 원소부터 heapify_down을 실행
        for k in range(n-1,-1,-1):
            self.heapify_down(k,n)
            
    def heapify_up(self,k:int):
        """
        만약 자식노드가 부모노드보다 크다면 그때 자식노드와 부모노드의 위치를 바꾼다\n
        바뀐자리에서도 똑같이 반복
        시간복잡도 : O(log2N)
        """
        
        #루트노드에 도달하지 않았으면서 & 현재 노드가 부모노드보다 크다면 둘의 자리를 바꿔줌
        #바꿔준다면, 새로 바뀐자리에서 다시 반복
        while k > 0 and self.H[(k-1)//2] < self.H[k] : 
            self.H[k],self.H[(k-1)//2] = self.H[(k-1)//2], self.H[k]
            k = (k-1) // 2
    
    def insert(self,key:int):
        """
        값을 추가한 후, 힙 조건에 맞게 정렬
        """
        self.H.append(key)
        self.heapify_up(len(self.H)-1)
        
    def find_max(self):
        """
        가장 큰 값, 즉 루트노드를 리턴
        """
        return self[0]
    
    def delete_max(self) -> int:
        """
        가장 큰 값, 즉 루트노드를 삭제
        """
        H = self.H
        
        if len(self.H) == 0 : 
            return None
        
        
        key = H[0]
        
        #맨 마지막의 값을 루트위치로
        H[0],H[len(H)-1] = H[(len(H)-1)],H[0]
        
        #맨 마지막으로 이동된 루트값 삭제
        H.pop()
        
        #루트 위치로 이동된 노드의 위치를 정리
        self.heapify_down(0,len(H))
        
        #일반적인 pop 처럼삭제되는 루트노드의 값 리턴
        return key
    

#test_code
H = Heap([1,2,3,4,5])
print(H)
H.insert(8)
print(H)
H.delete_max()
print(H)