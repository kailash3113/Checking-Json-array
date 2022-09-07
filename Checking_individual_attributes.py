import json

with open(r"C:\Users\KAILASH\Desktop\task 4\books.json",'r',encoding="utf8") as f1:   
    arr1 = json.load(f1)
    
with open(r"C:\Users\KAILASH\Desktop\task 4\custom.json",'r',encoding="utf8") as f2:    
    arr2 = json.load(f2)
 
author_lst1 = []
author_lst2 = []
title_lst1 = []
title_lst2 = []
location_lst1 = []
location_lst2 = []
publisher_lst1 = []
publisher_lst2 = []
date_lst1 = []
date_lst2 = []
tup_data1  = []
tup_data2  = []
type_lst1 = []
type_lst2 = []

def json_array_comparing(data1,data2):   
        
    for i,j in zip(data1,data2):
        json_dump1 = json.dumps(i)
        json_dump2 = json.dumps(j)
        json1_dict = json.loads(json_dump1)
        json2_dict = json.loads(json_dump2)
    
        def sorting_the_array(item):
            if isinstance(item, dict):
                return sorted((key, sorting_the_array(values)) for key, values in item.items())
            if isinstance(item, list):
                return sorted(sorting_the_array(x) for x in item)
            else:   
                return item  
            
        
        print(sorting_the_array(json1_dict) == sorting_the_array(json2_dict))
        
        print(sorting_the_array(json1_dict))
        
        print("\n")
                
        print(sorting_the_array(json2_dict))
        
        print("\n")
        
        def complete_conversion(tup_data_1,tup_data_2):
            def conversion(tup, dict):
                for x, y in tup:
                    dict.setdefault(x, []).append(y)
                return dict
            dictionary1 = {}
            dictionary2 = {}
            tuple_to_dict_1 = conversion(tup_data_1, dictionary1)
            tuple_to_dict_2 = conversion(tup_data_2, dictionary2)

            if "author" in tuple_to_dict_1 and "author" in tuple_to_dict_2 :
                if (tuple_to_dict_1["author"] != tuple_to_dict_2["author"]):
                    author_lst1.append(tuple_to_dict_2["author"])
                else:
                    author_lst2.append(tuple_to_dict_1["author"])

                
            if "title" in tuple_to_dict_1 and "title" in tuple_to_dict_2 :
                if (tuple_to_dict_1["title"] != tuple_to_dict_2["title"]):
                    title_lst1.append(tuple_to_dict_2["title"])
                else:
                    title_lst2.append(tuple_to_dict_1["title"])
                    
                
            if "location" in tuple_to_dict_1 and "location" in tuple_to_dict_2 :
                
                if (tuple_to_dict_1["location"] != tuple_to_dict_2["location"]):
                    
                    location_lst1.append(tuple_to_dict_2["location"])
                    
                else:
                    
                    location_lst2.append(tuple_to_dict_1["location"])
            
            if "publisher" in tuple_to_dict_1 and "publisher" in tuple_to_dict_2 :
                if (tuple_to_dict_1["publisher"] != tuple_to_dict_2["publisher"]):
                    publisher_lst1.append(tuple_to_dict_2['publisher'])
                else:
                    publisher_lst2.append(tuple_to_dict_1['publisher'])
                
                if "date" in tuple_to_dict_1 and "date" in tuple_to_dict_2 :
                    if (tuple_to_dict_1["date"] != tuple_to_dict_2["date"]):
                        date_lst1.append(tuple_to_dict_2['date'])
                    else:
                        date_lst2.append(tuple_to_dict_1['date'])
                
                if "type" in tuple_to_dict_1 and "type" in tuple_to_dict_2 :
                    if (tuple_to_dict_1["type"] != tuple_to_dict_2["type"]):
                        type_lst1.append(tuple_to_dict_2['type'])
                    else:
                        type_lst2.append(tuple_to_dict_1['type'])
                        
                
    
        print("Arrays are equal for author :",len(author_lst2))
        print("Arrays are not equal for author :",len(author_lst1))
        print("Arrays are equal for  title :",len(title_lst2))
        print("Arrays are not equal for title :",len(title_lst1))
        print("Arrays are equal for  location :",len(location_lst2))
        print("Arrays are not equal for location :",len(location_lst1))
        print("Arrays are equal for  publisher :",len(publisher_lst2))
        print("Arrays are not equal for publisher :",len(publisher_lst1))
        print("Arrays are equal for  date :",len(date_lst2))
        print("Arrays are not equal for date :",len(date_lst1))
        print("Arrays are equal for  type :",len(type_lst2))
        print("Arrays are not equal for type :",len(type_lst1))


        complete_conversion(sorting_the_array(json1_dict),sorting_the_array(json2_dict))   


json_array_comparing(arr1,arr2) #for checking the file - json_array_comparing(arr1,arr2)


