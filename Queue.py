#Queue
class Queue:
    
    #데이터 저장을 위한 리스트 준비
    def __init__(self):
        self.items = []
        self.first_index = 0
    
    #데이터 추가
    def enqueue(self,val):
        self.items.append(val)
    
    #데이터 삭제    
    def dequeue(self):
        
        if self.first_index == len(self.items):
            print("queue is empty!")
            return None
        else:
            self.first_index += 1
            return self.items[self.first_index-1]
        
    def __len__(self):
        return len(self.items) - self.first_index
    

q = Queue()
for i in range(5):
    q.enqueue(i)

k = 2
count = 0
while len(q) != 1:
    count += 1
    person = q.dequeue()
    if count % k != 0:
        q.enqueue(person)
        
print(q.items[-1])