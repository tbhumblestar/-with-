#Stack
class Stack:
    
    #데이터 저장을 위한 리스트 준비
    def __init__(self):
        self.items = []
    
    #데이터 추가
    def push(self,val):
        self.items.append(val)
    
    #데이터 삭제    
    def pop(self,val):
        try:
            return self.items.pop()
        except IndexError:
            print("Stack is empty!")
    
    #맨 위에 있는 데이터가 무엇인지 확인
    def top(self):
        try:
            return self.items[-1]
        except IndexError:
            print("Stack is empty!")

    #stack의 길이 반환
    def __len__(self):
        return len(self.items)
