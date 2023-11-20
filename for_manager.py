import pickle
import datetime

class MEquipment:                                            #장비 객체
    def __init__(self,type,detail,deadline,total):
        self.type=type
        self.detail=detail                                  #세부 사항은 딕셔너리(분류:[속성1, 속성2]) 형식으로 저장, 예를 들어 ("색상":["빨강","파랑","검정"]) 그러니깐 딕셔너리 아이템으로 리스트
        self.deadline=deadline
        self.total=total                                    #총 장비 개수
        self.num=total                                      #장비 잔여 개수(동아리 방)
        self.owner_ID=[]                                    #누가 빌려 갔는 지?(ID로 저장, 자료형은 고민)

class User:
    def __init__(self,ID):
        self.ID=ID
        self.own


def init_program():
    with open('data.p', 'rb') as file:    # james.p 파일을 바이너리 읽기 모드(rb)로 열기
        name = pickle.load(file)

def exit_program():                     #프로그램 값과 저장되어있는 값 다르면 수정사항 저장할 것이냐고 묻는 분기 추가
    print("exiting the program")
    exit()

def save_data(all_equipment_dic, users_dic):
    with open('data.p', 'wb') as file:
        pickle.dump(all_equipment_dic, file)
        pickle.dump(users_dic, file)

def input_new_equipment_type():
    type=input('새로운 장비를 입력하세요\n>>')
    if type in all_equipment_dic:
        print(type+"는 이미 존재합니다.")
    else:
        all_equipment_dic[type]=[]

def print_equipment_types(all_equipment_dic):
    print("아래는 현재 존재하는 장비 종류입니다\n\n")
    for type in all_equipment_dic:
        print(type)

def interface_main_page(all_equipment_dic):
    print_equipment_types(all_equipment_dic)
    print("q:프로그램 종료,s:저장,a:장비 종류 추가,d:장비 종류 삭제, g (장비 종류): 해당 장비 메뉴로 이동\n")           #유저 빌려간 장비 확인.
    op=input('>>')
    if op=='q':
        exit_program()
    elif op =='s':
        save_data()
    elif op == 'a':
        input_new_equipment_type()
    elif op == 'g':
        type=input()

def borrow_equipment(self, user_id):
        if self.num > 0:  # Check if there is equipment to borrow
            self.num -= 1
            self.owner_ID.append({'user_id': user_id, 'date_borrowed': datetime.now()})
            print(f"{self.type} has been borrowed by the user {user_id}.")
        else:
            print(f"Sorry, no {self.type} available to be borrowed.")

def return_equipment(self, user_id):
        for item in self.owner_ID:
            if item['user_id'] == user_id:  # Check if the user borrowed this equipment
                item['date_returned'] = datetime.now()
                self.num += 1
                print(f"{self.type} has been returned by id {user_id}.")
                break
        else:
            print(f"The user {user_id} did not borrow {self.type}.")

all_equipment_dic={}
users_dic={}










# 날짜 클래스 관련
# https://www.daleseo.com/python-datetime/
# https://ctkim.tistory.com/entry/%ED%8C%8C%EC%9D%B4%EC%8D%AC-datetime-%EB%9D%BC%EC%9D%B4%EB%B8%8C%EB%9F%AC%EB%A6%AC-%EA%B0%80%EC%9E%A5-%EB%A7%8E%EC%9D%B4-%EC%82%AC%EC%9A%A9%ED%95%98%EB%8A%94-%ED%95%A8%EC%88%98

#객체 파일 저장 관련 (pickle module)
# https://dojang.io/mod/page/view.php?id=2327
