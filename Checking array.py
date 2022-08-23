import json

with open(r'C:\Users\KAILASH\Desktop\books.json','r') as f1:
    arr1 = json.load(f1)
    
with open(r'C:\Users\KAILASH\Desktop\first_10.json','r') as f2:
    arr2 = json.load(f2)
    

#sample arrays - Output(True)
json_1 = [{"Name":"GFG", "Class": "Website", "Domain":"CS/IT", "CEO":"Sandeep Jain","Subjects":["DSA","Python","C++","Java"]}]
  
json_2 = [{"CEO":"Sandeep Jain","Subjects":["C++","Python","DSA","Java"], "Domain":"CS/IT","Name": "GFG","Class": "Website"}]
  

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
            
        print("\n")

        print(sorting_the_array(json1_dict) == sorting_the_array(json2_dict))
        
        print(sorting_the_array(json1_dict))
        
        print("\n")
        
        print(sorting_the_array(json2_dict))
        
                        

json_array_comparing(json_1,json_2) #for checking the file - json_array_comparing(arr1,arr2)

