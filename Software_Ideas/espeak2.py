import os
import json
import time


#take json file
with open('sim1_theatre_file.json', 'r') as read_file:
    data = json.load(read_file)


for chunks in data['chunks']:
    string = chunks['speakText']
    print(string)
    
    # sim1 speaks
    os.system('espeak -s 120 -vmb-us1 "{}"'.format(string))



# sim1 speaks
# os.system('espeak -s 120 -vmb-us1 "{}"'.format(string))
# 
# data["count"] = int(data["count"])
# data["timer"] = int(data["timer"])
# data["button"] = int(data["button"])
# data["servoPan"] = int(data["servoPan"])
# data["servoArmLeft"] = int(data["servoArmLeft"])
# 
# print("timer  ")
# print(data["timer"])
# 
# time.sleep(data["timer"])
# 
# #take next json file
# with open("sim1_theatre_file_2.json", "r") as read_file:
#     data = json.load(read_file)
# 
# string=[data["speakText"]]
# print(string)
# 
# # sim1 speaks
# os.system('espeak -s 120 -vmb-us1 "{}"'.format(string))
# 
# data["count"] = int(data["count"])
# data["timer"] = int(data["timer"])
# data["button"] = int(data["button"])
# data["servoPan"] = int(data["servoPan"])
# data["servoArmLeft"] = int(data["servoArmLeft"])
# 
# print("timer  ")
# print(data["timer"])
# 
# #take next json file
# with open("sim1_theatre_file_3.json", "r") as read_file:
#     data = json.load(read_file)
# 
# string=[data["speakText"]]
# print(string)
# 
# # sim1 speaks
# os.system('espeak -s 120 -vmb-us1 "{}"'.format(string))
# 
# data["count"] = int(data["count"])
# data["timer"] = int(data["timer"])
# data["button"] = int(data["button"])
# data["servoPan"] = int(data["servoPan"])
# data["servoArmLeft"] = int(data["servoArmLeft"])
# 
# print("timer  ")
# print(data["timer"])
# 
# 
# #take next json file
# with open("sim1_theatre_file_4.json", "r") as read_file:
#     data = json.load(read_file)
# 
# string=[data["speakText"]]
# print(string)
# 
# # sim1 speaks
# os.system('espeak -s 120 -vmb-us1 "{}"'.format(string))
# 
# data["count"] = int(data["count"])
# data["timer"] = int(data["timer"])
# data["button"] = int(data["button"])
# data["servoPan"] = int(data["servoPan"])
# data["servoArmLeft"] = int(data["servoArmLeft"])
# 
# print("timer  ")
# print(data["timer"])

