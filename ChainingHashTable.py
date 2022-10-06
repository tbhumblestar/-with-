#HashTableChaining

from typing import Any

#hashtable 생성. 모든 슬롯은 기본적으로 빈 리스트임
hash_table = [[] for i in range(100)]


def hash_func(key:str) -> int:
    """
    받은 키값의 마지막글자를 아스키 코드로 변환하고, 변환된 글자를 100으로 나눈 나머지로 인덱스를 설정
    """
    hash_value = ord(key[-1])
    hash_index = hash_value % 100
    return hash_index

def save_func(key:str,value:Any) -> None:
    """
    Key에 매핑되는 해쉬테이블의 인덱스에 우선접근 \n
    해당 인덱스가 비어있다면 리스트를 만들고, [key,value]형태로 저장 \n
    해당 인덱스가 비어있지는 않았으나 동일한 키값이 존재하지 않는다면 [key,value]형태를 append \n
    해당 인덱스에 동일한 키값이 존재한다면, 해당 키값의 value를 업데이트
    
    """
    index = hash_func(key)
    
    #해당 슬롯이 비어 있지 않다면
    if hash_table[index]:
        for i in range(len(hash_table[index])):
            
            #해당 인덱스에 동일한 키값이 있다면 > 이미 들어잇던 데이터 > 업데이트 해줌
            if hash_table[index][i][0] == key:
                hash_table[index][i][1] = value
                return None
            
            #인덱스에 동일한 키값이 존재하지 않는 경우 > 업데이트
            hash_table[index].append([key,value])
            
    
    #해당 슬롯이 비어 있었다면
    else:
        hash_table[index].append([key,value])
    
def read_func(key:str) -> Any:
    """
    키 값에 매핑된 인덱스로 해쉬테이블에 접근\n
    접근한 인덱스에 일치하는 키값이 존재하는지 확인\n
    존재할 경우 Value를 리턴
    """
    index = hash_func(key)
    if hash_table[index] != 0:
        for i in range(len(hash_table[index])):
            
            #키를 찾은 경우
            if hash_table[index][i][0] == key:
                print("here")
                return hash_table[index][i][1]
            
        #인덱스는 비어있지 않으나 해당 인덱스에 키가 존재하지 않음
        print("Key Error!")
    
    else:
        #인덱스 자체가 비어있음
        print("Key Error!")

#test
save_func("test_key","test_value")
a = read_func("test_key")
b = read_func("test_key2")
print(a)