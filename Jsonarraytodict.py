import os 
import json 

dict_components = {} # Getting the dictionary of the component in the json array data 
f = open("/mnt/c/Users/Kornbotdev/AppData/Local/Programs/Robotics_nodes_json/codeconfiggen.json") # Getting the code config gen json to running on the code system 
datacom = json.load(f)
print(datacom)
for ire in range(0,len(datacom)): 
        print(datacom[ire]) # Getting the ire 
        if len(datacom[ire]) == 2: 
                dict_components[datacom[ire][0]] = datacom[ire][1] 
        if len(datacom[ire]) >2: 
                 getsplit_com = datacom[ire].split(":")
                 dict_components[getsplit_com[0]] = getsplit_com[1] 
print(dict_components) 
json_dumpcom = json.dumps(dict_components)
writejson_Com = open("Components_node_robotics.json","w")
writejson_Com.write(json_dumpcom) #Write the json component 
writejson_Com.close()                

