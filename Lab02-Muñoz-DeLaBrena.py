import json

with open("D:\\Program Files\\Documents\\Universidad\\Data Structures\\Tasks\\Lab02\\words (1).json") as file:
    
    data=json.load(file)
  
#print(data)

#print(data.keys())

#for element in data:
    
    #print(data.values())
   
#-------------------------------------------------------------------------------

json_Dict=data

#new_Name=input('Introduce a new name here: ')
#old_Name=input('Introduce the name you want to change here: ')

#category_choice=input('Introduce the name of the category you want to change here: ')
#new_Word=input('Introduce the word you want to add here: ')

#category_choice=input('Introduce the name of the category you want to change here: ')
#removed_word=input('Introduce the word you want to remove here: ')


def mod_Category_name(json_Dict,old_Name,new_Name):
    
    json_Dict[new_Name]=json_Dict[old_Name]
    del json_Dict[old_Name]
    
    return json_Dict

#-------------------------------------------------------------------------------
 

def add_Word(json_Dict,category_choice,new_Word):
    
    json_Dict[category_choice].append(new_Word)
    
    return json_Dict


#-------------------------------------------------------------------------------

def remove_Word(json_Dict,category_choice,removed_word):
    
    json_Dict[category_choice].remove(removed_word)
    
    return json_Dict
