import pickle                                               #it is for save data
import os.path
from datetime import date

class MEquipment:                                          # Objects for all equipment in the club                                          
    def __init__(self,type,detail,deadline,total):
        self.type=type
        self.detail=detail                                  #Details are stored in the form of a dictionary (category:[attribute1, attribute2]), for example ("color":["red","blue","black"]), so it is listed as a dictionary item.
        self.deadline=deadline                              #equipment life time stored as date class which in datetime module
        self.total=total                                    
        self.num=total                                      #Remaining number of equipment (in club room)
        self.owner_ID=[]                                    #Store who rented the equipment(as student ID)

class UEquipment:                                            # Object for equipment owned by the user   
    def __init__(self,type,detail,deadline,num):
        self.type=type
        self.detail=detail                                  
        self.deadline=deadline
        self.num=num


class User:                                                 #user object
    def __init__(self,ID):                                  
        self.ID=ID                                          #User student ID
        self.own={}                                         #Equipment rented by the user will be stored {"typename": [](list of Equipment of that type)}



def load_data():
    with open('data.p', 'rb') as file:
        all_equipment_dic = pickle.load(file)
        users_dic = pickle.load(file)
    return all_equipment_dic, users_dic

def save_data(all_equipment_dic, users_dic):
    with open('data.p', 'wb') as file:
        pickle.dump(all_equipment_dic, file)
        pickle.dump(users_dic, file)
    print('저장이 완료되었습니다!')


def load_data():
    with open('data.p', 'rb') as file:
        all_equipment_dic = pickle.load(file)
        users_dic = pickle.load(file)
    return all_equipment_dic, users_dic

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

def exit_program():    
    print("exiting the program")
    exit()

def interface_main_page():
    while(True):
            print("q:Program exit\n")
            op=input('>>')
            if op=='q':
                exit_program()
            else:
                print(op+'is a command that does not exist!')


init_program()