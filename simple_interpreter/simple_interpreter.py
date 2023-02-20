import sys
from collections import defaultdict

DATA_LIST =[]
defined_variable = defaultdict(bool)
variable_value = defaultdict(int)
data_val_in_dict = defaultdict(bool)


def check_uninary(op):
    if(op.strip()=="-" or op.strip()=="not"):
        return True
    return False

def check_binary(op):
    temp = op.strip()
    L = ["+","-","*","/",">","<",">=","<=","==","!=","and","or"]
    if temp in L:
        return True
    return False

def check_integer(davedar):
    try:
        if(str(int(davedar)).strip()== str(davedar).strip()):
            return True
    except:
        return False

def check_term(davedar):
    if( davedar.strip()=="True" or davedar.strip()=="False" or check_integer(davedar) ):
        return True
    dd = davedar.strip()
    for i in range(len(dd)):
        if( ord('a') <=ord(dd[i])<= ord('z') or ord('A') <=ord(dd[i])<= ord('Z')):
            pass
        else:
            return False
    return True

def check_variable_type(davedar):
    dd = davedar.strip()
    for i in range(len(dd)):
        if( ord('a') <=ord(dd[i])<= ord('z') or ord('A') <=ord(dd[i])<= ord('Z')):
            pass
        else:
            return False
    return True

def find_value(sona):
    if(sona=="True"):
        return True
    if(sona=="False"):
        return False
    if(check_integer(sona)):
        return int(sona)
    if(defined_variable[sona]):
        return variable_value[sona]
    print("Variable ‘"+str(sona)+"’ is not defined")
    sys.exit()

def set_var_val(variable, key1):
    key = find_value(key1)
    
    if(data_val_in_dict[key]==False):
        DATA_LIST.append([key])
        data_val_in_dict[key]= True
        
    if(defined_variable[variable]==False):
        defined_variable[variable] = True
        variable_value[variable] = key
        index = 0
        while(index<len(DATA_LIST) and (DATA_LIST[index][0]!=key or type(DATA_LIST[index][0])!= type(key)) ):
            index+=1
        if(index<len(DATA_LIST)):
            DATA_LIST.append([variable,index])
        else:
            DATA_LIST.append([key])
            DATA_LIST.append([variable,index])
    else:
        ind1 = 0
        while(True):
            if(ind1<len(DATA_LIST) and len(DATA_LIST[ind1])==2 and DATA_LIST[ind1][0]== variable):
                break
            else:
                ind1 = ind1 + 1
        
        variable_value[variable] = key
        index = 0
        while(index<len(DATA_LIST) and (DATA_LIST[index][0]!=key or type(DATA_LIST[index][0])!= type(key))):
            index+=1
                
        if(index<len(DATA_LIST)):
            DATA_LIST[ind1][1] = index
        else:
            DATA_LIST.append([key])
            DATA_LIST[ind1][1] = index


Input = open("input_file.txt","r")
Lines = Input.readlines()
n = len(Lines)   # number of commands

for line in Lines:
    if(line=="\n"):
        continue
    else:
        mycommand = line.strip()
        listform = mycommand.split()
        
        if(len(listform)==3 and listform[1]=="="):
            value_to_set  = find_value(listform[2])
            if(check_variable_type(listform[0])):
                set_var_val(listform[0], listform[2])
            else:
                print("Kuch jhol hua hai in expression = ", mycommand)
                sys.exit()
                
        elif(len(listform)==4 and listform[1]=="="):
            # x = - 5 , x = not 5
            if(check_variable_type(listform[0])==False):
                print("Kuch jhol hua hai in expression = ", listform[0])
            
            if( (listform[2]=="-") and check_integer(find_value(listform[3])) ):
                set_var_val(listform[0], -int(find_value(listform[3])))
            elif( (listform[2]=="not") and find_value(listform[3].strip())==True and type(find_value(listform[3].strip()) ) ==bool):
                set_var_val(listform[0], "False")
            elif( (listform[2]=="not") and find_value(listform[3].strip())==False and type(find_value(listform[3].strip()) )==bool):
                set_var_val(listform[0], "True")
            else:
                print("Something went wrong in command:", mycommand )
                sys.exit()

        elif(len(listform)==5 and listform[1]=="="):
            
            try:
                val1 = find_value(listform[2])
                if(data_val_in_dict[val1]==False):
                    DATA_LIST.append([val1])
                    data_val_in_dict[val1]= True
                    
                val2 = find_value(listform[4])
                if(data_val_in_dict[val2]==False):
                    DATA_LIST.append([val2])
                    data_val_in_dict[val2]= True
                
                oper = listform[3]
                if( (check_variable_type(listform[0])==False) or (check_binary(oper)==False) ):
                    temp = 2/0
                
                key = -1
                i_am_bool = False
                if(oper=="+"):
                    key = val1+ val2
                elif(oper=="-"):
                    key = val1- val2
                elif(oper=="*"):
                    key = val1* val2
                elif(oper=="/"):
                    if(val2==0):
                        print("DIVISON BY 0")
                        sys.exit()
                    key = val1//val2
                elif(oper==">"):
                    key = (val1>val2)
                    i_am_bool = True
                elif(oper=="<"):
                    key = (val1<val2)
                    i_am_bool = True
                elif(oper==">="):
                    key = (val1>=val2)
                    i_am_bool = True
                elif(oper=="<="):
                    key = (val1<=val2)
                    i_am_bool = True
                elif(oper=="=="):
                    key = (val1==val2)
                    i_am_bool = True
                elif(oper=="!="):
                    key = (val1!=val2)
                    i_am_bool = True
                elif(oper=="and"):
                    key = (val1 and val2)
                    i_am_bool = True
                elif(oper == "or"):
                    key = (val1 or val2)
                    i_am_bool = True
                else:
                    print("Operator out of list it seems !!", oper)
                    sys.exit()
                
                if(i_am_bool==True):
                    if(key):
                        key = "True"
                    else:
                        key = "False"  

                set_var_val(listform[0], key)
            except:
                print("Something went wrong in expression = ", mycommand)
                sys.exit()
        else:
            print("Something went wrong in expression = ", mycommand)
            sys.exit()

data_list = []
for item in DATA_LIST:
    if(len(item)==1):
        data_list.append(item[0])
    else:
        data_list.append((item[0],item[1]))
garbage = [True for i in range(len(DATA_LIST))]

for i in range(len(DATA_LIST)):
    if(len(DATA_LIST[i])==2 ):
        garbage[i]= False
        garbage[DATA_LIST[i][1]] = False


Garbage_values = []
for i in range(len(garbage)):
    if(garbage[i]):
        Garbage_values.append(data_list[i])

print(data_list)
print(Garbage_values)