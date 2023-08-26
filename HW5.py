import xmltodict
from dict2xml import dict2xml
import json
test_dict = {
    'user1': {'gender': 'm',
              'firstname': 'Vasya',
              'lastname': 'Pupkin',
              'age': 20},
    'user2': {'gender': 'f',
              'firstname': 'Vasilisa',
              'lastname': 'Pupkina',
              'age': 21}
}
####################################################################first#########################################################################
xml = dict2xml(test_dict, wrap ='root', indent ="   ")
with open("answer_HW5_1.xml","w") as f:
    f.write(xml)
###########################################################################################second#######################################################
with open("answer_HW5_1.xml","r") as f:
    file = f.read()
test_dict2 = xmltodict.parse(file)
test_dict2 = test_dict2.get("root")
for i in test_dict2.values():
    i["age"] = int(i["age"])
print(test_dict)
print(test_dict2)
##################################################################################################third#####################################################
json_file = json.dumps(test_dict, indent = 4)
with open("answer_HW5_3.json","w") as f:
     f.write(json_file)
############################################################################################fourth###################################################
with open("answer_HW5_3.json", "r") as f:
    test_dict3 = json.load(f)
print(test_dict)
print(test_dict3)
###########################################################################fivth#############################################################
with open("answer_HW5_1.xml","r") as f:
    file = f.read()
test_dict3 = xmltodict.parse(file)
json_file = json.dumps(test_dict3, indent = 4)
with open("answer_HW5_5.json","w") as f:
     f.write(json_file)