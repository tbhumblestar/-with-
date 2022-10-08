class Heap:
    def __init__(self, L=[]): # default: 빈 리스트 
        self.A = L
        self.make_heap() # A의 값을 힙성질이 만족되도록 # make_heap 함수 호출 
    
    def __str__(self):
        return str(self.A)
    
    def heapify_down(self, k, n):
        # k : 검사가 진행되는 현재 노드의 인덱스. 즉 A[k]가 현재 노드가 됨
        # n = 힙의 전체 노드수 [heap_sort를 위해 필요함]
        # A[k]를 힙 성질을 만족하는 위치로 내려가면서 재배치
        while 2*k+1 < n: # 2*k + 1 == n이면 현재 노드가 리프노드라는 뜻. 리프노드면 더이상 노드를 내려줄 필요가 없음
            
            L,R=2*k+1,2*k+2 # L , R 은 각각 A[k]의 자식노드의 인덱스
            
            #왼쪽 자식노드 부터 먼저 비교
            if self.A[L] > self.A[k]:
                #m은 max를 의미
                m=L 
            else:
                m=k
            
            #오른쪽 자식노드 비교. n이랑 R을 비교하는 이유는, n=R이면 애초부터 존재하지 않는 자식노드이기때문
            if R < n and self.A[R] > self.A[m]:
                m=R
                
            # m = A[k], A[L], A[R] 중 최대값의 인덱스
            
            #A[k]가 최대값이 아니면 
            if m!=k:
                
                #자리를 바꿔준다. 인덱스는 그대로 유지하고 값만 바꿔주면 됨
                self.A[k], self.A[m] = self.A[m], self.A[k] 
                
                #자리르 바꿧으니 최대값도 바뀜
                k=m
            
            #A[k]의 값이 제일 크니까 더이상 작업을 진행할 필요 X
            else:
                break # 

    
    def make_heap(self):
        n = len(self.A)
        #가장 뒤에 있는 원소부터 heapify_down을 실행
        for k in range(n-1, -1, -1):
            self.heapify_down(k, n)
            
    def heap_sort(self): 
        n = len(self.A)
        for k in range(len(self.A)-1, -1, -1): 
            self.A[0],self.A[k] = \
                self.A[k],self.A[0]
            n = n - 1 # A[n-1]은 정렬되었으므로 self.heapify_down(0, n)

    
    #
    def heapify_up(self, k):# 올라가면서 A[k]를 재 배치 
        """
        새로운 리프노드가 추가될 경우에 사용
        새 리프노드가 부모노드보다 클 수도 있으니까, 그때 리프노드를 부모노드와 위치를 바꿔준다
        """
        
        #루트노드에 도달하지 않았으면서 & 부모노드보다 작다면
        while k>0 and self.A[(k-1)//2] < self.A[k] :
            self.A[k], self.A[(k-1)//2] = \
                self.A[(k-1)//2], self.A[k]
            k = (k-1)//2
            
    def insert(self, key):
        self.A.append(key)
        self.heapify_up(len(self.A)-1)
        
    def delete_max(self):
        if len(self.A) == 0: 
            return None
        key = self.A[0]
        self.A[0], self.A[len(self.A)-1] = \
        self.A[len(self.A)-1], self.A[0] 
        self.A.pop() # 실제로 리스트에서 delete!
        self.heapify_down(0, len(self.A)) # len(A) = n-1 
        return key
    
    def find_max(self):
        """
        가장 큰 값, 즉 루트노드를 리턴
        """
        return self[0]
    
    def delete_max(self):
        """
        가장 큰 값, 즉 루트노드를 삭제
        """
        
        if len(self.A) == 0 : 
            return None
        
        H = self.A
        
        key = H[0]
        
        #맨 마지막의 값을 루트위치로
        H[0],H[len(H)-1] = H[(len(H)-1)],H[0]
        
        #맨 마지막으로 이동된 루트값 삭제
        H.pop()
        
        #루트 위치로 이동된 노드의 위치를 정리
        self.heapify_down(0,len(H))
        
        #일반적인 pop 처럼삭제되는 루트노드의 값 리턴
        return key
