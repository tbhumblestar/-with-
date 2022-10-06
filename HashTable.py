from typing import Any

#충돌 회피 방법이 구현되어 있지 않은 기본적인 해시테이블
#hashtable 생성
hash_table = [0 for i in range(0,100)]


def hash_func(key:str) -> int:
    """
    받은 키값의 마지막글자를 아스키 코드로 변환하고, 변환된 글자를 100으로 나눈 나머지로 인덱스를 설정
    """
    hash_value = ord(key[-1])
    hash_index = hash_value % 100
    return hash_index

def save_data(key:str,value:Any) -> None:
    """
    Key에 매핑되는 인덱스로 해쉬 테이블에 Value를 저장
    """
    idx = hash_func(key)
    hash_table[idx]=value
    
def read_data(key:str) -> Any:
    """
    키 값으로 해쉬테이블을 찾아 값을 가져옴
    """
    idx = hash_func(key)
    return hash_table[idx]

#test
save_data('test_key','test_value')
print(hash_table)
print(read_data('test_key'))