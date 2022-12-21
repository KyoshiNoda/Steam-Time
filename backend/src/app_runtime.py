# import psutil
# import time


# process_time={}
# timestamp = {}
# # while True:
# #     current_app = psutil.Process(13980)
# #     timestamp[current_app] = int(time.time())
# #     time.sleep(1)
# #     if current_app not in process_time.keys():
# #         process_time[current_app] = 0
# #     process_time[current_app] = process_time[current_app]+int(time.time())-timestamp[current_app]
# #     print(process_time)

# current_app = psutil.Process(13980)
# print(current_app.)
# # timestamp[current_app] = int(time.time())
# # print(timestamp)

import time
import psutil
def findProcessIdByName(processName):
    # Here is the list of all the PIDs of a all the running process 
    # whose name contains the given string processName
    listOfProcessObjects = []
    #Iterating over the all the running process
    for proc in psutil.process_iter():
       try:
           pinfo = proc.as_dict(attrs=['pid', 'name', 'create_time'])
           # Checking if process name contains the given name string.
           if processName.lower() in pinfo['name'].lower() :
               listOfProcessObjects.append(pinfo)
       except (psutil.NoSuchProcess, psutil.AccessDenied , psutil.ZombieProcess) :
           pass
    return listOfProcessObjects;
# Finding PIDs od all the running instances of process 
# which contains 'chrome' in it's name
listOfProcessIds = findProcessIdByName('Code')
if len(listOfProcessIds) > 0:
   print('Process Exists | PID and other details are')
   for elem in listOfProcessIds:
       processID = elem['pid']
       processName = elem['name']
       processCreationTime =  time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(elem['create_time']))
       print((processID ,processName,processCreationTime ))
else :
   print('No Running Process found with this text')


