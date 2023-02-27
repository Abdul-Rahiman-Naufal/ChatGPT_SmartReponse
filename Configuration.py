import os
from pathlib import Path
from datetime import datetime
import sys

'''arg1 = 
   arg2 =
'''

SRP_API=str(sys.argv[1])
ChatGPT_API=str(sys.argv[2])


data = {
    "SRP_API":SRP_API,
    "ChatGPT_API":ChatGPT_API,
    "PrefixSearch":"Analyse and investigate"
}

folder_name = 'C:/ChatGPT_SmartResponse/'

if not os.path.exists(folder_name):
      os.makedirs(folder_name)

file_name = 'ChatGPT.conf'
file_path = os.path.join(folder_name, file_name)

with open(file_path, "w") as f:
    for key, value in data.items():
        f.write(f"{key}:{value}\n")