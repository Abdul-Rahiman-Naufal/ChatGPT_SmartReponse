from os import path
import os
import time
import openai
import requests
import sys
from pathlib import Path

'''arg1 = 
'''

alarmID=sys.argv[1]

def virtualAsnalyst():

  try:

    out=''
    my_dict = {}

    filename="C:/ChatGPT_SmartResponse/ChatGPT.conf"

    with open(filename, "r") as f:
        for line in f:
            key, value = line.strip().split(":")
            my_dict[key] = value

    
    SRP_API=str(my_dict['SRP_API'])
    openai.api_key=str(my_dict['ChatGPT_API'])
    Prefix=str(my_dict['PrefixSearch'])

    URL = "http://localhost:8505/lr-drilldown-cache-api/drilldown/"+str(alarmID)

    headers = {"Authorization": "Bearer "+str(SRP_API)}

    response = (requests.get(URL, headers=headers,json={"Content-Type": "application/json"}, verify=False)).json()
    log_Message=response['Data']['DrillDownResults']['RuleBlocks'][0]['DrillDownLogs']
    alarm_Name=str(response['Data']['DrillDownResults']['AIERuleName'])

    search = Prefix+' alarm Name:"'+alarm_Name+'" , Log: '+log_Message

    response = openai.Completion.create(
      engine="text-davinci-003",
      prompt=search,
      max_tokens=1024,
      n=1,
      stop=None,
      temperature=0.7
    )

    out=response['choices'][0]['text']

  except Exception as e:
          out=str(e)
          print(out)
          return False

  print(out)
  return True
  


for i in [1,2,3,4,5]:
    waiting=60
    print("Waiting "+str(waiting)+" seconds for AIE to generate Drilldown Results")
    time.sleep(waiting)
    if(virtualAsnalyst()==True):
        break
