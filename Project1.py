import os
import ast
#****************************************************************************#
#Create a new Id password list.#
def create_list(name):
    
    f1=open(name,'w')
    id_pass=dict()
    n=int(input('Total number of id pass you want to store:'))
    for i in range(n):
        id1=input("Enter User_id:")
        pass1=input("Enter password:")
        id_pass[id1]=pass1
    f1.write(str(id_pass))
    f1.close()
    print("A new Id password list is created succesfully.")

#***************************************************************************#
#Open exsisting list and check for correct id password.#
def open_list(name):
    f1=open(name,'r')
    read_file=f1.read()
    id_pass_reference=ast.literal_eval(read_file) 
    user_id=input("Enter User_id:")
    if user_id not in id_pass_reference:
        print("Invalid user_id")
        return
    password=input("Enter password:")
    if password != id_pass_reference[user_id]:
        print("Incorrect Password.")
    else:
        print("Correct Password...User access granted.")
    f1.close()


#************************************************************#
option=input("Write '0' ->to create a new id password list.\nWrite '1' ->to open exsisting list and check for correct id password.\n")
name=input("Enter file name:")
name=name+'.txt'
if option=='0':
    create_list(name)
elif option=='1':
    open_list(name)