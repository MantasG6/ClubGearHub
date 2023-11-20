import pickle
import os.path

class MEquipment:                                            #장비 객체
    def __init__(self,type,detail,deadline,total):
        self.type=type
        self.detail=detail                                  #세부 사항은 딕셔너리(분류:[속성1, 속성2]) 형식으로 저장, 예를 들어 ("색상":["빨강","파랑","검정"]) 그러니깐 딕셔너리 아이템으로 리스트
        self.deadline=deadline                              #장비 수명
        self.total=total                                    #총 장비 개수
        self.num=total                                      #장비 잔여 개수(동아리 방)
        self.owner_ID=[]                                    #누가 빌려 갔는 지?(ID로 저장, 자료형은 고민)

class UEquipment:
    def __init__(self,type,detail,deadline,num):
        self.type=type
        self.detail=detail                                  #세부 사항은 딕셔너리(분류:[속성1, 속성2]) 형식으로 저장, 예를 들어 ("색상":["빨강","파랑","검정"]) 그러니깐 딕셔너리 아이템으로 리스트
        self.deadline=deadline
        self.num=num


class User:                                                 #사용자 객체
    def __init__(self,ID):                                  
        self.ID=ID                                          #사용자 학번
        self.own={}                                          #유저가 가지고 있는 장비들, 타입별로 dictionary로 저장될 것임.

def load_data():
    with open('data.p', 'rb') as file:    # data.p 파일을 바이너리 읽기 모드(rb)로 열기
        all_equipment_dic = pickle.load(file)
        users_dic = pickle.load(file)
    return all_equipment_dic, users_dic

def save_data(all_equipment_dic, users_dic):
    with open('data.p', 'wb') as file:
        pickle.dump(all_equipment_dic, file)
        pickle.dump(users_dic, file)
    print('저장이 완료되었습니다!')

def init_program():
    if os.path.isfile('data.p'):
        all_equipment_dic, users_dic = load_data()
    else:
        all_equipment_dic={}
        users_dic={}
    user = login(users_dic)
    interface_main_page()


def login(users_dic):
    ID = input('input your student ID\n>> ')
    if not ID in users_dic:
        users_dic[ID]=User(ID)
    return users_dic[ID]

def exit_program():                     #프로그램 값과 저장되어있는 값 다르면 수정사항 저장할 것이냐고 묻는 분기 추가
    print("exiting the program")
    exit()

def interface_main_page():
    while(True):
            print("q:Program exit\n")
            op=input('>>')
            if op=='q':
                exit_program()
            else:
                print(op+'는 존재하지 않는 명령임!')


init_program()