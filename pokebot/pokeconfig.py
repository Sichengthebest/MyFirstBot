import json
import os

def load_config():
   global CONFIG
   with open(config_file, 'r') as configfile:
      CONFIG = json.load(configfile)
   if not "token2" in CONFIG:
      CONFIG["token2"] = ""
   if not "pk" in CONFIG:
      CONFIG["pk"] = {}
   
   return CONFIG

def save_config():
   with open(config_file, 'w') as configfile:
         json.dump(CONFIG, configfile, indent=4,ensure_ascii=False)

CONFIG = {}
config_file = '/pokebot/poke.json'

run_path = os.getcwd()

def save_backup_config():
   with open(config_file, 'w') as configfile:
      json.dump(CONFIG, configfile, indent=4,ensure_ascii=False)